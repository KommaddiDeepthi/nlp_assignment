import streamlit as st
import language_tool_python
from spellchecker import SpellChecker
tool = language_tool_python.LanguageTool('en-US')
spell = SpellChecker()
def correct_spelling(text):
    words = text.split()
    corrected_words = [spell.correction(word) if spell.correction(word) else word for word in words]
    return ' '.join(corrected_words)
def correct_grammar(text):
    matches = tool.check(text)
    return language_tool_python.utils.correct(text, matches)
st.title("🔤 Spelling & Grammar Correction Tool")
user_input = st.text_area("Enter text:", "This is an amazng tol for corecting gramar mistaks.")

if st.button("Correct Text"):
    corrected_spelling = correct_spelling(user_input)
    corrected_text = correct_grammar(corrected_spelling)
    st.subheader("✅ Corrected Text:")
    st.write(corrected_text)
