import os

path = os.path.join("docs", "poem_original.txt")

def write_new_poem(lines, path2):
    """
    writes the given lines into the given file (path2)
    """
    try:
        with open(path2, "w") as f:
            for line in lines:
                f.write(line)
                f.write("\n")
    except FileNotFoundError as f:
        print("The file was not found", f)

def append_lines(path2):
    """
    adds the lines to file, path2
    """
    try:
        with open(path2, "a") as f:
            f.write("------ \n")
            f.write("Original Poem By: Robert Frost \n")
            f.write("Remixed By: Ruchama Wiederblank \n")
            f.write("The poem had been reversed and some words have been replaced.")
    except FileNotFoundError:
        print("File not found")