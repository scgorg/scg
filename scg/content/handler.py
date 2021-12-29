class Handler:
    """
    This class is aim to deal with the mail content.
    """

    def __init__(self, mail_file):
        self.mail_file = mail_file

    def open(self, mail_file):
        """open and read the entire mail content, usually is a txt file"""
        with open(mail_file, "r") as mail:
            f = mail.read()


if __name__ == "__main__":
    pass
