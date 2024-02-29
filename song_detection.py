import asyncio
from shazamio import Shazam

def detect_song(file:str):
    shazam = Shazam(language="de-DE", endpoint_country="DE")

    async def main():
        return await shazam.recognize(file)
    result = asyncio.run(main())
    track = result["track"]["title"]
    artist = result["track"]["subtitle"]
    return f"artist:{artist} track:{track}"
