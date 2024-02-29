import os
from pydub import AudioSegment

def combine_audio_in_directory(directory, output_file):
    combined = None

    for filename in os.listdir(directory):
        if filename.endswith(".opus"):  # Adjust the file extension if needed
            file_path = os.path.join(directory, filename)
            audio = AudioSegment.from_file(file_path)

            if combined is None:
                combined = audio
            else:
                combined += audio

    if combined:
        combined.export(output_file, format="opus")
    else:
        print("No audio files found in the specified directory.")
