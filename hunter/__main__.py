"""The main CLI entry point"""


from hunter.smart import backends


def main() -> None:
    """The main CLI entry point"""
    backends.autogui()


if __name__ == "__main__":
    main()
