import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

def split_audio(path:str, output_folder:str):
    audio = AudioSegment.from_wav(path)
    song_segments = split_on_silence(audio, silence_thresh=-16, min_silence_len=1000)

    basename = os.path.basename(path)
    for i, segment in enumerate(song_segments):
        segment.export(f"{output_folder}/{basename}_{i + 1}.wav", format="wav")
