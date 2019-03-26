import os

from WPGenerator.GUIBuilder import GUIBuilder
from WPGenerator.Validation import Validation


Validation.is_user_root()
application = GUIBuilder()
application.show_window()
