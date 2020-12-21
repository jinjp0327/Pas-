import time
import getpass
from itertools import product

target = getpass.getpass(prompt="パスワードを入力してください:")
chars = "0123456789abcdefghijklmnopqrstuvwxyz"

def check(text, repeat):
    passwords = product(text, repeat=repeat)
    for i, passwords in enumerate(passwords):
        print("＼033[32m" + str(i) + ":" + "".join(passwords) + "＼033[0m")
        if "".join(passwords) == target:
            return "".join(passwords)


def yes_no_input():
    while True:
        choice = input("パスワードの解析を始めますか？[y/N]: ").lower()
        if choice == "y":
            return True
        else:
            return False

if yes_no_input():
    start = time.time()
    pw = check(chars, 6)

    if pw is None:
        print("failure")
    else:
        print("パスワードが見つかりました！-->", pw)
    finish = time.time() - start
    print(finish, "秒")
else:
    print("program end")