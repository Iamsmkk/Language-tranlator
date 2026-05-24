import streamlit as st
from deep_translator import GoogleTranslator

st.title("Language Translation Tool")

st.write("Translate text from one language to another.")

languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja",
    "Marathi": "mr"
}

text = st.text_area("Enter Text")

source = st.selectbox(
    "Source Language",
    list(languages.keys())
)

target = st.selectbox(
    "Target Language",
    list(languages.keys()),
    index=1
)

if st.button("Translate"):

    if text != "":

        translated = GoogleTranslator(
            source=languages[source],
            target=languages[target]
        ).translate(text)

        st.subheader("Translated Text")

        st.write(translated)

    else:
        st.warning("Please enter some text.")