from transformers import pipeline
from transformers import Conversation

chatbot = pipeline(task="conversational", model="facebook/blenderbot-400M-distill")


def get_response(user_message):
    conversation = Conversation(user_message)
    response_text = chatbot(conversation)
    return response_text.generated_responses[-1]
