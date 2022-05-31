# -*- coding: utf-8 -*-
import random
from naomi import plugin

class Plugin(plugin.SpeechHandlerPlugin):
    def intents(self):
        _ = self.gettext
        return {
            'GreetingsIntent': {
                'locale': {
                    'en-US': {
                        'templates': [
                            "HELLO",
                            "HI",
                            "GOOD MORNING",
                            "GOOD AFTERNOON",
                            "GOOD EVENING"
                        ]
                    }
                },
                'action': self.handle
            },
            'GoodbyeIntent': {
                'locale': {
                    'en-US': {
                        'templates': [
                            "GOODBYE",
                            "GOOD NIGHT"
                        ]
                    }
                },
                'action': self.handle_goodbye
            },
            'CanYouHearMe': {
                'locale': {
                    'en-US': {
                        'templates': [
                            "CAN YOU HEAR ME",
                            "HELLO CAN YOU HEAR ME"
                        ]
                    }
                },
                'action': self.handle_can_you_hear_me
            },
            'HowAreYou': {
                'locale': {
                    'en-US': {
                        'templates': [
                            "HOW ARE YOU"
                        ]
                    }
                },
                'action': self.handle_how_are_you
            }
        }

    def handle(self, intent, mic):
        choices = [
            "Hello.",
            "Hi.",
            "Hi there."
        ]
        if('MORNING' in intent['input']):
            choices.append('GOOD MORNING')
        if('AFTERNOON' in intent['input']):
            choices.append('GOOD AFTERNOON')
        if('EVENING' in intent['input']):
            choices.append('GOOD EVENING')
        mic.say(random.choice(choices))

    def handle_goodbye(self, intent, mic):
        choices = [
            "So long.",
            "Farewell.",
            "Goodbye."
        ]
        if('NIGHT' in intent['input']):
            choices.append("GOOD NIGHT")
        mic.say(random.choice(choices))

    def handle_can_you_hear_me(self, intent, mic):
        mic.say('Yes, I can hear you.')

    def handle_how_are_you(self, intent, mic):
        choices = [
            "I'm fine.",
            "Fine, thanks.",
            "Have you ever had one of those days where you just want to kill all humans?",
            "I think you should know I'm feeling rather depressed."
        ]
        mic.say(random.choice(choices))
        mic.say("Now, what can I do for you?")
