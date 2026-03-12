"""
Calculation functions for the student grade calculator.

This module contains pure computation logic: no input or output. It computes
each student's total and average from three test scores, and the class
average from the sum of student averages and the number of students.
"""

from typing import Tuple


def calculate_student_average(score1: float, score2: float, score3: float) -> Tuple[float, float]:
    """
    Compute the sum and average of three test scores for one student.

    Adds the three scores and divides by 3 to get the average. Used to
    display the student's average and to accumulate into the class total.

    Args:
        score1: float. First test score (expected 0.0 to 100.0).
        score2: float. Second test score (expected 0.0 to 100.0).
        score3: float. Third test score (expected 0.0 to 100.0).

    Returns:
        Tuple[float, float]: (total, average) where total is score1 + score2
        + score3 and average is total / 3.
    """
    # Add the three scores to get the total points
    total = score1 + score2 + score3
    # Divide by 3 to get the student's average
    average = total / 3
    # Return both values so caller can use total if needed and average for display
    return total, average


def calculate_class_average(total_averages: float, student_count: int) -> float:
    """
    Compute the class average from the sum of all student averages and the student count.

    Used to show the overall class performance. Avoids division by zero when
    no students have been entered.

    Args:
        total_averages: float. Sum of every student's average (each student
            contributes one average to this sum).
        student_count: int. Number of students included in total_averages.
            Should be positive when total_averages is non-zero.

    Returns:
        float: The class average (total_averages / student_count), or 0.0
        when student_count is 0 to avoid division by zero.
    """
    # If no students have been entered, return 0.0 instead of dividing by zero
    if student_count == 0:
        return 0.0
    # Otherwise divide the running total of averages by the number of students
    return total_averages / student_count
