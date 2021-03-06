import getpass
import os

import click

from scg import __version__
from scg import encrypt
from scg.config import KEY_FILE, SETTING_FILE, MAIL_CONFIG
from scg.content.message import Message
from scg.logo import logo
from scg.main import main

logo()


@click.group(invoke_without_command=True, no_args_is_help=True)
@click.pass_context
@click.version_option(version=__version__)
@click.option(
    "-c",
    "--csv",
    is_flag=False,
    type=click.Path(exists=True, file_okay=True, dir_okay=False),
    help="CSV file to read",
)
def entry_point(ctx, csv):
    """Send Custom Gmail via Python"""

    if ctx.invoked_subcommand is None:
        # click.echo("I was invoked without subcommand")
        if csv:
            main(csv)

    else:
        # click.echo("I am about to invoke %s" % ctx.invoked_subcommand)
        pass


@entry_point.command()
def init():
    print("====================Account Setting====================\n")

    account = input("Please Enter Your Gamil Account: ")

    if account:

        pwd = getpass.getpass("Password: ")

        if pwd:
            print(
                f"Your account and password will be encrypted and stored in {encrypt.SETTING_FILE}"
            )

            secret = (
                getpass.getpass("Your Encryption Secret: (default is 'scg')") or "scg"
            )

            key = encrypt.init_key(secret)

            encrypt.encrypt(key=key, account=account, pwd=pwd)
        else:
            print("It looks like you don't enter your password")

    else:
        print("It looks like you don't enter your account name")


@entry_point.command()
def check():
    print("====================Account Checking====================\n")

    key = encrypt.read_key()
    encrypt.decrypt(key)


@entry_point.command()
def mail():
    print("====================Mail Setting====================\n")
    message = Message()
    message.subject = input("Please Enter Your Mail Subject:\n")
    message.cc = input("Please Enter Your Mail CC:\n")
    message.fm = input("Please Enter Your Mail From:\n")
    message.to = input("Please Enter Your Mail To:\n")
    message.body = input("Please Enter Your Mail Body:\n")

    message.save_mail_setting()


@entry_point.command()
def clear():
    print("====================Clear Data and Setting====================\n")
    file_list = [SETTING_FILE, MAIL_CONFIG, KEY_FILE]

    for item in file_list:
        try:
            if os.path.isfile(item):
                os.remove(item)
        except OSError:
            pass

    print("Data and Setting are deleted successfully")


if __name__ == "__main__":
    entry_point()
