# 🔥 SarkastorX: The Roast Master Chatbot

This project is a functional, rule-based chatbot designed purely for sarcastic roasting and condescending replies.

## 🚀 Setup and Running Instructions

### Prerequisites

* Python 3.8+
* The `streamlit` library

### Local Setup

1.  **Clone the Repository:**
    ```bash
    git clone [YOUR GITHUB REPO LINK HERE]
    cd sarkastorX-chatbot
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Web Interface:**
    ```bash
    streamlit run app.py
    ```
4.  The application will open in your web browser, ready to roast you!

## 💡 Approach and Uniqueness

* **Approach:** This chatbot uses a **Rule-Based System with Custom Responses**. We did **not** use an external generative AI API (like Gemini or GPT).
* **How it Works:** The core Python function (`get_chatbot_response`) uses `if/elif` statements to detect specific **keywords** (e.g., "hello," "smart," "error") in the user's input. For each rule, the bot selects a **random** sarcastic reply from a dedicated list (`random.choice()`) to ensure the conversation is not repetitive.
* **Uniqueness:** The entire persona is built on **sarcasm**. The goal was to demonstrate creative use of basic logic and string manipulation to create an engaging, opinionated, and intentionally unhelpful personality.

## 🚧 Challenges and Solutions

* **Challenge:** Making the responses feel dynamic and not repetitive, even with limited rules.
* **Solution:** We overcame this by expanding the lists of roasts for each rule trigger, ensuring that `random.choice()` always had several options.

## 🎥 Demo

[https://screenrec.com/share/bc7K9yt2Y5]
