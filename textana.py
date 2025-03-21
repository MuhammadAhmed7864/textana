import streamlit as st
import re

def main():
    st.set_page_config(page_title="Text analyzer",page_icon="🖹",layout="centerd")

    st.markdown("""
        <style>
                .main{ background-color: #ebecda;}
                .stTextArea, .stTextInput{ border-radius: 10px;}
                .stButton>button { background-color: blue; color: white; border-radius: 10px; padding: 10px}
        </style>        
    
    """, unsafe_allow_html=True)

    st.title("Text Analyzer In phyton")
    st.write("Analyze your text quickly and efficent.")

    paragraph = st.text_area("✍🏽 Enter a paragraph: ", "",height=150)

    if paragraph:
        st.markdown("---")
        st.subheader("📌Analyzing Result")


        words = paragraph.split()
        words_count = len(words)
        char_count = len(paragraph)
        col1, col2 = st.columns(2)
        col1.metric("📋 Total words", words_count)
        col2.metric("Total character", char_count)
        
            #search and replace
        st.subheader("🔍Search and replace")
        search_word = st.text_input("Enter a word to search:")
        replace_word = st.text_input()
        
        if search_word and replace_word:
            modified_paragraph = re.sub(rf'/b{re.escape(search_word)}/b', replace_word, paragraph)
            st.success("Modified paragraph:")
            st.info(modified_paragraph)

            #uppercase and lowecase
            st.subheader("🌟Uppercase and lowercase Feature")
            st.text_area("UPPERCASE:" , paragraph.upper(), height=150)
            st.text_area("LOWERCASE:", paragraph.lower(), height=150)

            ope_phyton = "phyton" in paragraph
            st.write(f"✔️ Contain 'phyton': {ope_phyton}")

        
            #average length of paragraph:
            average_word_length = char_count / words_count if words_count else 0
            st.write(f"Average word Length:{average_word_length:2f}")

        else:
            st.warning(" ☢️ Please enter a paragraph for analyzing")
    if __name__ == "_main_":
        main()
