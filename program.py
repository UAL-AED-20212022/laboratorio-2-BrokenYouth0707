from sys import stdout
stdout.reconfigure(encoding='utf-8')
from view.cli import cli


def main() -> None:
    cli()

if __name__ == "__main__":
    main()