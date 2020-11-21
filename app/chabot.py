from textblob.classifiers import NaiveBayesClassifier
import json
import random
from pathlib import Path


class Chatbot:
    def __init__(self, intents):
        """
        The Chatbot class. Insert a json file in a specific format. The Chatbot will be trained
        to find a pattern in a given text string and return a response.
        Define the patterns the bot should find. Then set the answers it should give
        and give them both a suitable label.

        The format of the json file:

        {
            "intents": [
                {
                "label": "greeting",
                "patterns": [
                    "Hi",
                    "How are you",
                ],
                "responses": [
                    "Hello!",
                    "Good to see you again!",
                ],
        }

        :param intents: A json file with the intents. Use the specific format.

        """
        file_path = Path.cwd() / intents

        with open(file_path, "r") as file:
            self.data = json.load(file)

        self.classifier = self.train()

    def train(self):
        """
        Train a classifier dependeding on the data
        """
        train = []
        for intent in self.data["intents"]:
            for pattern in intent["patterns"]:
                train.append((pattern, intent["tag"]))

        cl = NaiveBayesClassifier(train)
        return cl

    def chat(self, input_text):
        """
        Insert a string and get a response

        :param input_text: A string that the response depends on
        """
        label = self.classifier.classify(input_text)
        return self.get_response(label)

    def get_response(self, label):
        """
        Insert a label defined in the intent data and get a random response

        :param label: The label of tha you want a response
        """
        intents = self.data["intents"]
        responses = [
            intent["responses"] for intent in intents if intent["tag"] == label
        ]
        return random.choice(responses[0])
