# -*- coding: utf-8-*-
from semantic.numbers import NumberService
import random
#from client import app_utils
import re

WORDS = ["MATH"]

PRIORITY = 3


def get_a_question(min=0, max=10, op='+'):

    num1 = random.randint(min, max)
    num2 = random.randint(min, max)
    answer = num1 + num2
    question = (answer, num1, num2)

    return question


def handle(text, mic, profile):
    """
        Responds to user-input, typically speech text, with a summary of
        the day's top news headlines, sending them to the user over email
        if desired.
        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    question = get_a_question()
    mic.say("What is " + str(question[1]) + " plus " + str(question[2]))
    response = mic.activeListen()

    numservice = NumberService()
    user_answer  = numservice.parse(response)
    if user_answer == question[0]:
        mic.say("Yay! You are right!")
    else:
        mic.say("Nah, that is incorrect!")


def isValid(text):
    """
        Returns True if the input is related to the news.
        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\b(math)\b', text, re.IGNORECASE))