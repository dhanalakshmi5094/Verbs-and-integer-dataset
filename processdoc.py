import re


def process_document(document: bytes):
    # JSON Patterns from patterns.json file
    pattern1 = r"\b(ha(ve|d)|a(m|re)|\bbe(en)?\b|d(o(ne)?|id)|s(ay|aid|een)|th(ink|ought))\b"
    pattern2 = r"^[-+]?\\d+$"
    result = {}  # empty dictionary
    # to find out each word or letter that matches with pattern from given document .Findall method can return  empty
    # strings also along with matching elements.
    verbs = re.findall(pattern1, document)
    # remove empty strings from verbs
    verbs = [j for i in verbs for j in i if j != '']
    integers = re.findall(pattern2, document)
    integers = [j for i in integers for j in i if j != '']
    # concatenation of both verbs list and integer list
    verbs_integers = verbs + integers
    # set functions returns unique verbs or integers
    unique_verbs_integers = list(set(verbs_integers))
    # assigning verb and integers and their counts to result dictionary
    for word in unique_verbs_integers:
        result[word] = verbs_integers.count(word)
    return result

