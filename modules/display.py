"""
Display/output functions for the student grade calculator.

This module handles all console output: formatted student details (name, ID,
three scores, average) and the final session summary (number of students and
class average). It does not read input or perform calculations; it only
prints. Functions in this module do not return values.
"""


def print_student_info(
    first_name: str,
    middle_initial: str,
    last_name: str,
    student_id: int,
    score1: float,
    score2: float,
    score3: float,
    average: float
) -> None:
    """
    Print a formatted block of student information and test scores to the console.

    Outputs the student's name (first, middle initial, last), ID, three test
    scores with two decimal places, and the computed average, then a separator
    line. Does not return a value; all work is done via print statements.

    Args:
        first_name: str. Student's first name.
        middle_initial: str. Student's middle initial (typically one character).
        last_name: str. Student's last name.
        student_id: int. Student's ID number.
        score1: float. First test score (displayed with 2 decimal places).
        score2: float. Second test score (displayed with 2 decimal places).
        score3: float. Third test score (displayed with 2 decimal places).
        average: float. Computed average of the three scores (displayed with 2 decimals).

    Returns:
        None. This function only prints; it does not return a value.
    """
    # Print each field on its own line in the required format
    print(f"Student's First Name= {first_name}")
    print(f"Student's Middle Initial= {middle_initial}")
    print(f"Student's Last Name= {last_name}")
    print(f"Student's ID Number= {student_id}")
    # Scores and average shown with two decimal places
    print(f"Student's Test Score1= {score1:.2f}")
    print(f"Student's Test Score2= {score2:.2f}")
    print(f"Student's Test Score3= {score3:.2f}")
    print(f"Student's Average= {average:.2f}")
    # Visual separator before the continue prompt
    print("\n ************************")


def print_summary(student_count: int, class_average: float) -> None:
    """
    Print the final session summary: total number of students and class average.

    Called once at the end of the program after the user has finished entering
    all students. Outputs two lines only. Does not return a value.

    Args:
        student_count: int. Total number of students processed in this session.
        class_average: float. The overall class average (sum of student
            averages divided by student count). Displayed with 2 decimal places.

    Returns:
        None. This function only prints; it does not return a value.
    """
    # Show how many students were entered
    print(f"Total Number of students: {student_count}")
    # Show the class average with two decimal places
    print(f"Class Average= {class_average:.2f}")
