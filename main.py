import sys
import argparse
from lib.RUN import run


def main():
    print("爆破结果如下:")
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", dest="url", help="目标URL")
    parser.add_argument("-f", "--fil", dest="filename", default="110w.txt", help="字典路径")
    parser.add_argument("-t", "--thread", dest="count", type=int, default=10, help="威胁系数")
    args = parser.parse_args()

    if args.url and args.filename:
        run(args.url, args.filename, args.count)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == '__main__':
    main()
