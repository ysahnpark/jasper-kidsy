# -*- coding: utf-8-*-
import glob
import random
#from client import app_utils
import re

WORDS = ["STORY"]

PRIORITY = 3


def get_a_story(story_repo_path=None):

    story_repo_path = story_repo_path if story_repo_path.endswith('/') else story_repo_path + '/'
    story_repo_path += '*.story.txt'
    print("Selecting from " + story_repo_path)
    story_files = glob.glob(story_repo_path)

    if len(story_files) == 0:
        print("No Story");
        return None

    # Select one
    idx = random.randint(0, len(story_files) - 1)
    story_path = story_files[idx]
    story_text = None
    print("Loading " + story_path);
    with open(story_path, 'r') as story_file:
        story_lines = story_file.readlines()
        story_text = ''.join(story_lines).replace('\n', ' ')


    return story_text


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
    mic.say("Retrieving a story")
    story_repo = profile['story_repo'] if 'story_repo' in profile else '~/prjs/jasper-kidsy/repo'
    print(story_repo)
    story = get_a_story(story_repo)
    if story != None:
        mic.say(story)
    else:
        mic.say("Sorry. I could not retrieve story")


def isValid(text):
    """
        Returns True if the input is related to the news.
        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\b(story)\b', text, re.IGNORECASE))