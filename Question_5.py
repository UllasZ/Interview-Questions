"""
    QUESTION 5
    NER Tagging
    In NLP, a Named Entity is a real-world object that’s assigned a name – for example, a person, a
    country, a product or a book title. A typical Named Entity Recognition (NER) algorithm takes a
    sentence and tags each of the words with a label. Consider the following labels:
    Entity Name Label Code
    Degree DEG
    Major MAJ
    Institute INS
    Company COM
    Location LOC
    Title TIT
    Other OTH
    Example:
    Sentence : I am a Python Developer at Skillate in Bengaluru
    NER tags : OTH OTH OTH TIT TIT OTH COM OTH LOC .
    The NER tags tell us about the following information:
    Title : Python Developer
    Company : Skillate
    Location : Bengaluru
    Your task -
    1. Write a Python function to extract the NER tagged information.
    2. The function will take two strings as input:
    - sentence: an input sentence
    - ner_tags: the corresponding NER tags
    3. The function returns the entities present in “sentence” using the corresponding labels
    present in “ner_tags”.
    4. The returned value must be in the form of a dictionary. The dictionary will have the
    following possible keys:
    [“Degree”, “Major”, “Institute”, Company”, “Location”, “Title”]
    A sample input and the expected output are given below.
    5. NOTE:
    - The length of words in “sentence” will be the same as the length of words in
    “ner_tags”. Both these inputs will be provided by us.
    - Ignore all the entities tagged as Other (OTH).
    - If a NER label occurs consecutively, then the corresponding entities must be
    considered as part of a single entity group.
    Example: In the following sentence, the words “Python Developer” must be a
    single entity while “Intern” is another entity.
    Sentence : I was an Intern at Skillate then a Python Developer
    NER tags : OTH OTH OTH TIT OTH COM OTH OTH TIT TIT .
    Sample Input
    sentence = “I was an Intern at Skillate then a Python Developer”
    ner_tags = “OTH OTH OTH TIT OTH COM OTH OTH TIT TIT”
    Expected Output
    {
    “Title” : [“Intern”, “Python Developer”],
    “Company” : [“Skillate”]
    }
    6. HINT:
    The function signature can be as follows:
    def extract_ner(sentence: str, ner_tags: str) -> dict:
    pass
"""

user_sentence = "I was an Intern at Skillate then a Python Developer "
user_ner_tags = "OTH OTH OTH TIT OTH COM OTH OTH TIT TIT"

labels = {
    "Degree": "DEG",
    "Major": "MAJ",
    "Institute": "INS",
    "Company": "COM",
    "Location": "LOC",
    "Title": "TIT",
    "Other": "OTH", }


def extract_ner(sentence: str, ner_tags: str) -> dict:
    dic = dict(zip(list(sentence.split(" ")), list(ner_tags.split(" "))))
    items = {}
    for i1 in labels.items():
        for i2 in dic.items():
            if i2[1] in i1[1]:
                if i2[1] == 'OTH':
                    pass
                else:
                    items.setdefault(i1[0], [])
                    items[i1[0]].append(i2[0])

    return items


print(user_sentence)
print(user_ner_tags)
print("\n")

result = extract_ner(user_sentence, user_ner_tags)
print(result)
