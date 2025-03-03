import requests
import streamlit as st

st.title("😂 Random Bad Joke Generator")

# Fetch a random joke from API
def get_joke():
    joke = requests.get('https://official-joke-api.appspot.com/random_joke').json()
    return joke['setup'], joke['punchline']

if st.button("Get a Joke!"):
    setup, punchline = get_joke()
    st.write(f"**{setup}**")
    st.success(punchline)
