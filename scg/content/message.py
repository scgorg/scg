"""
message is for construct the mail content
"""

import json


class Message:
    __slots__ = ["_cc", "_to", "_fm", "_subject", "_body"]

    def __init__(self):
        self._cc = ""
        self._to = ""
        self._fm = ""
        self._subject = ""
        self._body = ""

    @property
    def cc(self):
        return self._cc

    @cc.setter
    def cc(self, cc):
        self._cc = cc

    @property
    def to(self):
        return self._to

    @to.setter
    def to(self, to):
        self._to = to

    @property
    def fm(self):
        return self._fm

    @fm.setter
    def fm(self, fm):
        self._fm = fm

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, subject):
        self._subject = subject

    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, body):
        self._body = body

    def save_mail_setting(self):
        with open("mail-setting.json", "w") as json_file:
            content = {
                "cc": self._cc,
                "to": self._to,
                "from": self._fm,
                "subject": self._subject,
                "body": self._body,
            }
            json.dump(content, json_file, indent=4)
