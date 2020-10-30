#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 13:03:13 2020

@author: antoniofoglia
"""
from chatterbot import ChatBot
from __output__ import say
from chatterbot.trainers import ListTrainer


bot = ChatBot('Goffredo',logic_adapters=[
        'chatterbot.logic.UnitConversion',
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.UnitConversion'
])

conversation = [
    "Hello",
    "Hi there!",
    "How are you?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
    "What is your name?",
    "My name is Goffredo!"
]

trainer = ListTrainer(bot)

trainer.train(conversation)

conversation = [
    "Hello",
    "Hi there!",
    "How are you?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
    "What is your name?",
    "My name is Goffredo!",
    "how old are you?",
    "Such questions shall not be answered..."
]

trainer = ListTrainer(bot)

trainer.train(conversation)

import nltk
nltk.download('wordnet', quiet=True)

def chat(text):
    re = str(bot.get_response(text))
    say(re,'en')
    return
