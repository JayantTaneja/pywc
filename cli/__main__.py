import argparse
from .funcs import get_all, get_bytes, get_lines, get_words

def build_parser():
    ''' Returns parser (argparse.ArgumentParser)'''

    parser = argparse.ArgumentParser(
        prog = "py-wc",
        description = "A Python implementation of wc command line utility"
    )

    parser.add_argument("filename")
    parser.add_argument('-c', help="number of bytes", action="store_true")
    parser.add_argument('-l', help="number of lines", action="store_true")
    parser.add_argument('-w', help="number of words", action="store_true")

    return parser

def main():
    '''Main function'''

    parser = build_parser()
    args = parser.parse_args()

    filename, C, W, L = args.filename, args.c, args.w, args.l

    if C:   # Print Byte Count
        print(f"\t {get_bytes(filename)}", end = "")

    if L:   # Print Line Count
        print(f"\t {get_lines(filename)}", end = "")

    if W:   # Print Word Count
        print(f"\t {get_words(filename)}", end = "")
    
    if not C and not L and not W:               # Print Everything
        result = get_all(filename)
        print(f"\t {result[0]} \t {result[1]} \t {result[2]}", end = "")

    print(f"\t {filename}")

if __name__ == "__main__":
    main()
