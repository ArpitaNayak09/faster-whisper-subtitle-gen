
# 🎬 Faster-Whisper Subtitle Generator

This is a Python project that transcribes audio from videos and generates `.srt` subtitle files using OpenAI's Whisper model (via faster-whisper).

## 🚀 Features
- Uses the small version of Whisper model
- Extracts subtitles with timestamps
- Saves them in standard `.srt` format for use in media players

## 🛠 Requirements
- Python 3.8+
- Install dependencies

## 📁 Usage
```python
from faster_whisper import WhisperModel

model = WhisperModel("small")
segments, info = model.transcribe("your_video.mp4")

# Converts and saves to subtitles.srt
