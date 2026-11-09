# speech-metrics

Small scripts used to study how presenters speak in short-form ads and stories: pace, pauses, pitch and emphasis.
No audio, transcripts or results are included.

| Script | What it does |
|---|---|
| `transcribe.py [model]` | faster-whisper (default `large-v3`, CPU int8, `language="pt"`, word timestamps, VAD) → `<name>.json` |
| `metrics.py` | words per minute over speech time, pauses > 0.35 s, F0 (praat-parselmouth) mean/median/p10–p90 and peaks, RMS (librosa) peaks → `metrics.json` |
| `refine.py` | median-smoothed F0, per-word loudness and emphasis (≥ +4 dB over median), voiced activity outside words |

```bash
pip install faster-whisper soundfile numpy librosa praat-parselmouth
ffmpeg -i clip.mp4 -ac 1 -ar 16000 clip.wav
SPEECH_DIR=/path/to/wavs python transcribe.py && SPEECH_DIR=/path/to/wavs python metrics.py && SPEECH_DIR=/path/to/wavs python refine.py
```
Only analyze recordings you have the right to process.
