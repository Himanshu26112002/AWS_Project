import streamlit as st
from datetime import datetime
from kerykeion import AstrologicalSubject
import random

# Dictionary of horoscope messages for different signs
HOROSCOPE_MESSAGES = {
    "Ari": ["Take bold steps today, and fortune will favor you.", 
              "Your energy is contagious—use it to inspire others.", 
              "Unexpected opportunities may arise, be open to them."],
    "Tau": ["Patience is key today, trust the process.", 
               "A financial opportunity might be heading your way.", 
               "Take some time for self-care and relaxation."],
    "Gem": ["Your words have power—use them wisely.", 
               "A new connection may bring exciting possibilities.", 
               "Stay curious, learning something new will benefit you."],
    "Can": ["Trust your intuition—it will guide you well today.", 
               "Emotional balance is important; take time for yourself.", 
               "A heartfelt conversation may bring clarity to a situation."],
    "Leo": ["Your confidence will attract positive attention today.", 
            "Take the lead on an important project—it will pay off.", 
            "Someone admires your strength more than you realize."],
    "Vir": ["Attention to detail will be your greatest asset today.", 
              "A small act of kindness will go a long way.", 
              "Don't overthink—sometimes, the simplest solution is best."],
    "Lib": ["Harmony is within reach—focus on balance.", 
              "A creative spark could lead to an exciting idea.", 
              "Seek fairness in all interactions; it will serve you well."],
    "Sco": ["Embrace transformation—change will bring growth.", 
                "Your intensity can be a strength—use it wisely.", 
                "A mystery will unfold, trust that the truth will surface."],
    "Sag": ["Adventure is calling—step out of your comfort zone.", 
                    "Optimism will be your greatest asset today.", 
                    "New experiences will lead to valuable insights."],
    "Cap": ["Hard work will pay off—stay committed to your goals.", 
                  "Discipline and patience will lead to success.", 
                  "A wise decision today will benefit your future."],
    "Aqu": ["Your unique perspective will inspire those around you.", 
                 "Innovation is key—think outside the box.", 
                 "A spontaneous idea could lead to an exciting opportunity."],
    "Pis": ["Let your imagination guide you—creativity is flowing.", 
               "Your empathy will make a difference in someone's life.", 
               "Dream big, but take practical steps to make it happen."]
}

def generate_horoscope(name, birthdate, birthtime, city, country):
    # Create an instance of AstrologicalSubject
    subject = AstrologicalSubject(name, birthdate.year, birthdate.month, birthdate.day,
                                  birthtime.hour, birthtime.minute, city, country)
    
    # Convert sun sign to title case to match dictionary keys
    sun_sign = subject.sun['sign'].title()

    # Check if the sign exists in the dictionary and select a random message
    if sun_sign in HOROSCOPE_MESSAGES:
        horoscope = random.choice(HOROSCOPE_MESSAGES[sun_sign])
    else:
        horoscope = "Today is a day to embrace new opportunities."
    
    # Customize the message
    final_horoscope = f"Hello {name}! As a {sun_sign}, {horoscope}"
    return sun_sign, final_horoscope

# Streamlit UI
st.title("AI Horoscope Generator")

# Create a form for user input
with st.form(key='horoscope_form'):
    name = st.text_input("Enter your name:")
    birthdate = st.date_input("Enter your birthdate:")
    birthtime = st.time_input("Enter your birth time:")
    city = st.text_input("Enter your birth city:")
    country = st.text_input("Enter your birth country:")
    
    # Submit button
    submit_button = st.form_submit_button(label='Submit')

# Process the form data after submission
if submit_button:
    if name and birthdate and birthtime and city and country:
        sign, horoscope = generate_horoscope(name, birthdate, birthtime, city, country)
        st.subheader(f"Your Horoscope ({sign})")
        st.write(horoscope)
    else:
        st.error("Please fill in all the fields.")
