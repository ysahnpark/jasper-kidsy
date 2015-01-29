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

    max_attempts = 3

    question = get_a_question()

    attempt = 0
    is_correct = False

    while attempt < max_attempts and not is_correct:
        attempt += 1

        mic.say("What is " + str(question[1]) + " plus " + str(question[2]))
        response = mic.activeListen()

        numservice = NumberService()

        try:
            numbers = re.findall(r'\d+', response)
            #user_answer  = numservice.parse(response)

            if len(numbers) > 0:
                user_answer = numbers[0];

                if user_answer == question[0]:
                    mic.say("Yay! You are right!")
                    is_correct = True
                else:
                    comment = ''
                    if attempt < max_attempts - 1:
                        comment = "Try again"
                    else:
                        comment = "The correct answer is " + question[0]
                    mic.say("Nah, that is incorrect! " + comment)
            elif len(response) == 0:
                mic.say("Too late!")
            else:
                mic.say("Could not understand your answer!")

        except:
            mic.say("Could not understand your answer!")



def isValid(text):
    """
        Returns True if the input is related to the news.
        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\b(math)\b', text, re.IGNORECASE))