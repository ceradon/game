#!/usr/bin/env python

class Letter_Game(object):
    def __init__(self):
        self._intro = [
            ""
        ]
        
        self._questions = [
            ("What does AMS stand for?", "Administrative Management Society"),
            ("In a block style letter, how many times do you press enter after the date?",
                "4", "4 times", "four"),
            ("A letter has its date indented. What style does it use?", "modified block style"),
            ("If 'cc' is on a letter, what does it stand for?", "carbon copy")
        ]
