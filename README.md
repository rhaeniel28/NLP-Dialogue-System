# NLP Dialogue System: Local BlenderBot Interface

A full-stack AI chatbot application running locally on Windows. This project integrates the **Facebook BlenderBot-400M-Distill** model with a **Flask** backend and a responsive HTML/JS frontend.

It is capable of open-domain conversation with context awareness (short-term memory).

## Project Origin & Adaptation
This project is based on the **IBM AI Engineering Professional Certificate** lab. 

**My Contributions & Refactoring:**
* **Windows Porting:** Adapted the original Linux-based cloud environment code to run natively on **Windows 10/11** using VS Code.
* **Memory Optimization:** Implemented a **Sliding Window Memory** system (last 3 turns) to prevent token overflow and infinite memory crashes, which were present in the original lab code.
* **Error Handling:** Fixed `IndexError` crashes by enforcing `max_length` constraints during generation.
* **Front-End Integration:** Integrated the REST API with a dynamic web template.

## Tech Stack
* **Language:** Python 3.11
* **Framework:** Flask (Backend), HTML/CSS/JavaScript (Frontend)
* **AI Model:** `facebook/blenderbot-400M-distill` (via Hugging Face Transformers)
* **Machine Learning:** PyTorch (CPU)
* **Tools:** VS Code, Git

## 🛠️ Installation & Setup

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/](https://github.com/)<YOUR-USERNAME>/NLP-Dialogue-System.git
    cd NLP-DIALOGUE-SYSTEM
    ```

2.  **Create a Virtual Environment** (Recommended)
    ```powershell
    python -m venv my_env
    .\my_env\Scripts\activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install flask flask_cors transformers torch
    ```

4.  **Run the Application**
    ```bash
    python app.py
    ```

5.  **Access the Chatbot**
    Open your browser and navigate to: `http://127.0.0.1:5000`

##  How It Works
1.  **User Input:** The frontend sends a JSON POST request to the `/chatbot` endpoint.
2.  **Processing:** * The Flask server receives the prompt.
    * The `Sliding Window` logic trims the conversation history to the last 6 interactions to maintain context without overloading the model.
    * The tokenizer converts text to tensors.
3.  **Generation:** The BlenderBot model generates a response.
4.  **Response:** The server sends the text back to the frontend to be displayed in the chat bubble.


## License
This project is for educational purposes as part of the Coursera IBM AI Engineering curriculum.
