import sys
import argparse
from lib.RUN import run


def main():
    print("The results of the blasting are as follows:")
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", dest="url", help="Destination URL")
    parser.add_argument("-f", "--fil", dest="filename", default="110w.txt", help="Dictionary Path")
    parser.add_argument("-t", "--thread", dest="count", type=int, default=10, help="The threat factor")
    args = parser.parse_args()

    if args.url and args.filename:
        run(args.url, args.filename, args.count)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == '__main__':
    main()
