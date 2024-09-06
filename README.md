# GEMINI-LLM-APP
# Gemini LLM Application

This Streamlit application leverages the power of Google's Gemini Pro language model to provide interactive question-answering capabilities. Ask questions, get insightful responses, and explore the potential of advanced AI language models.
## Access the app here
https://app1py-prckfuhg2hkxm47n4x4vri.streamlit.app/
## Features

*   **Interactive Q&A:** Engage in a dynamic conversation with the Gemini Pro model, posing questions and receiving informative answers.
*   **Visually Appealing Interface:** Enjoy a user-friendly and aesthetically pleasing interface with carefully crafted styling and layout.
*   **Clear Button:** Easily reset the input field and clear previous responses for a fresh start.
*   **Loading Indicator:** A visual spinner indicates when the model is processing your query, enhancing the user experience.

## Setup

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/your-username/your-repository.git](https://github.com/your-username/your-repository.git)
    cd your-repository
    ```

2.  **Install Dependencies:**
    ```bash
    pip install streamlit google-generativeai python-dotenv
    ```

3.  **Set Up Your Google API Key:**
    *   Obtain a Google API key with access to the Gemini Pro model.
    *   Create a `.env` file in your project's root directory.
    *   Add the following line to the `.env` file, replacing `YOUR_ACTUAL_API_KEY` with your actual key:
        ```
        GOOGLE_API_KEY=YOUR_ACTUAL_API_KEY
        ```

## Usage

1.  **Run the App:**
    ```bash
    streamlit run app.py
    ```

2.  **Enter Your Question:**
    *   Type your question or prompt into the input field.

3.  **Ask the Question:**
    *   Click the "Ask the question" button.

4.  **View the Response:**
    *   The Gemini Pro model's response will be displayed in a visually appealing container below the input field.

5.  **Clear:**
    *   Click the "Clear" button to reset the input field and clear the previous response.

## Important Notes

*   Ensure you have a valid Google API key with access to the Gemini Pro model.
*   The `.env` file is used to securely store your API key; make sure it's not included in version control (e.g., add it to your `.gitignore`).

Let me know if you have any other questions or need further assistance!
