from google import genai 
import os
from config import MAIN_PROXY, GEMINI_API, gemini_model

os.environ['http_proxy'] = 'http://' + MAIN_PROXY
os.environ['https_proxy'] = 'http://' + MAIN_PROXY
os.environ['all_proxy'] = 'socks5://' + MAIN_PROXY

client = genai.Client(api_key=GEMINI_API)

chat_data = {}

def get_chat(userID):
    if userID not in chat_data:
        chat_data[userID] = client.chats.create(model=gemini_model)
    return chat_data[userID]    

def chat_response(question,userID):
    chat = get_chat(userID)
    print('new req', question)
    response = chat.send_message(question)
    #     model = gemini_model,
    #     contents=question
    # )
    return response.text