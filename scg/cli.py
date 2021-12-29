import getpass

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
    print("====================SCG====================\n")

    account = input("Please input your Gamil account: ")

    if account:

        pwd = getpass.getpass('Password: ')

        if pwd:
            print("Your account and password will be encrypted and stored in setting.json")
            print(account)
            print(pwd)
        else:
            print("It looks like you don't enter your password")

    else:
        print("It looks like you don't enter your account name")


if __name__ == "__main__":
    entry_point()
