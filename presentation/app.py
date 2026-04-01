import streamlit as st
from audiorecorder import audiorecorder


st.markdown("""
    <style>
        .stButton > button {
            background-color: #D30000;
            color: white;
            border: none;
        }
    </style>
""", unsafe_allow_html=True)

st.title("New Meeting")
st.caption("Fill in the details and let AI handle the rest.")


st.write("##### Meeting Info")


title = st.text_input("Meeting Title", placeholder="e.g. Sprint Review -- Week 12")

col1, col2 = st.columns(2)
    
with col1:
    date = st.date_input("Date")
    organizer = st.text_input("Organizer", placeholder="Organizer's Name")
    attendees = st.text_area("Attendees", placeholder="Add Names Or Emails, Comma Seperated")
    
with col2:
    time = st.time_input("Time")
    location = st.text_input("Location or Platform", placeholder="e.g  Teams Call, Conference Room...")
    agenda = st.text_area("Agenda", placeholder="What's On The Table Today ?")


st.write("##### Discussion Notes")

notes = st.text_area("Bullet Points", placeholder="Write down key points, decisions, blockers, anything discussed...")



st.write("##### Audio Input")

col3, col4 = st.columns(2)

with col3:
    uploaded_file = st.file_uploader("Upload Recording", type=["mp3", "wav", "m4a"])
    

with col4:
    recorded_audio = st.audio_input("Record Audio")
    
    
generate = st.button("Generate MoM", use_container_width=True)