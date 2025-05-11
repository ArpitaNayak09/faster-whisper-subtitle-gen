from faster_whisper import WhisperModel

model = WhisperModel("small")

segments, info = model.transcribe(r"C:\Users\HP\Videos\out3.mp4") # added the r before the string

results = []
for segment in segments:
    results.append({
        "start": segment.start,
        "end": segment.end,
        "text": segment.text.strip()
    })

def create_srt(results, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        for i, segment in enumerate(results):
            start_time = format_time(segment["start"])
            end_time = format_time(segment["end"])
            f.write(f"{i + 1}\n")
            f.write(f"{start_time} --> {end_time}\n")
            f.write(f"{segment['text']}\n\n")

def format_time(seconds):
    hours = int(seconds / 3600)
    minutes = int((seconds % 3600) / 60)
    seconds = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:06.3f}".replace(".", ",")

create_srt(results, "subtitles.srt")
print("Subtitles saved to subtitles.srt")