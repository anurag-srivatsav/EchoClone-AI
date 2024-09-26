import os
import streamlit as st
import google.generativeai as genai
from google.generativeai import configure, GenerativeModel
from pyht import Client
from pyht.client import TTSOptions

# Set your API key as an environment variable
os.environ['GENAI_API_KEY'] = 'AIzaSyDzeATPLWRenJGapH8wOCtKEs_QFf6FPR0'  # Replace with your actual API key

# Configure the SDK with the API key
api_key = os.getenv('GENAI_API_KEY')
configure(api_key=api_key)

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 30,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

# Streamlit app
st.title("EchoClone AI: Experience My Unique Voice Assistant")


# Add a sidebar
st.sidebar.header("About the AI VoiceAssist 🤖")

# Display the image with the custom style
st.sidebar.markdown(
    '<img src="https://rampd.co/wp-content/uploads/2023/09/image-15-1024x1000.png" class="styled-image" alt="EchoClone AI">',
    unsafe_allow_html=True
)# Update with your image path
st.sidebar.markdown("""
This AI-powered chatbot utilizes Google's Generative AI and custom TTS to deliver intelligent responses with natural-sounding voice output.
""")


st.markdown(
    """
    <style>
    .styled-image {
        border-radius: 15px; /* Adjust the radius as needed */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Add shadow */
        width: 100%; /* Make the image responsive */
    }
    </style>
    """,
    unsafe_allow_html=True
)



# Add some line breaks for spacing
st.sidebar.markdown("<br><br>", unsafe_allow_html=True)

# Display the text below the image
st.sidebar.markdown("**EchoClone AI**<br>created by - Anurag Srivastav", unsafe_allow_html=True)

url = 'https://anuragsportfolioassist.streamlit.app/'  # Replace with your desired URL

st.markdown(
    """
    <style>
    .styled-text {
        font-size: 18px; /* Change font size */
        color: skyblue; /* Change text color */
        font-weight: bold; /* Make the text bold */
        
        margin-bottom: 20px; /* Add space below */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Use markdown to display the styled text in the sidebar
st.sidebar.markdown('<p class="styled-text">Wanna explore my personal portfolio bot? Check it out now!</p>', unsafe_allow_html=True)
# Adding a button to redirect to another URL
if st.sidebar.button('portfolioAssist🤖'):
    st.sidebar.markdown(f'You are being redirected to: [{url}]({url})', unsafe_allow_html=True)
    # Redirect using Streamlit's write function with HTML link and target="_blank"
    st.sidebar.write(f'<meta http-equiv="refresh" content="0;URL={url}" target="_blank">', unsafe_allow_html=True)

# Initialize chat history in session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for user_msg, bot_msg in st.session_state.chat_history:
    st.markdown(f"**You:** {user_msg}")
    st.markdown(f"**AI:** {bot_msg}")
    # if output_file:
    #     st.audio(output_file)

# User input
input_query = st.text_input("Enter your query:", "")

if st.button("Submit"):
    if input_query:
        # Show loading spinner
        with st.spinner("Generating response..."):
            # Start chat session and get response
            chat_session = model.start_chat(history=[])
            response = chat_session.send_message(input_query)
            Query_Response = response.text

            # Store the conversation in chat history
            st.session_state.chat_history.append((input_query, Query_Response))

            # Initialize the TTS client
            client = Client(
                # user_id="e6BvPrP9VGaGCHKY7io5o0KpKFr1",
                # api_key="075e90e1e50049f09e5921962a24cda1"
                user_id="qotPLKt4h0WV1fLPmFHa75aYNpw2",
                api_key="b43eab925d5e485999c0657f97907b7e"
            )

            # Define the voice URL
            # voice_url = "s3://voice-cloning-zero-shot/71843e74-2087-4c61-855e-8e0ff1b03ef8/anurag/manifest.json"
            voice_url="s3://voice-cloning-zero-shot/f41772f2-66d6-4127-a733-f2d621273740/original/manifest.json"
            # Replace with a valid voice URL or ID

            # Create TTS options
            tts_options = TTSOptions(voice=voice_url)

            # Save the audio to a file
            output_file = "output_audio.wav"
            with open(output_file, "wb") as audio_file:
                try:
                    for chunk in client.tts(Query_Response, options=tts_options):
                        audio_file.write(chunk)
                except Exception as e:
                    st.error(f"An error occurred during TTS: {e}")

            # Play the audio in Streamlit
            st.audio(output_file)
    else:  
        st.warning("Please enter a query.")



# Markdown with HTML for footer
st.markdown("""
<hr style="border-top: 3px solid #bbb;">
<div style="text-align:center;">
    <p>&copy; 2024 Anurag Srivatsav. All rights reserved.</p>
    <p>Developed with ❤️ using Streamlit</p>
    <p>Connect with me on LinkedIn: <a href="https://linkedin.com/in/anuragsrivatsav" target="_blank">Anurag Srivatsav</a></p>
</div>
""", unsafe_allow_html=True)
