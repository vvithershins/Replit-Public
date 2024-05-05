import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Speak the text
engine.say("Hello, how are you?")

# Wait for the speech to complete
engine.runAndWait()
