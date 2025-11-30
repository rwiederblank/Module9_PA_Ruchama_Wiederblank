"""
Pseudocode
    type poem into poem_original.txt
    read all the lines into a list
    print the list
    create a new list with the original list reversed
    change some words in the new list
    write the new list into the file poem_remix.txt
    print the new poem
    append some information about the code to poem_remix.txt
"""
import os

path = os.path.join("docs", "poem_original.txt")
path2 = os.path.join("docs", "poem_remix.txt")

# importing the functions from other files
from read_file import read_poem
from remix_poem import reverse_lines,  replace_words
from write_file import write_new_poem, append_lines


def main():
    original = read_poem(path) # reads poem into list and prints it
    reversed_lines = reverse_lines(original) # reverses the order of the original poem
    changed_poem = replace_words(reversed_lines) # replaces some words in the reversed poem with new ones
    write_new_poem(changed_poem, path2) # writes the new poem into poem_remix.txt with its adjustments
    read_poem(path2) # prints the new poem
    append_lines(path2) # adds some information to poem_remix.txt

main()