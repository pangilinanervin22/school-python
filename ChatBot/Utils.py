def string_contains_require(input_string, possible_word, require):
    if not input_string.__contains__(require):
        return False

    return possible_word.__contains__(input_string)


def string_contains(input_string, possible_word):
    return possible_word.__contains__(input_string)
