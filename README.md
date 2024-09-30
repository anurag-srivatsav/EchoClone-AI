

# EchoClone AI

EchoClone AI is an intelligent voice assistant built with Streamlit, Google Generative AI, and custom text-to-speech (TTS) technology. It delivers real-time, interactive responses in a unique voice, creating an immersive conversational experience.

<img src="https://rampd.co/wp-content/uploads/2023/09/image-15-1024x1000.png" alt="EchoClone AI Screenshot" width="300" height="300">

[LiveDemo](https://echoclone-ai.streamlit.app/)

## Features

- **Voice Interaction**: Generates responses using Google Generative AI and delivers them in a custom voice via TTS.
- **Personalized Conversations**: Provides engaging, intelligent, and concise replies to user queries.
- **Custom TTS Integration**: Utilizes Play.ht for creating a unique voice profile.
- **Interactive Interface**: User-friendly interface built with Streamlit for a seamless experience.
- **API Integration**: Integrated with the Gemini API for generating accurate and relevant responses.
- **Portfolio Integration**: Includes a button that redirects users to explore the creator's personal portfolio bot.

## Installation

To run EchoClone AI locally, follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/anurag-srivatsav/EchoCloneAI.git
    cd EchoCloneAI
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up Environment Variables**:
    Create a `.env` file in the root directory and add your Google Generative AI and Play.ht API keys:
    ```plaintext
    GENAI_API_KEY=your_google_api_key
    PLAYHT_API_KEY=your_playht_api_key
    ```

4. **Run the Application**:
    ```bash
    streamlit run app.py
    ```

## Usage

Once the application is running, a Streamlit server will provide a local URL (e.g., `http://localhost:8501`). Open this URL in your browser to interact with EchoClone AI. Type your query, and the assistant will respond with both text and voice output.

## Project Structure

- `app.py`: Main application file.
- `requirements.txt`: List of required Python libraries.
- `assets/`: Contains static assets like images.
- `.env`: Contains API keys and environment variables.
  
## Example Interaction

![Example Interaction](https://res.cloudinary.com/dvlgixtg8/image/upload/v1727680282/echocloneai.jpg)

## Contributing

Contributions are welcome! If you have ideas for improvements or new features, feel free to submit a pull request or open an issue.

## Contact

For questions or suggestions, contact [Anurag Srivatsav](mailto:anuragsrivatsav4@gmail.com).

---

You can modify this README further based on your specific requirements!
