import speech_recognition as sr


def get_voice_input(listener, microphone):
    with microphone as source:
        print("listening...")
        # get user input (voice)
        user_input = listener.listen(source)
        # uses Google API
        voice = listener.recognize_google(user_input)
        # makes sure input string is lowercase
        voice = voice.lower()
    return voice


def speech_to_text():
    listener = sr.Recognizer()
    microphone = sr.Microphone()

    input = get_voice_input(listener, microphone)
    return input


def translate_to_eng(input):
    pass
