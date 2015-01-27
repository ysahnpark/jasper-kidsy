__author__ = 'ysahn'

import os
import Story
import unittest

class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        # Nothing to do
        self.repo_path = self.get_path('repo/')

    def test_get_a_story(self):
        story = Story.get_a_story(self.repo_path)
        self.assertIsNotNone(story)
        print(story)

    def get_path(self, relative_path):
        return os.path.join(os.path.dirname(__file__), "../" + relative_path)