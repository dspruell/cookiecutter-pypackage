"""
{{ cookiecutter.project_description }}

"""

import argparse
from json import dumps as json_dumps
import logging


logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] %(message)s'
)


def cli():
    description = "{{ cookiecutter.project_description }}"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('name', help='name to greet')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='be verbose')
    args = parser.parse_args()

    if args.verbose:
        logging.debug("about to greet name: %s", args.name)
    print(f"Hello {args.name}!")
