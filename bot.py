#importing relevant libraries
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import nltk

# Creating ChatBot Instance
chatbot = ChatBot(name="Redeemer's University Help Chat Bot",
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
                  logic_adapters=[
                      'chatterbot.logic.MathematicalEvaluation',
                      'chatterbot.logic.TimeLogicAdapter',
                      'chatterbot.logic.BestMatch',
                      {
                        'import_path': 'chatterbot.logic.BestMatch',
                        'default_response': 'I am sorry, but I do not understand. I am still learning.',
                        'maximum_similarity_threshold': 0.90
                        }
                  ],
                  database_uri='sqlite:///db.sqlite3')

# Training with Questions
trainer = ListTrainer(chatbot)
training_data =open('Chatbot\data\questions.txt').read().splitlines()
trainer.train(training_data)

# Training with English Corpus Data
trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train(
    'chatterbot.corpus.english'
)