import re

from PySide6.QtGui import QValidator


class NumberValidator(QValidator):
    def validate(self, input_str, pos):
        # Validate the input based on your criteria
        if len(input_str) <= 5:
            if self.chceck_validity(input_str):
                return QValidator.State.Acceptable, input_str, pos
        return QValidator.State.Invalid, input_str, pos

    def chceck_validity(self, input_str: str):
        patterns = [r"\d{3}$", r"\d{2}$", r"\d$", r"\d{4}$", r"\d{5}$"]

        # Check if the input matches the pattern
        for pattern in patterns:
            if re.match(pattern, input_str) or input_str == "":
                return True
        return False
