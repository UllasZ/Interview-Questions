"""
scores = [
    {"subject": "maths", "july": 91, "august": 97},
    {"subject": "english", "july": 89, "august": 85},
    {"subject": "science", "july": 98, "august": 93},
    {"subject": "social science", "july": 94, "august": 90},
    {"subject": "kannada", "july": 96, "august": 97},
    {"subject": "music", "august": 85},
    {"subject": "sports", "july": 92},
]
"""

monthly_scores_doc = """ Q1. Convert the above data structure, split the data into the following formats
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

# ----------------------------------------------------------------------------------------------------------------------
# Given Data
scores = [
    {"subject": "maths", "july": 91, "august": 97},
    {"subject": "english", "july": 89, "august": 85},
    {"subject": "science", "july": 98, "august": 93},
    {"subject": "social science", "july": 94, "august": 90},
    {"subject": "kannada", "july": 96, "august": 97},
    {"subject": "music", "august": 85},
    {"subject": "sports", "july": 92},
]


def student_score(student_scores, july_month_scores=None, august_month_score=None):
    # Initiate empty lists
    if august_month_score is None and july_month_scores is None:
        july_month_scores = []
        august_month_score = []

    # Append the data as key:value pairs
    for idx, items in enumerate(student_scores):
        if "july" in list(items.keys()):
            july_month_scores.append({items["subject"]: items["july"]})

        if "august" in list(items.keys()):
            august_month_score.append({items["subject"]: items["august"]})
    return july_month_scores, august_month_score


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    # Q1
    scores_july, scores_august = student_score(scores)

    print(f"\nscores_july = {scores_july}")
    print(f"\nscores_august = {scores_august}")
