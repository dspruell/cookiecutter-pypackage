"""{{ cookiecutter.project_description }}"""

import argparse
import logging
from importlib.metadata import version

__application_name__ = "{{ cookiecutter.project_name }}"
__version__ = version(__application_name__)
__full_version__ = f"{__application_name__} {__version__}"

logging.basicConfig(level=logging.DEBUG, format="[%(levelname)s] %(message)s")


def cli():
    description = "{{ cookiecutter.project_description }}"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("name", help="name to greet")
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="be verbose"
    )
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=__full_version__,
        help="print package version",
    )
    args = parser.parse_args()

    if args.verbose:
        logging.debug("about to greet name: %s", args.name)
    print(f"Hello {args.name}!")
