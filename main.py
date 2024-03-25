import numpy as np
import sys

from test_cases import *

separator = f"<{50 * '='}>"
def determine_system_size() -> tuple[int, int]:
    """
    Determine the matrix size of the system.

    :return:
    `tuple` -- A 2-element tuple representing the size of the system.
          - The first element is the number of rows.
          - The second element is the number of columns.
    """
    number_of_equations = int(input("How many equations are in the system? "))
    number_of_variables = int(input("How many variables are in the equations? "))
    return number_of_equations, number_of_variables


def matrix_input(num_equations : int, num_variables : int) -> np.ndarray:
    """
    Get coefficients for each equation.
    :return
    `np.ndarray` -- The coefficients for each equation and results on the last position
    """
    numpy_matrix = np.zeros((num_equations, num_variables + 1))
    for i in range(num_equations):
        print(f"Equation {i+1}:")
        for j in range(num_variables):
            variable = float(input(f"Enter coefficient for variable {j+1} in equation {i+1}: "))
            numpy_matrix[i, j] = variable
        result = float(input(f"Enter result for equation {i+1}: "))
        numpy_matrix[i, -1] = result
    return numpy_matrix


def print_equation(numpy_matrix: np.ndarray) -> None:
    """
    Function prints the system of linear equations
    :param numpy_matrix:
    :return: None
    """
    num_equations, num_variables = numpy_matrix.shape[0], numpy_matrix.shape[1] - 1

    for i in range(num_equations):
        equation_str = f"Equation {i+1}: "
        for j in range(num_variables):
            equation_str += f"{numpy_matrix[i, j]} x{j+1} + "
        equation_str = equation_str[:-2]
        equation_str += f"= {numpy_matrix[i, -1]}"
        print(equation_str)


def solve_variables(numpy_matrix: np.ndarray) -> np.ndarray:
    """
    Function solves the system of linear equations for systems that only have one possible solution
    :param numpy_matrix:
    :return:
    """
    num_equations, num_variables = numpy_matrix.shape[0], numpy_matrix.shape[1] - 1
    solutions = np.zeros(num_variables)

    for i in range(num_equations - 1, -1, -1):
        solutions[i] = numpy_matrix[i, -1]
        for j in range(i + 1, num_variables):
            solutions[i] -= numpy_matrix[i, j] * solutions[j]

    return solutions


def gaussian_elimination(numpy_matrix: np.ndarray) -> tuple[str, np.ndarray]:
    """
    Function integrates the gaussian elimination algorithm with partial pivoting and back substitution

    :param numpy_matrix:
    :return: tuple of a string representing the type of system we are dealing with and the final numpy array
    """
    num_equations, num_variables = numpy_matrix.shape[0], numpy_matrix.shape[1] - 1

    for i in range(num_variables):
        # Partial pivoting
        max_row = i
        for k in range(i + 1, num_equations):
            if abs(numpy_matrix[k, i]) > abs(numpy_matrix[max_row, i]):
                max_row = k
        numpy_matrix[[i, max_row]] = numpy_matrix[[max_row, i]]

        for j in range(i + 1, num_equations):
            factor = numpy_matrix[j, i] / numpy_matrix[i, i]
            numpy_matrix[j, i:] -= factor * numpy_matrix[i, i:]

    # Check for inconsistency or undetermined
    for i in range(num_equations):
        if numpy_matrix[i, i] == 0 or numpy_matrix[i, i] == 1:
            if numpy_matrix[i, -1] != 0:
                return "Inconsistent", numpy_matrix
            else:
                return "Undetermined", numpy_matrix

    # Back substitution
    for i in range(num_equations - 1, -1, -1):
        numpy_matrix[i, i + 1:] = numpy_matrix[i, i + 1:] / numpy_matrix[i, i]
        numpy_matrix[i, i] = 1.0
        for j in range(i - 1, -1, -1):
            numpy_matrix[j, i:] -= numpy_matrix[j, i] * numpy_matrix[i, i:]

    return "Consistent with a unique solution", numpy_matrix

def get_test_case(test_case_choice):
    """
    Returns the test case data based on the user's choice.

    :param test_case_choice: The test case choice (1-4)
    :return: The NumPy matrix for the chosen test case
    """
    if test_case_choice == 1:
        return test_case_1
    elif test_case_choice == 2:
        return test_case_2
    elif test_case_choice == 3:
        return test_case_3
    elif test_case_choice == 4:
        return test_case_4
    else:
        raise ValueError("Invalid test case choice")


def run_test_case(numpy_matrix):
    print(separator)
    print_equation(numpy_matrix)
    print(separator)
    print(f"Matrix before operations:\n{numpy_matrix}")

    result, solution_matrix = gaussian_elimination(numpy_matrix)
    print(separator)
    print(f"Result: {result}")
    if result == "Consistent with a unique solution":
        solutions = solve_variables(solution_matrix)
        print("Solutions:")
        for i, solution in enumerate(solutions):
            print(f"x{i + 1} = {solution}")
    elif result == "Undetermined":
        print(separator)
        print("System is undetermined. Matrix after Gaussian elimination:")
        print(solution_matrix)

def run():
    """
    Run the program
    :return:
    """
    num_equations, num_variables = determine_system_size()
    numpy_matrix = matrix_input(num_equations, num_variables)
    print(separator)
    print_equation(numpy_matrix)
    print(separator)
    print(f"Matrix before operations:\n{numpy_matrix}")

    result, solution_matrix = gaussian_elimination(numpy_matrix)
    print(separator)
    print(f"Result: {result}")
    if result == "Consistent with a unique solution":
        solutions = solve_variables(solution_matrix)
        print("Solutions:")
        for i, solution in enumerate(solutions):
            print(f"x{i + 1} = {solution}")
    elif result == "Undetermined":
        print(separator)
        print("System is undetermined. Matrix after Gaussian elimination:")
        print(solution_matrix)


def main():
    if "--run_tests" in sys.argv:
        print("Choose a test case (1-4):")
        for i in range(1, 5):
            print(f"{i}. Test case {i}")
        test_case_choice = int(input("Enter your choice: "))

        if 1 <= test_case_choice <= 4:
            numpy_matrix = get_test_case(test_case_choice)
            run_test_case(numpy_matrix)

        else:
            print("Invalid choice. Exiting.")
            return
    else:
        run()


if __name__ == "__main__":
    main()
