"""Python static site generator hopefully the easiest (Inspired by Jekyll)"""
import argparse

__version__ = "0.0.0"


def main(argv=None):
    parser = argparse.ArgumentParser()
    sub_parsers = parser.add_subparsers(
        title="sub commands", dest="sub_commands", required=True
    )

    # flit init ----------------------------------------
    parser_init = sub_parsers.add_parser(
        "init", help="Initialize directory for github pages using pekyll"
    )
    
    parser_init.add_argument(
        "--root", type=str, default='.', help="Specifies the directory to initialize"
    )

    # flit build ---------------------------------------
    parser_build = sub_parsers.add_parser(
        "build", help="Build a static website using pekyll"
    )

    args = parser.parse_args(argv)

    if args.sub_commands == "init":
        from .initializer import intialize
        intialize()
    elif args.sub_commands == "build":
        from .builder import build
        build()