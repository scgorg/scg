import click

from scg import __version__


@click.group(invoke_without_command=True, no_args_is_help=True)
@click.pass_context
@click.version_option(version=__version__)
@click.option(
    "-c",
    "--csv",
    is_flag=False,
    help="CSV file to read",
)
def entry_point(ctx, csv):
    """Send custom Gmail with Python"""
    if ctx.invoked_subcommand is None:
        click.echo('I was invoked without subcommand')
    else:
        click.echo('I am about to invoke %s' % ctx.invoked_subcommand)


@entry_point.command()
def init():
    print("init")


if __name__ == "__main__":
    entry_point()
