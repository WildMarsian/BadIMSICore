#!/usr/bin/python3.4

from PyTail import PyTail

# We use a counter to skip every other line since the log duplicates SMQueue entries
count = 0

# There is 13 entries in SMQueue line log. With a list the last index is 12
last_index_of_smqueue_line = 12

for line in PyTail("smqueue.txt"):
    count += 1
    line_words = line.split(" ")
    # If it's a line containing "Decoded", it means it's a SMQueue log entry
    if "Decoded" in line:
        # If the count is even, that means it's a duplicate
        if count % 2 == 0:
            # We remove that extra carrier return for pretty printing
            parsed_entry_delimiter = line_words[last_index_of_smqueue_line - 1]
            #print(parsed_entry_delimiter)
            # Print instance of smqueue
            parsed_entry_instance = line_words[7]
            print(parsed_entry_instance + ": "+line.split(parsed_entry_delimiter)[2][:-1])
