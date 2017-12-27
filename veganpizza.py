"""
"""
from subprocess import call

import pyautogui
import pyxhook
import sys
import time

class Listener:
    def __init__(self):
        def action():
            return
        self.action = action

    def set_action(self, action):
        self.action = action

    def advance(self, char):
        result = self.step(char)
        if result:
            self.action()

class WordListener(Listener):
    def __init__(self, string, case_insensitive=False):
        super().__init__()
        self.string = string
        if case_insensitive:
            self.string = self.string.lower()
        self.case_insensitive = case_insensitive
        self.state = 0

    def step(self, char):
        # Ignore all presses of the shift key.
        if char == "Shift_L" or char == "Shift_R":
            return False
        char_lower = char.lower()
        if self.case_insensitive:
            char = char_lower
        # print("char: {}".format(char))
        next_target = self.string[self.state]
        if char == next_target or (char_lower == 'return' and next_target == '\n'):
            self.state = self.state + 1
            # The whole string has matched.
            if self.state == len(self.string):
                # Reset so we match again from the start.
                self.state = 0
                # Return True to signal that the action should be performed.
                return True
            else:
                return False
        else:
            self.state = 0
            return False

class Listeners:
    def __init__(self):
        self.listeners = []

        def handle_event(event):
            key = event.Key
            for listener in self.listeners:
                listener.advance(key)

        hookman = pyxhook.HookManager()
        hookman.KeyUp = handle_event
        hookman.HookKeyboard()
        hookman.start()
        self.hookman = hookman

    def add_listener(self, listener):
        self.listeners.append(listener)

    def wait(self):
        while True:
            try:
                time.sleep(0.1)
            except KeyboardInterrupt:
                self.hookman.cancel()
                sys.exit()

# Actions

def write_text(text):
    pyautogui.typewrite(text)

def lock_screen():
    try:
        call(["gnome-screensaver-command", "--lock"])
        return
    except FileNotFoundError:
        pass
    call(["xdg-screensaver", "lock"])

# High-level functions

def replace_text(match, replace):
    l = WordListener(match)
    def action():
        # time.sleep(1)
        for _ in match:
            pyautogui.press('backspace')
        write_text(replace)
    l.set_action(action)
    return l
