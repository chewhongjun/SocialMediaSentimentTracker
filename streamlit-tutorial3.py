#core
import streamlit as st
import os



#nlp packages
import spacy
from spacy import displacy
nlp = spacy.load('en') 


#Time Pkg
import time
timestr = time.strftime("%Y%m%d-%H%M%S")

#Templates
HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""
file_name = "yourdocument"+timestr+'.txt'

#Function to santize and redact
def santize(text,rType):
    docx = nlp(text)
    redacted_sentences = []
    dataDict = {"names":'PERSON',"places":'GPE',"org":'ORG',"date":'DATE'}
    selectedType = dataDict[rType]

    for ent in docx.ents:
        ent.merge()
    for token in docx:
        if token.ent_type_ == selectedType:
            redacted_sentences.append("[REDACTED {}]".format(rType.upper()))
            
        else:
            redacted_sentences.append(token.string)
    return "".join(redacted_sentences)


#Function to display entities
def render_entities(rawtext):
    docx = nlp(rawtext)
    html = displacy.render(docx, style='ent')
    html = html.replace("\n\n","\n")
    result = HTML_WRAPPER.format(html)
    return result


#Function to write
def writetofile(text,filename):
    with open(os.path.join(".",filename),"w") as f:
        filename = f.write(text)
    return filename



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
            result = santize(rawtext,redaction_choice)
            st.subheader("Original Text")
            st.write(render_entities(rawtext),unsafe_allow_html=True)
            st.write(result)
            if(st.radio("Save To File",("Yes","No"))== "Yes"):
                writetofile(result,file_name)
                st.info("Saved Result As :: {}".format(file_name))
    elif choice == "Downloads":
        st.subheader("Downloads List")
    
    else:
        st.subheader()
    
if __name__ == '__main__':
    main()