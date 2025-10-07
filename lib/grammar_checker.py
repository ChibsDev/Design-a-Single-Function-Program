def grammar_checker(text):
    if text is None:
        raise Exception("Please provide text and I will check your grammar")
    elif text.strip() == "":
        return False
    # split text to focuss on the first word
    split_text = text.split()
    return split_text[0] == split_text[0].capitalize() and text[-1] in ".!?"