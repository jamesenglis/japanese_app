import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
from io import BytesIO

st.title("🇯🇵 English → Japanese Learning App")
st.write("Type a phrase in English and hear it in Japanese!")

# Text input
english_text = st.text_input("Enter English phrase:")

if english_text:
    # Translate safely
    try:
        japanese_text = GoogleTranslator(source='en', target='ja').translate(english_text)
        st.success(f"Japanese Translation: {japanese_text}")

        # Generate audio
        tts = gTTS(text=japanese_text, lang='ja')
        audio_bytes = BytesIO()
        tts.write_to_fp(audio_bytes)
        audio_bytes.seek(0)
        st.audio(audio_bytes, format='audio/mp3')

    except Exception as e:
        st.error(f"Error: {e}")
import streamlit as st
from googletrans import Translator
from gtts import gTTS
import os
from io import BytesIO

# Initialize translator
translator = Translator()

st.title("🇯🇵 English → Japanese Learning App")
st.write("Type a phrase in English and hear it in Japanese!")

# Text input
english_text = st.text_input("Enter English phrase:")

if english_text:
    # Translate
    translation = translator.translate(english_text, src='en', dest='ja')
    japanese_text = translation.text
    st.success(f"Japanese Translation: {japanese_text}")

    # Generate audio
    tts = gTTS(text=japanese_text, lang='ja')
    audio_bytes = BytesIO()
    tts.write_to_fp(audio_bytes)
    audio_bytes.seek(0)
    st.audio(audio_bytes, format='audio/mp3')
import streamlit as st

st.title("こんにちは! (Hello!) Japanese Learning App")
st.write("This is your first AI language app project!")

name = st.text_input("What is your name?")
if name:
    st.success(f"Nice to meet you, {name}! Let's start learning Japanese together.")

