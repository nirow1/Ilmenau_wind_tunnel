import re

from PySide6.QtGui import QValidator

class NumberValidator(QValidator):
    def __init__(self, numbers, max_val = 1000000):
        super().__init__()
        self.max_val = max_val
        self.patterns = [fr"\d{{{i}}}$" for i in range(1, numbers + 1)]
        self.patterns.append(r"\d$")

    def validate(self, input_str, pos):
        # Validate the input based on your criteria
        if len(input_str) <= 5:
            if self.check_validity(input_str):
                return QValidator.State.Acceptable, input_str, pos
        return QValidator.State.Invalid, input_str, pos

    def check_validity(self, input_str: str):
        # Check if the input matches the pattern
        for pattern in self.patterns:
            if re.match(pattern, input_str) and int(input_str) <= self.max_val or input_str == "":
                return True
        return False