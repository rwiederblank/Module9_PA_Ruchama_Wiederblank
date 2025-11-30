import os

path = os.path.join("docs", "poem_original.txt")

def read_poem(text):
    """
    takes in a file name
    reads the file and adds each line to a list
    prints each line
    returns the list
    """
    lines= []
    try:
        with open(text, "r") as f:
            for line in f:
                print(line)
                lines.append(line.strip())
    except FileNotFoundError as f:
        print("Error! Could not find file", f)
    return lines