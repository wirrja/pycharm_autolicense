#!/usr/bin/env python3
import os
import sys
import requests
import subprocess
from tkinter import messagebox


_API = "https://api.ideaserver.pro/v1/domain"
_SERVER = requests.get(_API).json()
_HOMEDIR = os.getenv('HOME')

def get_url():
    url = _SERVER.get("domain")
    return f"http://{url}"


def ide_choice(ide):
    return {
        "pycharm": "pycharm-professional",
        "goland": "goland",
        "webstorm": "webstorm"
        }.get(ide, None)


def folder_choice(ide):
    return {
        "pycharm": "PyCharm",
        "goland": "GoLand",
        "webstorm": "WebStorm"
        }.get(ide.lower(), None)


def get_path(ide):
    keyfile = folder_choice(ide)
    list_files = os.listdir(path=_HOMEDIR)
    pycharm_root = list(filter(lambda x: f"{keyfile}" in x, list_files))[0]
    key_path = os.path.join(_HOMEDIR, pycharm_root, f"config/{ide}.key")
    return key_path


def main(ide):
    try:
        with open(get_path(ide), "w") as keyfile:
            keyfile.write(f"URL:{get_url()}")
        subprocess.Popen(f"{ide_choice(ide)}")
    except:
        messagebox.showerror(
            "Warning", f"First you must run {ide}! Configuration folder not found!"
        )


if __name__ == "__main__":
    ide = sys.argv[1]
    main(ide)
