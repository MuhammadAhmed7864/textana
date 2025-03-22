import streamlit as st
import re

def main():
    st.set_page_config(page_title="Text Analyzer", page_icon="🖹", layout="centered")

    st.markdown("""
        <style>
                .stTextArea, .stTextInput { border-radius: 10px; }
                .stButton>button { background-color: blue; color: white; border-radius: 10px; padding: 10px }
        </style>        
    """, unsafe_allow_html=True)

    st.title("Text Analyzer In Python")
    st.write("Analyze your text quickly and efficiently.")

    paragraph = st.text_area("✍🏽 Enter a paragraph: ", "", height=150)

    if paragraph:
        st.markdown("---")
        st.subheader("📌 Analyzing Result")

        words = paragraph.split()
        words_count = len(words)
        char_count = len(paragraph)

        col1, col2 = st.columns(2)
        col1.metric("📋 Total words", words_count)
        col2.metric("📏 Total characters", char_count)

        # Search and replace
        st.subheader("🔍 Search and Replace")
        search_word = st.text_input("Enter a word to search:")
        replace_word = st.text_input("Enter a word to replace with:")

        if search_word and replace_word:
            modified_paragraph = re.sub(rf'\b{re.escape(search_word)}\b', replace_word, paragraph)
            st.success("Modified paragraph:")
            st.info(modified_paragraph)

        # Uppercase and Lowercase
        st.subheader("🌟 Uppercase and Lowercase Feature")
        st.text_area("UPPERCASE:", paragraph.upper(), height=150)
        st.text_area("LOWERCASE:", paragraph.lower(), height=150)

        # Check if "Python" is in the text
        contains_python = "Python" in paragraph
        st.write(f"✔️ Contains 'Python': {contains_python}")

        # Average word length
        average_word_length = char_count / words_count if words_count else 0
        st.write(f"📊 Average word length: {average_word_length:.2f}")

    else:
        st.warning(" ☢️ Please enter a paragraph for analysis.")

if __name__ == "__main__":
    main()
