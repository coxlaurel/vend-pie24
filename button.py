import kivy

from kivy.uix.button import Button
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.screenmanager import SwapTransition


class MakeButton(Button, ButtonBehavior):
    """
    Class to create a button.

    Attributes:
        text: A string representing the name
        motor: An integer representing the corresponding motor number
        font_size: An integer representing the font size
        screen_manager: An instance of screen manager
    """
    def __init__(self, name, motor, screen_manager, size=30, **kwargs):
        """
        Function to initialize a button.

        Args:
            name: A string representing the name
            motor: An integer representing the corresponding motor number
            size: An integer representing the font size. Default = 30
            screen_manager: An instance of screen manager
        """
        super(MakeButton, self).__init__(**kwargs)
        self.status = 0
        self.text = name
        self.motor = motor
        self.font_size = size
        self.screen_manager = screen_manager

    def on_press(self):
        """
        A function to activate servo on button press.

        Returns:
            self.status: An integer 1 or 0 representing motor activation or not.
        """
        self.status = 1
        # write(self.motor)

    def on_release(self):
        """
        Function to switch to vending screen.
        """
        self.screen_manager.transition = SwapTransition(duration=2)
        self.screen_manager.current = 'vending'
