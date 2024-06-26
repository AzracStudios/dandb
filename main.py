import argparse
from shell import shell

argparser = argparse.ArgumentParser(
    prog="DanDB", description="A simple SQL-like database"
)
argparser.add_argument("filename", nargs="?", default=None)

args = argparser.parse_args()


def main():
    if not args.filename:
        shell()


if __name__ == "__main__":
    main()
