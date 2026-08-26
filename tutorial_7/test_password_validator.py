import unittest
from password_validator import validate_password

class TestPasswordValidator(unittest.TestCase):

    def setUp(self):
        # 1. Valid passwords (return True)
        self.valid_passwords = [
            "INT6181P@ssw0rd",          # Standard valid password
            "A1#b2C3d",            # Length 8 (lower bound)
            "A1#b2C3d4E5f6G7h8I9j"    # Length 20 (upper bound)
        ]

        # 2. Invalid-length passwords (length < 8 or > 20, expected return False)
        self.invalid_length_passwords = [
            "A1#b2C3",                 # Length 7 (too short)
            "A1#b2C3d4E5f6G7h8I9j00"   # Length 22 (too long)
        ]

        # 3. Passwords missing a required character type (expected return False)
        self.missing_char_passwords = [
            "int6181!",   # Missing uppercase letter
            "INT6181!",   # Missing lowercase letter
            "EdUHK@MIT",      # Missing digit
            "EduHKINT6181"      # Missing special character
        ]

        # 4. Passwords containing whitespace (expected return False)
        self.space_passwords = [
            "EdUHK @ INT6181",
            " EdUHKINT6181!",
            "EdUHKINT6181!\t",
            "EdUHKINT6181!\n"
        ]

        # 5. Wrong-type inputs (expected return False)
        self.invalid_type_inputs = [
            12345678,
            None,
            ["EdUHKINT6181!"],
            True
        ]

    # ---------------------------------------------------------------
    # Test cases
    # ---------------------------------------------------------------

    def test_valid_passwords(self):
        #Test that all valid passwords return True.
        for pwd in self.valid_passwords:
            self.assertTrue(
                validate_password(pwd),
                msg=f"Password '{pwd}' should be valid."
            )

    def test_invalid_length_returns_false(self):
        #Test that passwords outside the 8-20 length range return False.
        for pwd in self.invalid_length_passwords:
            self.assertFalse(
                validate_password(pwd),
                msg=f"Password '{pwd}' has invalid length and should return False."
            )

    def test_missing_required_characters_returns_false(self):
        #Test that passwords missing uppercase, lowercase, digit, or special character return False.
        for pwd in self.missing_char_passwords:
            self.assertFalse(
                validate_password(pwd),
                msg=f"Password missing one of category char ('{pwd}') should return False."
            )

    def test_spaces_returns_false(self):
        #Test that passwords containing whitespace return False.
        for pwd in self.space_passwords:
            self.assertFalse(
                validate_password(pwd),
                msg=f"Password with spaces ('{repr(pwd)}') should return False."
            )

    def test_invalid_types_returns_false(self):
        #Test that non-string inputs return False.
        for pwd in self.invalid_type_inputs:
            self.assertFalse(
                validate_password(pwd),
                msg=f"Input {pwd} (type: {type(pwd)}) is not a string and should return False."
            )


if __name__ == '__main__':
    unittest.main()
