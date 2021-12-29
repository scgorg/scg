import click

from scg import __version__


@click.version_option(version=__version__)
@click.command(no_args_is_help=True)
@click.option(
    "-t",
    "--test",
    is_flag=True,
    help="Hello",
)
def entry_point():
    """Send custom Gmail with Python"""


if __name__ == '__main__':
    entry_point()
