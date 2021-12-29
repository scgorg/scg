import click

from scg import __version__


@click.version_option(version=__version__)
@click.command(no_args_is_help=True)
@click.option(
    "-c",
    "--csv",
    is_flag=False,
    help="CSV file to read",
)
def entry_point(csv):
    """Send custom Gmail with Python"""
    print(csv)


if __name__ == "__main__":
    entry_point()
