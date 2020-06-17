from processdoc import process_document


def test_example_1():
    with open("example_1.txt", encoding="utf-8") as f:
        actual_result = process_document(f.read())
        expected_result = {'en': 5, 'ink': 2, 'be': 1, 'had': 19, 'thought': 2, 'have': 1, 'd': 19, 'id': 1, 've': 1, 'ought': 2, 'been': 5, 'think': 2, 'did': 1}
        assert expected_result == actual_result


def test_example_2():
    with open("example_2.txt", encoding="utf-8") as f:
        actual_result = process_document(f.read())
        expected_result = {'been': 20, 'am': 57, 'en': 20, 'id': 35, 'have': 117, 'ne': 10, 'm': 57, 'did': 35, 've': 117, 'do': 74, 'd': 17, 'done': 10, 'ay': 53, 'seen': 6, 'had': 17, 're': 65, 'be': 200, 'ink': 22, 'say': 53, 'ought': 8, 'o': 74, 'think': 22, 'one': 10, 'thought': 8, 'are': 65, 'said': 14, 'aid': 14, 'een': 6}
        assert expected_result == actual_result


def test_exxample_3():
    with open("exxample_3.txt", encoding="utf-8") as f:
        actual_result = process_document(f.read())
        expected_result = {'am': 75, 'be': 187, 'ne': 22, 'are': 87, 'ought': 9, 'o': 90, 'been': 17, 'done': 22, 'one': 22, 'have': 192, 've': 192, 'ay': 61, 'say': 61, 'think': 38, 'ink': 38, 'seen': 5, 'did': 31, 'een': 5, 'do': 90, 'said': 11, 'aid': 11, 'thought': 9, 'm': 75, 'd': 49, 're': 87, 'had': 49, 'id': 31, 'en': 17}
        assert expected_result == actual_result


def test_example_4():
    with open("example_4.txt", encoding="utf-8") as f:
        actual_result = process_document(f.read())
        expected_result = {'ve': 163, 'en': 22, 'o': 112, 'ne': 4, 'have': 163, 'say': 41, 'id': 43, 'done': 4, 'one': 4, 'ink': 25, 'ay': 41, 'had': 42, 'am': 73, 'een': 5, 'been': 22, 'm': 73, 'aid': 13, 'said': 13, 'seen': 5, 'be': 186, 'ought': 8, 're': 98, 'd': 42, 'did': 43, 'are': 98, 'thought': 8, 'think': 25, 'do': 112}
        assert expected_result == actual_result
