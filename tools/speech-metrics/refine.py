import json
import numpy as np, parselmouth, librosa, soundfile as sf
import glob, os
OUT = os.environ.get("SPEECH_DIR", ".")  # folder with <name>.wav files (mono 16 kHz)
NAMES = sorted(os.path.splitext(os.path.basename(p))[0] for p in glob.glob(os.path.join(OUT, "*.wav")))
def mmss(t):
    m = int(t // 60); return f"{m:02d}:{t-m*60:05.2f}"
def phrase_at(segs, t):
    for s in segs:
        if s["start"] - 0.05 <= t <= s["end"] + 0.05: return s["text"].strip(), True
    s = min(segs, key=lambda s: min(abs(s["start"]-t), abs(s["end"]-t)))
    return s["text"].strip(), False
def peaks(times, values, n=3, min_sep=1.0):
    order = np.argsort(values)[::-1]; chosen = []
    for i in order:
        if all(abs(times[i]-times[j]) >= min_sep for j in chosen): chosen.append(i)
        if len(chosen) == n: break
    return chosen
metrics = json.load(open(f"{OUT}/metrics.json"))
for name in NAMES:
    d = json.load(open(f"{OUT}/{name}.json")); segs = d["segments"]
    audio, sr = sf.read(f"{OUT}/{name}.wav", dtype="float32")
    snd = parselmouth.Sound(f"{OUT}/{name}.wav")
    pitch = snd.to_pitch(time_step=0.01, pitch_floor=100, pitch_ceiling=400)
    f0 = pitch.selected_array["frequency"]; tt = pitch.xs()
    v = f0 > 0; f0v = f0[v]; tv = tt[v]
    # 150 ms median smoothing on voiced contour
    f0s = np.array([np.median(f0v[max(0,i-7):i+8]) for i in range(len(f0v))])
    pk = peaks(tv, f0s, 3, 1.0)
    f0_peaks = []
    for i in pk:
        ph, inside = phrase_at(segs, tv[i])
        f0_peaks.append({"t": float(tv[i]), "f0": float(f0s[i]), "phrase": ph, "inside_words": inside})
    # raw outliers above 400 from earlier run (ceiling 500)
    p500 = snd.to_pitch(time_step=0.01, pitch_floor=75, pitch_ceiling=500).selected_array["frequency"]
    out_frames = int(((p500 > 400)).sum())
    # per-word loudness
    rms = librosa.feature.rms(y=audio, frame_length=1024, hop_length=256)[0]
    rt = librosa.frames_to_time(np.arange(len(rms)), sr=sr, hop_length=256)
    wdb = []
    for s in segs:
        for w in s["words"]:
            m = (rt >= w["start"]) & (rt <= w["end"])
            val = float(20*np.log10(rms[m].mean()+1e-9)) if m.any() else float("nan")
            w["db"] = val; wdb.append(val)
    med = float(np.nanmedian(wdb))
    for s in segs:
        for w in s["words"]:
            w["emph"] = bool(not np.isnan(w["db"]) and w["db"] >= med + 4.0)
    # non-speech vocal activity: voiced frames outside word spans (laugh candidates)
    spans = [(w["start"], w["end"]) for s in segs for w in s["words"]]
    def in_words(t): return any(a-0.05 <= t <= b+0.05 for a,b in spans)
    outside = [t for t in tv if not in_words(t)]
    # group into clusters
    clusters = []
    for t in outside:
        if clusters and t - clusters[-1][1] < 0.1: clusters[-1][1] = t
        else: clusters.append([t, t])
    clusters = [c for c in clusters if c[1]-c[0] >= 0.25]
    json.dump(d, open(f"{OUT}/{name}.json","w"), ensure_ascii=False, indent=1)
    m = metrics[name]
    m.update({"f0_mean": float(f0v.mean()), "f0_median": float(np.median(f0v)),
              "f0_p10": float(np.percentile(f0v,10)), "f0_p90": float(np.percentile(f0v,90)),
              "f0_peaks": f0_peaks, "f0_outlier_frames_gt400": out_frames,
              "word_db_median": med, "voiced_outside_words": clusters})
    print(f"== {name} F0 média {m['f0_mean']:.0f} mediana {m['f0_median']:.0f} p10-p90 {m['f0_p10']:.0f}-{m['f0_p90']:.0f} | frames>400Hz (teto 500): {out_frames}")
    for p in f0_peaks: print(f"   pico {mmss(p['t'])} {p['f0']:.0f} Hz inside={p['inside_words']}: {p['phrase']}")
    print(f"   mediana dB por palavra {med:.1f}; ênfases (>= +4 dB): " + ", ".join(f"{w['word'].strip()}({w['db']-med:+.1f})" for s in segs for w in s["words"] if w["emph"]))
    print(f"   vozeamento fora de palavras (>=0.25s): " + "; ".join(f"{mmss(a)}-{mmss(b)}" for a,b in clusters))
json.dump(metrics, open(f"{OUT}/metrics.json","w"), ensure_ascii=False, indent=1)
