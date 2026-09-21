import numpy as np

def clean_column(col, name="column"):
    col_fixed = np.where(np.isinf(col), np.nan, col)

    has_nan = np.isnan(col_fixed).any()
    print(f"{name} has Nan: ", has_nan)

    if has_nan:
        avg_data = np.nanmean(col_fixed)
        print(f"Average {name} marks: ", avg_data)

        col_cleaned = np.nan_to_num(col_fixed, nan=avg_data)
    else:
        col_cleaned = col_fixed

    # print(col_cleaned)
    # print("=" * 75)
    return col_cleaned

def clean_all_subjects(data, subjects):
    cleaned_columns = []
    for subject in subjects:
        cleaned = clean_column(data[subject], subject)
        cleaned_columns.append(cleaned)

    return np.column_stack(cleaned_columns)