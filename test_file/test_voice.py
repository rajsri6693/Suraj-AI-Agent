from services.voice_service import VoiceService

script = """

नमस्कार दोस्तों।

आज निफ्टी 50 ने शानदार वापसी की है।

अगर ऐसी ही शेयर बाजार की अपडेट चाहते हैं
तो चैनल को सब्सक्राइब करें।

"""

voice = VoiceService()

path = voice.generate_audio(

    "Nifty 50 Today",

    script

)

print(path)