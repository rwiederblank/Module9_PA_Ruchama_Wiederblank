import os


path = os.path.join("docs", "poem_original.txt")
path2 = os.path.join("docs", "poem_remix.txt")


def reverse_lines(lines):
    """
    takes in a list, reverses it and returns it
    """
    return lines[::-1]

def replace_words(lines):
    """
    replaces instances of one word with another in the inputted list
    """
    new_list = []
    for line in lines:
        new_line = line.replace("snow", "glitter")
        new_line = new_line.replace("crow", "cat")
        new_line = new_line.replace("tree", "skyscraper")
        new_line = new_line.replace("heart", "brain")
        new_list.append(new_line)
    return new_list
