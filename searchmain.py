import requests
import streamlit as st

from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("NYTIMES_API_KEY")
API_GUARDIAN_KEY = os.getenv("GUARDIAN_API_KEY")
API_BASE_URL = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
API_GUARDIAN_BASE_URL = "https://content.guardianapis.com/search"





def search_articles(search_term):
    params_ny = {
        "q": search_term,
        "api-key": API_KEY
    }
    params_guardian = {
        "q": search_term,
        "api-key": API_GUARDIAN_KEY,
        "show-fields": "trailText"
    }

    response = requests.get(API_BASE_URL, params_ny)
    response_guardian = requests.get(API_GUARDIAN_BASE_URL, params_guardian)
    

    return {
        "nytimes": response.json(),
        "guardian": response_guardian.json()
    }



def display_nytimes_results(search_results):
    docs = search_results["response"]["docs"]

    count = 1
    for doc in docs:
        article_web_url = doc["web_url"]
        article_headline = doc["headline"]["main"]
        article_summary = doc.get("snippet", "No summary available.")
        with st.expander(f"{count}. {article_headline}"):
            st.markdown(str(count)+ ". " + article_headline + " (" + article_web_url + " )")
            st.write(article_summary)
        count = count + 1

def display_guardian_results(guardian_results):
    docs = guardian_results["response"]["results"]


    count = 1
    for doc in docs:
        article_web_url = doc["webUrl"]
        article_headline = doc["webTitle"]
        article_summary = doc.get("fields", {}).get("trailText", "No summary available.")
        with st.expander(f"{count}. {article_headline}"):
            st.markdown(str(count)+". " + article_headline + " (" + article_web_url + " )")
            st.write(article_summary)
        count = count + 1



#------------------ GUI ------------------ 

st.title("Bajillion Search Engine")
st.write("Search for articles from NYTimes and The Guardian")
st.write("Type a keyword and press Search to see article headlines and summaries.")
st.write("") 

search_term = st.text_input("Your search term: ")

if st.button("Search") and search_term.strip() !="":
    search_results = search_articles(search_term)

    st.subheader("NYTimes Results")
    display_nytimes_results(search_results["nytimes"])

    st.subheader("The Guardian Results")
    display_guardian_results(search_results["guardian"])
