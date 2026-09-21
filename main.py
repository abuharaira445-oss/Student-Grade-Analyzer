from load_data import data
from clean_data import clean_all_subjects
from analyze import analyze_grade

subjects = ["math", "physics", "chemistry", "english", "computer_science"]

cleaned_data = clean_all_subjects(data, subjects)

list = analyze_grade(cleaned_data, data["name"])