import streamlit as st

from sumy.parsers.plaintext import PlaintextParser #pass text through parser
from sumy.nlp.tokenizers import Tokenizer          #cuuting the words
from sumy.summarizers.lsa import LsaSummarizer #latent semantic analysis
from sumy.summarizers.luhn import LuhnSummarizer #based on word frequency
from sumy.summarizers.lex_rank import LexRankSummarizer #graph based approach
from sumy.summarizers.text_rank import TextRankSummarizer #sentence selection

st.title('Text Summarization App')

text = st.text_area("Please Enter the text to Summarize...")

summarizer_type = st.selectbox("Choose Summarizer Type", ('LSA', 'LUHN', 'LexRank', 'TextRank'))
sentence_count = st.slider("NO. Sentences", 1, 20)

def summarize_text(text, summarizer_type = 'LSA', sentence_count = 5):
    parser = PlaintextParser.from_string(text, Tokenizer('english'))
    
    if summarizer_type == 'LSA':
        summarizer = LsaSummarizer()
    elif summarizer_type == 'LUHN':
        summarizer = LuhnSummarizer()
    elif summarizer_type == 'LexRank':
        summarizer = LexRankSummarizer()
    elif summarizer_type == 'TextRank':
        summarizer = TextRankSummarizer()
        
    summary = summarizer(parser.document, sentence_count)
    return " ".join(str(sentence) for sentence in summary) 

if st.button('Summarize Text'):
    if text:
        summary = summarize_text(text, summarizer_type, sentence_count)
        st.subheader('Summary')
        st.write(summary)
    else:
        st.write('Please Write a Text To Summarize')
