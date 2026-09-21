import numpy as np

data = np.genfromtxt(
    'student_grades.csv',
    delimiter=',',
    names=True,
    dtype=None,
    encoding='utf-8'
)
