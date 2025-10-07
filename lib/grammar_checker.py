def grammar_checker(text):
    # split text to focuss on the first word
    split_text = text.split()
    return split_text[0] == split_text[0].capitalize() and text[-1] == "."