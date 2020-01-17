#!/usr/bin/env python3
# -*- coding: utf8 -*-

# standar python library+
import sys, argparse, os

if not sys.version_info.major == 3 and sys.version_info.minor >= 6:
	print("\nKickSploit supports only python3.6 or higher\n")
	sys.exit(0)

# local lab classes
from lib.common import orchestra
from lib.common import completer

def usage():
    """where we parse all our arguments"""
    parser = argparse.ArgumentParser(description="Lab - Simplify your life - Ethical Hacking tool")
    parser.add_argument("-q", "--quiet", help="suppress war", action="store_true")
    parser.add_argument("--option", metavar="OPTION", default=None
        ,help="set an option to start")
    parser.add_argument("--list-options", action="store_true", default=False
        ,help="List Lab's options")

    return parser.parse_args()

def main():
    args = usage()
    completer = HeaderCompleter()
    completer.header(args.quiet)
    if args.option:
        # Fire!
        lab = orchestra.LabConductor()
        lab.start(args.option)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
