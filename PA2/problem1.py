# Programmer: Kai Ibarrondo
# RUID: kai51
# Date: Feb 21, 2022
# Programming Homework: 02
#
# File: problem1.py

def remove_extra_whitespaces(infile, outfile):
    """Takes two arguments infile, a file name, and outfile, a file name,
    and rewrites the essay with all unnecessary whitespace removed."""

    # open files for reading and writing.
    input_file = open(infile, "r")
    out_file = open(outfile, "w")

    # read the file and use splitlines to show the \n characters in the list.
    file_contents = input_file.read()
    contents_split = file_contents.splitlines(True)

    # create a list to store the indexes of all \n with \n in front of it in the list.
    newlinechar_index = []

    # iterate through the list and when the element in the list
    # is \n and the element at the next index is \n append the index the element
    # to the list use enumerate to get the index and so the for loop does not
    # return an index error.
    for count, ele in enumerate(contents_split):
        if count != len(contents_split) - 1:
            if ele == "\n" and contents_split[count + 1] == "\n":
                newlinechar_index.append(count)

    # iterate through the list and delete the indexes that are in the
    # newlinechar_index. Then delete one from all the number in the list
    # as one element has been deleted from the contents_split list.
    for i in newlinechar_index:
        del contents_split[i]
        newlinechar_index[:] = [number - 1 for number in newlinechar_index]

    # use while loops to delete all \n characters from the start and end of list.
    while contents_split[0] == '\n':
        del contents_split[0]
    while contents_split[-1] == '\n':
        del contents_split[-1]

    # iterate through the and join all the word together using .join
    # method and use enumerate so that the last line is printed correctly.
    for count, line in enumerate(contents_split):
        if count + 1 == len(contents_split):
            line = line.replace("\n", "")
            line = " ".join(line.split())
            out_file.write(line)
        else:
            line = " ".join(line.split()) + "\n"
            out_file.write(line)

    # close the files.
    input_file.close()
    out_file.close()


def adjust_linelength(infile, outfile):
    """Takes two arguments infile, a file name, and outfile, a file name,
    and creates a file from the essay inputted that only contains at most 60
    character per line."""

    # open files for reading and writing.
    input_file = open(infile, "r")
    out_file = open(outfile, "w")

    # create a list of the words in the file, including the newline characters.
    words_newlinechar = input_file.read().split(" ")

    # use list comprehension to replace the \n characters with a space placeholder.
    # This needs to be done to get the words with \n characters apart.
    words = [word.replace("\n", " ") for word in words_newlinechar]

    # use list comprehension to split each word in the list again to
    # get placeholders for the \n characters and get the separate words.
    list_of_words = [word for line in words for word in line.split(" ")]

    # create empty string to add to.
    line = ""

    # iterate through the list of words to determine if the line is over 60 characters.
    for i in list_of_words:

        # if i is equal to a whitespace then it is a paragraph break,
        # so we must strip the line of any space, add the break,
        # and write it to the file. Then restart the line variable.
        if i == '':
            line = line.rstrip()
            line += "\n\n"
            out_file.write(line)
            line = ""

        # while the length of the line plus i and a space is under 60
        # continue to add words to the line.
        elif len(line + i + " ") <= 60:
            line += i + " "

        # when it is over 60 strip the line, add one new line character,
        # write the line to the file, then add the word to the new blank line
        # variable.
        elif len(line + i + " ") > 60:
            line = line.rstrip()
            line += "\n"
            out_file.write(line)
            line = ""
            line += i + " "

    # write the final line to the file.
    out_file.write(line.rstrip())

    # close the files.
    input_file.close()
    out_file.close()


def essay_statistics(infile, outfile):
    """Takes two arguments infile, a file name, and outfile, a file name,
    that will be used to read and output statistics regarding the inputted essay."""

    # open files for reading and writing.
    input_file = open(infile, "r")
    out_file = open(outfile, "w")

    # create intermediate name for later use.
    intermediate = infile.replace("_final.txt", ".txt")

    # create variables for the statistics that will be outputted.
    num_of_words = 0
    num_of_lines = 0
    len_of_words = 0

    # iterate thought the input file to gather the necessary info.
    # if the line is not "\n", then we add one to the number of lines.
    for i in input_file:
        if i != "\n":
            num_of_lines += 1

            # the number of words is equal to the length of
            # the list i.split.
            num_of_words += len(i.split())

        # iterate through each word and the list and
        # add the length together.
        for word in i.split():
            len_of_words += len(word)

    # calculate the average length of the words using the previous variables.
    avg_word_len = len_of_words // num_of_words

    out_file.write(f"In the file {intermediate}:\n\n")
    out_file.write("Number of (non-blank) lines: " + str(num_of_lines))
    out_file.write("\n            Number of words: " + str(num_of_words))
    out_file.write("\n        Average word length: " + str(avg_word_len))

    # close the files.
    input_file.close()
    out_file.close()


def format_essay():
    """ Takes no arguments. Asks for name of file, and prints various information to the
    screen regarding then names of the files it creates."""

    # prints header to screen.
    print("Essay Formatting Helper Program")
    print("-" * 31)

    # asks user for name of file containing essay, and uses the previously
    # created functions to create the various essays and statics needed.
    essay_name = input("\nEnter the name (*.txt) of the file containing the essay: ")
    intermediate = essay_name.replace(".txt", "")
    remove_extra_whitespaces(essay_name, intermediate + "_neb.txt")
    adjust_linelength(intermediate + "_neb.txt", intermediate + "_final.txt")
    essay_statistics(intermediate + "_final.txt", intermediate + "_stats.txt")

    # informs user what files were created.
    print(f"\nThe formatted essay is in the file {intermediate}_final.txt")
    print(f"The essay statistics are in the file {intermediate}_stats.txt")


if __name__ == "__main__":
    format_essay()
