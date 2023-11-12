#!/usr/bin/env python

import argparse
import fileinput

def main():
    # define the arg parser
    parser = argparse.ArgumentParser(description="wc tool")

    # define commands (arguments)
    parser.add_argument("-c", action="store_true", help="Return byte count")
    parser.add_argument("-l", action="store_true", help="Return line count")
    parser.add_argument("-w", action="store_true", help="Return word count")
    parser.add_argument("-m", action="store_true", help="Return char count")
    parser.add_argument("filename", help="Input filename")

    args = parser.parse_args()

    if args.c:
        byte_count = byte_count_func(args.filename)
        print(f"{byte_count} {args.filename}")

    elif args.l:
        line_count = line_count_func(args.filename)
        print(f"{line_count} {args.filename}")
    elif args.w:
        word_count = word_count_func(args.filename)
        print(f"{word_count} {args.filename}")
    elif args.m:
        char_count = char_count_func(args.filename)
        print(f"{char_count} {args.filename}")
    else:
        byte_count = byte_count_func(args.filename)
        line_count = line_count_func(args.filename)
        word_count = word_count_func(args.filename)

        print(f"{line_count} {word_count} {byte_count} {args.filename}")
    

def byte_count_func(file_path):
    try:
        with open(file_path, "rb") as file:
            byte_count = len(file.read())
            return byte_count
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
def line_count_func(file_path):
    try:
        with open(file_path, "r") as file:
            line_count = sum(1 for line in file)
            return line_count
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
def word_count_func(file_path):
    try:
        with open(file_path, "r") as file:
            text = file.read()
            words = text.split()
            word_count = len(words)
            return word_count
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
def char_count_func(file_path):
    try:
        with open(file_path, "r") as file:
            text = file.read()
            char_count = len(text)
            return char_count
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
