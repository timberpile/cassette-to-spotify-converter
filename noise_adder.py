from pydub import AudioSegment
from pydub.generators import WhiteNoise

def add_noise_to_audio(input_path, output_path):
    audio: AudioSegment = AudioSegment.from_file(input_path)
    raw_noise = WhiteNoise(8000, 8)
    audio_len = len(audio)
    noise = raw_noise.to_audio_segment(duration=audio_len, volume=-30)
    audio_with_noise = audio.overlay(noise)
    audio_with_noise.export(output_path, format="wav")
