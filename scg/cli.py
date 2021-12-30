import getpass
import json

import click
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad

from scg import __version__
from scg.config import key
from scg.logo import logo

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
    """Send custom Gmail via Python"""

    if ctx.invoked_subcommand is None:
        click.echo("I was invoked without subcommand")
    else:
        click.echo("I am about to invoke %s" % ctx.invoked_subcommand)


@entry_point.command()
def init():
    print("====================Account Setting====================\n")
    print(key)
    account = input("Please input your Gamil account: ")

    if account:

        pwd = getpass.getpass("Password: ")

        if pwd:
            print(
                "Your account and password will be encrypted and stored in setting.json"
            )

            cipher = AES.new(key, AES.MODE_CBC)
            encoded_data = json.dumps({"ACCOUNT": account, "PASSWORD": pwd}).encode(
                "utf-8"
            )
            print(encoded_data)
            cipheredData = cipher.encrypt(pad(encoded_data, AES.block_size))
            print(cipheredData)
            with open("setting.bin", "wb") as f:
                f.write(cipher.iv)
                f.write(cipheredData)

        else:
            print("It looks like you don't enter your password")

    else:
        print("It looks like you don't enter your account name")


@entry_point.command()
def check():
    print("====================Account Checking====================\n")

    inputFile = "setting.bin"

    with open(inputFile, "rb") as f:
        iv = f.read(16)
        cipheredData = f.read()

    cipher = AES.new(key, AES.MODE_CBC, iv=iv)

    originalData = unpad(cipher.decrypt(cipheredData), AES.block_size)
    setting = json.loads(originalData.decode("utf-8"))
    if setting["ACCOUNT"] and setting["PASSWORD"]:
        print("Account is all set")
    else:
        print("Your account is not set up")


if __name__ == "__main__":
    entry_point()
