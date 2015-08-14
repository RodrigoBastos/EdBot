__author__ = 'rodrigo'

from chatterbot import ChatBot

chatbot = ChatBot("Ron Obvious")

conversation = [
  "Hello",
  "Hi there!",
  "How are you doing?",
  "I'm doing great.",
  "That is good to hear",
  "Thank you.",
  "Your welcome."
]

chatbot.train(conversation)

response = chatbot.get_response("Thank you.")
print(response)