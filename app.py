import requests
import streamlit as st
import base64
import webbrowser
# Define the API endpoint
API_URL = "http://127.0.0.1:8000/transcribe"  # Update with the correct URL

# Streamlit UI
st.title("Audio Transcription")

# Function to transcribe audio
def transcribe_audio(audio_file):
    # Determine the content type based on file extension
    content_type = "audio/wav" if audio_file.name.endswith('.wav') else "audio/mp3"

    # Prepare the audio file as multipart/form-data
    files = {"audio": (audio_file.name, audio_file.read(), content_type)}

    # Make the POST request to the API
    response = requests.post(API_URL, files=files)

    # Check if the request was successful
    if response.status_code == 200:
        # Provide the MIDI data for download
        midi_data = response.content
        b64_midi = base64.b64encode(midi_data).decode('utf-8')
        href = f'<a href="data:audio/midi;base64,{b64_midi}" download="transcribed_audio.mid">Download MIDI</a>'
        st.markdown(href, unsafe_allow_html=True)
        st.success("Transcription successful.")
    else:
        st.error("Transcription failed.")

# Streamlit file uploader
uploaded_file = st.file_uploader("Upload an audio file (.wav or .mp3)", type=["wav", "mp3"])

if uploaded_file is not None:
    st.write("File uploaded successfully!")
    st.audio(uploaded_file)
    if st.button("Transcribe"):
        transcribe_audio(uploaded_file)

def open_google_drive_link():
    google_drive_link = "https://google.com"  # Replace with your Google Drive link
    webbrowser.open_new_tab(google_drive_link)
st.write('Download fuwalo android app')
if st.button("Download App"):
    open_google_drive_link()
# FAQ data
faqs = [
    {"question": "How do I convert audio to MIDI using Fuwallo? 🤔", "answer": "Fuwallo provides a simple and intuitive interface for converting audio to MIDI. Simply upload your audio file to the platform, choose your desired settings, and Fuwallo will handle the rest."},
    {"question": "Is my data secure when using Fuwallo to convert audio files? 🤨", "answer": "Yes, Fuwallo takes data security seriously. We use industry-standard encryption protocols to ensure that your audio files and personal information remain secure throughout the conversion process."},
    {"question": "What audio file formats are supported by Fuwallo for conversion to MIDI? 🎧", "answer": "Fuwallo supports a wide range of audio file formats, including MP3, WAV, AIFF, and more. If you're unsure whether your file format is supported, feel free to reach out to our support team for assistance."},
    {"question": "Can I customize the output MIDI files generated by Fuwallo? 🎶", "answer": "Yes, Fuwallo provides options for customizing the output MIDI files to suit your needs. You can adjust parameters such as note sensitivity, tempo mapping, and instrument assignment to achieve the desired result."},
    {"question": "How accurate are the MIDI conversions performed by Fuwallo? 🎵", "answer": "Fuwallo strives to provide accurate and high-quality MIDI conversions. While the accuracy may vary depending on factors such as the complexity of the audio file and the settings chosen, our team is continuously working to improve the conversion algorithms."},
    
]
# Display FAQ questions and answers
st.title("FAQs")

for faq in faqs:
    with st.expander(faq["question"]):
        st.write(faq["answer"])
