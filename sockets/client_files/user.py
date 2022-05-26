""" User class """
import json

from client_files.config import *


class User:
    """ User class nad methods """


    # Variables
    nickname = ""
    message = ""

    def get_nickname(self) -> str:
        try:
            nickname = input("Enter nickname: ")
            return nickname
            raise RuntimeError(f"ERROR: get_nickname error value: {nickname}")
        except RuntimeError as re:
            print(re)


    def login(self):
        self.nickname = self.get_nickname()
        print("Logining in...")
        print(f"Hello {self.nickname}!")


    def send_message(self):
        self.message = input("Command: ")
        msg = {
            "nickname": self.nickname,
            "message": self.message
        }
        msg_to_send = json.dumps(msg).encode(CODING)
        return msg_to_send
