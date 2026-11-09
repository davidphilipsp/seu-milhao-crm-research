import json, re
import numpy as np
import parselmouth
import librosa
import soundfile as sf

import glob, os
OUT = os.environ.get("SPEECH_DIR", ".")  # folder with <name>.wav files (mono 16 kHz)
NAMES = sorted(os.path.splitext(os.path.basename(p))[0] for p in glob.glob(os.path.join(OUT, "*.wav")))
PAUSE = 0.35

def mmss(t):
    m = int(t // 60); s = t - m*60
    return f"{m:02d}:{s:05.2f}"

def phrase_at(segs, t):
    for s in segs:
        if s["start"] - 0.05 <= t <= s["end"] + 0.05:
            return s["text"].strip()
    # nearest
    s = min(segs, key=lambda s: min(abs(s["start"]-t), abs(s["end"]-t)))
    return s["text"].strip() + " (frase mais próxima)"

def peaks(times, values, n=3, min_sep=1.0):
    order = np.argsort(values)[::-1]
    chosen = []
    for i in order:
        if np.isnan(values[i]): continue
        if all(abs(times[i]-times[j]) >= min_sep for j in chosen):
            chosen.append(i)
        if len(chosen) == n: break
    return chosen

results = {}
for name in NAMES:
    d = json.load(open(f"{OUT}/{name}.json"))
    segs = d["segments"]
    words = [w for s in segs for w in s["words"]]
    audio, sr = sf.read(f"{OUT}/{name}.wav", dtype="float32")
    total = len(audio)/sr

    # speech runs: merge words separated by gaps <= PAUSE
    runs = []
    cur = [words[0]["start"], words[0]["end"]]
    pauses = []
    for prev, w in zip(words, words[1:]):
        gap = w["start"] - prev["end"]
        if gap > PAUSE:
            pauses.append({"start": prev["end"], "end": w["start"], "dur": gap,
                           "before": prev["word"].strip(), "after": w["word"].strip()})
            runs.append(cur); cur = [w["start"], w["end"]]
        else:
            cur[1] = max(cur[1], w["end"])
    runs.append(cur)
    speech_time = sum(e-s for s, e in runs)
    n_words = len(words)
    wpm = n_words / (speech_time/60)
    top_pauses = sorted(pauses, key=lambda p: -p["dur"])[:3]

    # pitch via parselmouth
    snd = parselmouth.Sound(f"{OUT}/{name}.wav")
    pitch = snd.to_pitch(time_step=0.01, pitch_floor=75, pitch_ceiling=500)
    f0 = pitch.selected_array["frequency"]
    tt = pitch.xs()
    voiced = f0 > 0
    f0v = f0[voiced]; tv = tt[voiced]
    # median smoothing (window 5) on voiced contour to suppress octave glitches
    f0s = np.array([np.median(f0v[max(0,i-2):i+3]) for i in range(len(f0v))])
    pk = peaks(tv, f0s, 3, 1.0)
    f0_peaks = [{"t": float(tv[i]), "f0": float(f0s[i]), "phrase": phrase_at(segs, tv[i])} for i in pk]

    # RMS energy via librosa
    rms = librosa.feature.rms(y=audio, frame_length=1024, hop_length=256)[0]
    rt = librosa.frames_to_time(np.arange(len(rms)), sr=sr, hop_length=256)
    rk = peaks(rt, rms, 3, 1.0)
    rms_peaks = [{"t": float(rt[i]), "rms": float(rms[i]), "db": float(20*np.log10(rms[i]+1e-9)), "phrase": phrase_at(segs, rt[i])} for i in rk]

    results[name] = {
        "total": total, "speech_time": speech_time, "n_words": n_words, "wpm": wpm,
        "first_word": words[0]["start"], "last_word": words[-1]["end"],
        "n_pauses": len(pauses),
        "pause_mean": float(np.mean([p["dur"] for p in pauses])) if pauses else 0.0,
        "top_pauses": top_pauses,
        "f0_mean": float(np.mean(f0v)), "f0_median": float(np.median(f0v)),
        "f0_p10": float(np.percentile(f0v, 10)), "f0_p90": float(np.percentile(f0v, 90)),
        "voiced_frac": float(voiced.mean()),
        "f0_peaks": f0_peaks, "rms_peaks": rms_peaks,
    }
    r = results[name]
    print(f"== {name}: total {total:.2f}s | fala {speech_time:.2f}s | {n_words} palavras | {wpm:.0f} wpm")
    print(f"   pausas>{PAUSE}s: {r['n_pauses']} | média {r['pause_mean']:.2f}s | top: " + "; ".join(f"{mmss(p['start'])} {p['dur']:.2f}s ('{p['before']}'→'{p['after']}')" for p in top_pauses))
    print(f"   F0 média {r['f0_mean']:.0f} Hz | mediana {r['f0_median']:.0f} | p10-p90 {r['f0_p10']:.0f}-{r['f0_p90']:.0f}")
    for p in f0_peaks: print(f"   F0 pico {mmss(p['t'])} {p['f0']:.0f} Hz: {p['phrase']}")
    for p in rms_peaks: print(f"   RMS pico {mmss(p['t'])} {p['db']:.1f} dBFS: {p['phrase']}")

json.dump(results, open(f"{OUT}/metrics.json", "w"), ensure_ascii=False, indent=1)
