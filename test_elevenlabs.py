import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

load_dotenv()

api_key = os.getenv("ELEVENLABS_API_KEY")
voice_id = os.getenv("ELEVENLABS_VOICE_ID")

if not api_key:
    raise Exception("ELEVENLABS_API_KEY not found")

client = ElevenLabs(api_key=api_key)

audio = client.text_to_speech.convert(
    voice_id=voice_id,
    model_id="eleven_multilingual_v2",
    text="नमस्ते दोस्तों! आज निफ्टी फिफ्टी में ज़बरदस्त गिरावट देखने को मिली है। आइए जानते हैं इसके पीछे की वजह।"
)

os.makedirs("output/audio", exist_ok=True)

output_file = "output/audio/eleven_test.mp3"

with open(output_file, "wb") as f:
    for chunk in audio:
        if chunk:
            f.write(chunk)

print("=" * 40)
print("ElevenLabs Test Successful")
print(output_file)
print("=" * 40)