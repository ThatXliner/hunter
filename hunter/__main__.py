"""The main CLI entry point"""
from hunter import core


def main() -> None:
    """The main CLI entry point"""
    core.Bot(print).run()


if __name__ == "__main__":
    main()
