"""
message is for construct the mail content
"""


class Message:
    __slots__ = ["cc", "to", "fm", "subject"]

    def __init__(self):
        self.cc = ""
        self.to = ""
        self.fm = ""
        self.subject = ""
        self.body = ""

    @property
    def cc(self):
        return self.cc

    @property
    def to(self):
        return self.to

    @property
    def fm(self):
        return self.fm

    @property
    def subject(self):
        return self.subject

    @property
    def body(self):
        return self.body
