"""
Student Grade Calculator - Main Program

Module to run the student grade calculator application. Calculates the average
of three test scores for each student and the overall class average. Original
Java program (CSC-117) converted to Python with a modular architecture.

This module imports input, calculation, and display helpers and orchestrates
the main loop: collect student data, compute averages, show results, and
optionally continue with another student.

Author: Hamza Siyam
"""

from input_utils import (
    get_student_name,
    get_student_id,
    get_validated_score,
    get_continue_choice,
)
from calculations import calculate_student_average, calculate_class_average
from display import print_student_info, print_summary


def main() -> None:
    """
    Run the main program loop for the student grade calculator.

    Prompts for one or more students: name, ID, three test scores. Computes
    each student's average and the running class average, then asks whether
    to add another student. Does not return a value; prints output via
    display functions and exits when the user chooses not to continue.

    Returns:
        None. This function only orchestrates I/O and calls other functions;
        it does not return a value.
    """
    # Running sum of all student averages, used to compute class average
    total_averages = 0.0
    # Number of students entered in this session
    student_count = 0

    # Loop until the user chooses to stop adding students
    while True:
        # Call input_utils to get first name, middle initial, and last name
        first_name, middle_initial, last_name = get_student_name()
        # Get the student's ID number from the user
        student_id = get_student_id()

        # Get three validated scores (each must be between 0 and 100)
        score1 = get_validated_score(1)
        score2 = get_validated_score(2)
        score3 = get_validated_score(3)

        # Pass the three scores to calculations to get total and average
        total, average = calculate_student_average(score1, score2, score3)
        # Add this student's average to the running total for class average
        total_averages += average

        # Pass all student data to display so it can print the formatted output
        print_student_info(
            first_name, middle_initial, last_name,
            student_id, score1, score2, score3, average
        )

        # One more student has been processed
        student_count += 1
        # Compute current class average from running total and count
        class_average = calculate_class_average(total_averages, student_count)

        # Ask user if they want to add another student
        if not get_continue_choice():
            # If user did not answer 'y', exit the loop
            break

    # After loop ends, print final summary (total students and class average)
    print_summary(student_count, class_average)


# If this file is run as the main script (not imported), start the program
if __name__ == "__main__":
    main()
