"""
Input handling functions for the student grade calculator.

This module is responsible for all user input: student name (first, middle
initial, last), student ID, three test scores with validation (0-100), and
the continue (y/n) choice. It does not perform calculations or formatting;
callers use the returned values for that.
"""

from typing import Tuple


def get_student_name() -> Tuple[str, str, str]:
    """
    Prompt for and return the student's first name, middle initial, and last name.

    Reads three inputs from the user. The middle initial is normalized to a
    single character (first character only) so empty or multi-character input
    is handled consistently.

    Returns:
        A tuple of three strings: (first_name, middle_initial, last_name).
        middle_initial is always a single character or empty string.
    """
    # Prompt for first name; no validation, any string is accepted
    first_name = input("Please enter student's first name: ")
    # Get middle initial and strip whitespace so we can check length
    middle_initial = input("Please enter student's middle initial: ").strip()
    # If the user entered at least one character, keep only the first one
    if middle_initial:
        middle_initial = middle_initial[0]
    # If no middle initial was provided, middle_initial stays empty string
    # Prompt for last name
    last_name = input("Please enter student's last name: ")
    # Return all three values as a tuple for the caller to unpack
    return first_name, middle_initial, last_name


def get_student_id() -> int:
    """
    Prompt for and return the student's ID number as an integer.

    Reads one line of input and converts it to int. Caller should be aware
    that non-numeric input will raise ValueError.

    Returns:
        int: The student ID number entered by the user.
    """
    # Read input and convert to integer; pass result directly to caller
    return int(input("Please enter student's ID Number: "))


def get_validated_score(score_number: int) -> float:
    """
    Prompt for a single test score and return it only if it is in the valid range.

    Asks the user for score number 1, 2, or 3 (based on score_number). Re-prompts
    until the value is between 0 and 100 inclusive. Does not return until a
    valid score is entered.

    Args:
        score_number: An integer (typically 1, 2, or 3) used in the prompt
            text, e.g. "Please enter student's score1: ". Should be a positive
            integer for clear user messaging.

    Returns:
        float: The validated test score in the range 0.0 to 100.0.
    """
    # Keep asking until the user enters a score in the allowed range
    while True:
        # Read the score and convert to float for decimal support
        score = float(input(f"Please enter student's score{score_number}: "))
        # If the score is between 0 and 100 inclusive, it is valid
        if 0 <= score <= 100:
            return score
        # Otherwise show error message and loop again (re-prompt)
        print("Score should be greater than 0 and less than 100: ")


def get_continue_choice() -> bool:
    """
    Ask the user whether to continue adding another student.

    Prompts with "Do you want to continue: (y/n):". Response is stripped and
    lowercased so that 'Y' or 'y' are treated as yes; any other input is no.

    Returns:
        bool: True if the user entered 'y' (or 'Y'), False otherwise.
    """
    # Read response, remove leading/trailing spaces, and convert to lowercase
    response = input("Do you want to continue: (y/n): ").strip().lower()
    # Return True only when the user explicitly chose yes ('y')
    return response == 'y'
