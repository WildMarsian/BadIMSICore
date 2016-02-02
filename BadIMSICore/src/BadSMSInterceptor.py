#!/usr/bin/python3.4

#Usage: BadSMSInterceptor.py -i <inputlog>

from PyTail import PyTail
import sys
import getopt


def main():
    input_log = ''
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi", ["help", "input="])
    except getopt.GetoptError as err:
        print(err)
        print("Usage: BadSMSInterceptor.py -i <input>")
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("Usage: BadSMSInterceptor.py -i <input>")
            sys.exit(0)
        elif opt in ("-i", "--input"):
            input_log = args[0]
        else:
            assert False, "unhandled exception"
    # We use a counter to skip every other line since the log duplicates SMQueue entries
    count = 0

    # There is 13 entries in SMQueue line log. With a list the last index is 12
    last_index_of_smqueue_line = 12

    for line in PyTail(input_log):
        count += 1
        line_words = line.split(" ")
        # If it's a line containing "Decoded", it means it's a SMQueue log entry
        if "Decoded" in line:
            # If the count is even, that means it's a duplicate
            if count % 2 == 0:
                # We remove that extra carrier return for pretty printing
                parsed_entry_delimiter = line_words[last_index_of_smqueue_line - 1]
                # Print instance of smqueue
                parsed_entry_instance = line_words[7]
                print(parsed_entry_instance + ": "+line.split(parsed_entry_delimiter)[2][:-1])
if __name__ == '__main__':
    main()
