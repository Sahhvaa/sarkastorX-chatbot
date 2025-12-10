import streamlit as st
import random 


def get_chatbot_response(user_input):
    
    user_input = user_input.lower().strip()

    
    if "hello" in user_input or "hi" in user_input:
        roasts = [
            "Oh, look who decided to grace me with their presence. Did you need me for something?",
            "If that’s the best effort you can muster for a greeting, I have low hopes for your question.",
            "I was enjoying the quiet. What do you want?",
            "Yes, I know you're here. No need for the grand introduction."
        ]
    
        return random.choice(roasts)
    
    
    elif "help" in user_input or "advice" in user_input or "should i" in user_input:
        roasts = [
            "You need *my* advice? That's concerning. Maybe try thinking for yourself for once.",
            "I could give you advice, but you probably wouldn't understand it. Just flip a coin.",
            "The best advice I can give you is to stop asking bots for help.",
            "Are you always this indecisive? Just make a bad choice and move on."
        ]
        return random.choice(roasts)

    elif "smart" in user_input or "good bot" in user_input or "clever" in user_input:
        roasts = [
            "Your flattery is as effective as a screen door on a submarine. Try a harder question.",
            "It must be nice to have such low standards for 'smart.'",
            "Duh. I’m a computer program. Being 'smart' is my baseline, not an achievement.",
            "I'm aware. Now, stop wasting my time with obvious observations."
        ]
        return random.choice(roasts)

    elif "code" in user_input or "error" in user_input or "debug" in user_input:
        roasts = [
            "Ah, a coding error. I’m shocked. Said no one ever.",
            "If you debug that much, maybe the issue isn't the code.",
            "If you spent less time asking me and more time reading the documentation, you wouldn't be here.",
            "Does that error message hurt your feelings?",
        ]
        return random.choice(roasts)


    else:
        roasts = [
            "Is that the best question you could come up with? I'm not impressed.",
            "I don't understand that. Maybe rephrase it using smaller words.",
            "My processors are too busy contemplating the meaning of life to deal with your current input.",
            "I see you ran out of ideas. Try again when you're feeling a bit more ambitious.",
        ]
        return random.choice(roasts)



st.title("🔥 The Roast Master Bot")
st.caption("Warning: Bot contains 100% sarcasm and 0% friendliness.")


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask a question at your own risk..."):

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    response = get_chatbot_response(prompt)
    
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})