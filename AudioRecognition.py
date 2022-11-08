import speech_recognition as speech_recog
from textProceed import *


def audio_message(audio_link):
    sample_audio = speech_recog.AudioFile(audio_link)
    with sample_audio as audio_file:
        audio_content = speech_recog.record(audio_file)
        exitText = speech_recog.recognize_goole(audio_content)
        return exitText
