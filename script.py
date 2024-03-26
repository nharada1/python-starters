"""Script overview.

Details about the script, and how to run it with the arguments included.

python script.py --arg_path /path/to/thing --debug
"""
import argparse
import pathlib


def main(args: argparse.Namespace):
    """Define your main function here."""
    print(args)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Example script to demonstrate argparse usage."
    )

    parser.add_argument(
        "--path",
        type=pathlib.Path,
        required=True,
        help="The path to the file or directory.",
    )
    parser.add_argument("--name", type=str, required=True, help="A name string.")
    parser.add_argument("--number", type=int, required=True, help="An integer number.")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode.")

    args = parser.parse_args()
    main(args)
