"""CLI entry point for Mist API Info Tool."""

import sys

from .client import main

if __name__ == "__main__":
    sys.exit(main() if hasattr(main, "__call__") else 0)
