import json, sys, time
from faster_whisper import WhisperModel
import soundfile as sf
import numpy as np

import glob, os
OUT = os.environ.get("SPEECH_DIR", ".")  # folder with <name>.wav files (mono 16 kHz)
NAMES = sorted(os.path.splitext(os.path.basename(p))[0] for p in glob.glob(os.path.join(OUT, "*.wav")))
model_name = sys.argv[1] if len(sys.argv) > 1 else "large-v3"
t0 = time.time()
model = WhisperModel(model_name, device="cpu", compute_type="int8")
print(f"model {model_name} loaded in {time.time()-t0:.1f}s", flush=True)

for name in NAMES:
    t1 = time.time()
    segments, info = model.transcribe(
        sf.read(f"{OUT}/{name}.wav", dtype="float32")[0],
        language="pt",
        word_timestamps=True,
        vad_filter=True,
        temperature=0,
        beam_size=5,
        condition_on_previous_text=False,
    )
    data = {"file": name, "duration": info.duration, "model": model_name, "segments": []}
    for s in segments:
        data["segments"].append({
            "start": s.start, "end": s.end, "text": s.text,
            "avg_logprob": s.avg_logprob, "no_speech_prob": s.no_speech_prob,
            "words": [{"start": w.start, "end": w.end, "word": w.word, "prob": w.probability} for w in (s.words or [])],
        })
    suffix = "" if model_name == "large-v3" else f".{model_name}"
    with open(f"{OUT}/{name}{suffix}.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    print(f"{name}: {len(data['segments'])} segments in {time.time()-t1:.1f}s", flush=True)
    for s in data["segments"]:
        print(f"  [{s['start']:6.2f}-{s['end']:6.2f}] lp={s['avg_logprob']:.2f} ns={s['no_speech_prob']:.2f} {s['text']}")
