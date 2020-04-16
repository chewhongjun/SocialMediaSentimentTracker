import streamlit as st

#NLP pkgs
import spacy
from textblob import TextBlob
from gensim.summarization import summarize

#Sumy Pkg
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

def text_analyzer(my_text):
    nlp = spacy.load('en')
    docx = nlp(my_text)

    # tokens = [tokens.text for token in docx]
    allData = [('"Tokens":{},\n"Lemma":{}'.format(token.text,token.lemma_)) for token in docx]
    return allData

def entity_analyzer(my_text):
    nlp = spacy.load('en')
    docx = nlp(my_text)

    tokens = [token.text for token in docx]
    entities = [(entity.text,entity.label_) for entity in docx.ents]
    allData = ['"Tokens":{},\n"Entities:{}'.format(tokens,entities)]
    return allData
def sumy_summerizer(docs):
    parser = PlaintextParser.from_string(docs,Tokenizer("english"))
    lex_summarizer = LexRankSummarizer()
    
    summary = lex_summarizer(parser.document,3)
    summary_list = [str(sentence) for sentence in summary]
    result = ' '.join(summary_list)
    return result



def main():
    st.title("NLP Web Application")
    st.subheader("NLP on the go")

    #Tokenization
    if(st.checkbox("Show Tokenms and Lemma")):
        st.subheader("Tokenize Your Text")
        message = st.text_area("Enter you Text", "Type Here")
        if(st.button("Analyze")):
            nlp_result = text_analyzer(message)
            st.json(nlp_result)
    
    #Named Entities
    if(st.checkbox("Show named entities")):
        st.subheader("Extract Entities from your text")
        message = st.text_area("Enter you Text", "Type Here")
        if(st.button("Extract")):
            entity_result = entity_analyzer(message)
            st.json(entity_result)

    #Sentiment Analysis
    if(st.checkbox("Show Sentiment Analysis")):
        st.subheader("Sentiment of your text")
        message = st.text_area("Enter you Text", "Type Here")
        if(st.button("Analyse")):
            blob =TextBlob(message)
            result_sentiment = blob.sentiment
            st.success(result_sentiment)
    
    #Text summarization
    if(st.checkbox("Show Text summarization")):
        st.subheader("summarization of your text")
        message = st.text_area("Enter you Text", "Type Here")
        summary_options = st.selectbox("Choice of you Summerizer",("gensim","sumy"))
        if(st.button("Summarize")):
            if summary_options=='gensim':
                summary_result =summarize(message)
            else:
                summary_result = sumy_summerizer(message)

        st.success(summary_result)




if __name__ == '__main__':
    main()
    