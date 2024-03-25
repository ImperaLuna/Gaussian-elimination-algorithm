import numpy as np

# 3 equations with 3 unknown variables
# only 1 correct answer
test_case_1 = np.array([[-3.0, 2.0, -1.0, -1.0],
                        [6.0, -6.0, 7.0, -7.0],
                        [3.0, -4.0, 4.0, -6.0]])

# undetermined system with infinite number of solutions
test_case_2 = np.array([[1.0, -3.0, 2.0, 1.0],
                        [4.0, 1.0, -5.0, 17.0],
                        [2.0, -3.0, 1.0, 5.0]])

# inconsistent system with no solution
test_case_3 = np.array([[1.0, 1.0, 1.0, 2.0],
                        [0.0, 1.0, -3.0, 1.0],
                        [2.0, 1.0, 5.0, 0.0]])

# 4 equations with 4 variables
# only 1 possible solution
test_case_4 = np.array([[2.0, 3.0, -1.0, 4.0, 10.0],
                        [1.0, -1.0, 2.0, -1.0, 5.0],
                        [3.0, 4.0, -2.0, 1.0, 18.0],
                        [1.0, 1.0, 1.0, 2.0, 12.0]])

