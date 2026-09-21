import numpy as np

def analyze_grade(cleaned_data, names):
    student_avg = cleaned_data.mean(axis=1)
    subject_avg = cleaned_data.mean(axis=0)

    ranked_indices = np.argsort(student_avg)[::-1]
    for rank, index in enumerate(ranked_indices, start=1):
        print(f"Rank {rank}: {names[index]}, Average {student_avg[index]:.2f}")

    pass_threshold = 40
    failing_mask = student_avg < pass_threshold  # boolean array, True where a student is failing

    failing_names = names[failing_mask]
    failing_scores = student_avg[failing_mask]

    if failing_names.size == 0:
        print("No students below the pass threshold.")
    else:
        for name, score in zip(failing_names, failing_scores):
            print(f"FAILING: {name} — Avg: {score:.2f}")

    return student_avg, subject_avg