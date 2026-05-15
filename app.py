import gradio as gr
import google.generativeai as genai

genai.configure(api_key="AIzaSyCUhiLOdvVKozrOenAY5pmHqLGe_PeuGTI")

def chat_with_gemini(message, history):
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")

        response = model.generate_content(message)
        
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# 3. Create the UI
demo = gr.ChatInterface(
    fn=chat_with_gemini, 
    title="Gemini Chatbot",
    description="Ask me anything | Best if you ask me only about stuff that are related to School.",
    examples=["What is Python?", "Tell me a brief information of HTML.", "What is CSS?"]
)

if __name__ == "__main__":
    demo.launch(theme="ocean")