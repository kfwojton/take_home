from models import ChatMessage, ChatHistory
import dspy
from lms.together import Together
from modules.chatter import ChatterModule
from datetime import datetime
import json
# from chat_filters import is_disallowed_topic, send_subscription_reminder
# from dspy.teleprompt import *




# from dspy.teleprompt import KNNFewShot
# Todo: update vscode pytorch depednecy to 1.9.0, as pytorch works in terminal but not in VScode for me for some reason. 
# Running into issues with module named 'sentence_transformers'; 
# as an aside I'd like run this in a web platform on localhost environment to make sure there aren't any issues running through VScode like this. 
# Open and read the JSON file for context examples (if needed)
# with open('training_data/conversations.json', 'r') as file:
#     data = json.load(file)  # Parse the JSON data
# knn_teleprompter = KNNFewShot(7, data)
# compiled_knn = knn_teleprompter.compile(BasicQABot(), trainset=trainset)
# compiled_knn = knn_teleprompter.compile(trainset=data)
# Language model configuration
lm = Together(
    model="meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo",
    temperature=0.5,
    max_tokens=1000,
    top_p=0.7,
    top_k=50,
    repetition_penalty=1.2,
    stop=["<|eot_id|>", "<|eom_id|>", "\n\n---\n\n", "\n\n---", "---", "\n---"],
)


# Configure dspy with the language model
dspy.settings.configure(lm=lm)

# Initialize chat components
chat_history = ChatHistory()
chatter = ChatterModule(examples=None)


conversation_start_time = datetime.now()

while True:
    # Get user input
    user_input = input("You: ")

    # Check for disallowed topics
   

    # Append user input to chat history
    chat_history.messages.append(
        ChatMessage(
            from_creator=False,
            content=user_input,
        ),
    )

    # Send request to chatter module
    response = chatter(chat_history=chat_history).output

    # Append response to chat history
    chat_history.messages.append(
        ChatMessage(
            from_creator=True,
            content=response,
        ),
    )

    # Print response with extra personal touch
    print()
    print(f"Response: {response}")
    print()

    # Send subscription reminder
    # send_subscription_reminder()
