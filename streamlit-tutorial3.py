#core
import streamlit as st
import os

#nlp packages
import spacy
from spacy import displacy
nlp = spacy.load('en') 



#Function to santize and redact
def santize_names(text):
    docx = nlp(text)
    redacted_sentences = []
    for ent in docx.ents:
        ent.merge()
    for token in docx:
        st.write(token.ent_type)
        if token.ent_type == 'PERSON':
            redacted_sentences.append("[REDACTED NAME]")
            
        else:
            redacted_sentences.append(token.string)
    return "".join(redacted_sentences)


def main():
    """Document redactor application"""

    st.title("Document Redactor Application")
    st.text("Build with streamlit and SpaCy")

    activities = ["Redactor","Downloads","About"]

    choice = st.sidebar.selectbox("Select Task",activities)

    if choice == "Redactor":
        st.subheader("Redactor of terms")
        rawtext = st.text_area("Enter Text", "Type Here")
        redaction_item = ["names","places","org","date"]
        redaction_choice = st.selectbox("Select term to redact",redaction_item)
        save_option = st.radio("Save to file", ("Yes","No"))

        if st.button("submit"):
            result = santize_names(rawtext)
            st.write(result)

    elif choice == "Downloads":
        st.subheader("Downloads List")
    
    else:
        st.subheader()
    
if __name__ == '__main__':
    main()