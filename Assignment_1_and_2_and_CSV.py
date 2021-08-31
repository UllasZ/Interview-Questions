"""
scores_july = [
    {
        "maths": 91,
        "english": 89,
        "science": 98,
        "social science": 94,
        "kannada": 96,
        "sports": 92,
    }
]
scores_august = [
    {
        "music": 85,
        "maths": 97,
        "english": 85,
        "science": 93,
        "social science": 90,
        "kannada": 97,
    }
]
"""
import csv
import os

scores_doc = """ \nQ2. Convert the above data structures to the following format
scores = [
    ("maths", 91, 97),
    ("english", 89, 85),
    ("science", 98, 93),
    ("social science", 94, 90),
    ("kannada", 96, 97),
    ("music", None, 85),
    ("sports", 92, None),
] \n"""

scores_2_doc = """ \n Q3. Convert the above data structures to the following format
scores_2 = [
    {"subject": "maths", "july": 91, "august": 97},
    {"subject": "english", "july": 89, "august": 85},
    {"subject": "science", "july": 98, "august": 93},
    {"subject": "social science", "july": 94, "august": 90},
    {"subject": "kannada", "july": 96, "august": 97},
    {"subject": "music", "july": None, "august": 85},
    {"subject": "sports", "july": 92, "august": None},
] \n"""

csv_dump_doc = """ Dump the results to CSV in this format
subject         | july  | august    |
-------------------------------------
maths           | 91    | 97        |
english         | 89    | 85        |
science         | 98    | 93        |
social science  | 94    | 90        |
kannada         | 96    | 97        |
music           | -     | 85        |
sports          | 92    | -         | """

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
scores_july = [
    {
        "maths": 91,
        "english": 89,
        "science": 98,
        "social science": 94,
        "kannada": 96,
        "sports": 92,
    }
]
scores_august = [
    {
        "music": 85,
        "maths": 97,
        "english": 85,
        "science": 93,
        "social science": 90,
        "kannada": 97,
    }
]


# ----------------------------------------------------------------------------------------------------------------------

def scores(dictionary1, dictionary2, student_scores=None):
    # Initiate an empty list
    if student_scores is None:
        student_scores = []

    for key1, key2 in zip(dictionary1, dictionary2):
        if key2 not in dictionary1:
            student_scores.append((key2, None, dictionary2[key2],))

        if key1 not in dictionary2:
            student_scores.append((key1, dictionary1[key1], None,))

        elif key1 in dictionary2 or key2 in dictionary1:
            student_scores.append((key1, dictionary1[key1], dictionary2[key1],))

    return student_scores


# ----------------------------------------------------------------------------------------------------------------------

def scores_2(student_scores, student_scores_2=None):
    # Initiate an empty list
    if student_scores_2 is None:
        student_scores_2 = []

    # Map the keys "subject", "july", "august" to their respective values.
    # Append the dictionary to the list.
    for dic in student_scores:
        student_scores_2.append({"subject": dic[0], "july": dic[1], 'august': dic[2]})

    return student_scores_2


# ----------------------------------------------------------------------------------------------------------------------

def csv_dump():
    # Dump the data as dictionary to the csv file

    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "student_data.csv")

    with open(os.path.join(path), "w") as f:
        csv.DictWriter(f, fieldnames=list(student_score_2[0].keys()))
        f_csv = csv.DictWriter(f, list(student_score_2[0].keys()))
        f_csv.writeheader()
        f_csv.writerows(student_score_2)

    print("Data dumped to the csv file successfully!\n")


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    # Q2
    student_score = scores(scores_july[0], scores_august[0])
    print(f"\nscores = {student_score}\n")

    # Q3
    student_score_2 = scores_2(student_score)
    print(f"scores_2 = {student_score_2}\n")

    # CSV Dump
    csv_dump()
