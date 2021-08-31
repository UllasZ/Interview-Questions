"""
Consider the following list of dictionaries. It stores the information of candidates and their
scores:
candidates = [
{"name": "Candidate A", "id": 1, "score": 63.7},
{"name": "Candidate B", "id": 2, "score": 98.3},
{"name": "Candidate C", "id": 3, "score": 63},
{"name": "Candidate D", "id": 4},
{"name": "Candidate E", "id": 5, "score": 64},
]
Write a Python snippet to sort the candidates in descending order by their scores. If a candidate
does not have a score, they should be placed at the end.
"""

candidates = [
    {"name": "Candidate A", "id": 1, "score": 63.7},
    {"name": "Candidate B", "id": 2, "score": 98.3},
    {"name": "Candidate C", "id": 3, "score": 63},
    {"name": "Candidate D", "id": 4},
    {"name": "Candidate E", "id": 5, "score": 64},
]

result = sorted(candidates, key=lambda d: d['score'] if 'score' in d.keys() else -1, reverse=True)
print(result)
