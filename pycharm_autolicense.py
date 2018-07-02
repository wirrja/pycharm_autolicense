#!/usr/bin/python3.6
import os.path
import subprocess
import subprocess


_API = 'https://api.ideaserver.pro/v1/domain'
_SERVER = requests.get(_API).json()


def get_url():
    url = _SERVER.get("domain")
    return f'http://{url}'

def get_path():
    list_files = os.listdir(path=os.getcwd())
    pycharm_root = list(filter(
        lambda x: '{}'.format('PyCharm') in x, list_files)
    )[0]
    key_path = os.path.join(os.getcwd(), pycharm_root, 'config/pycharm.key')
    return key_path

def main():
    try:
        with open(get_path(), 'w') as keyfile:
            keyfile.write(f'URL:{get_url()}')
        subprocess.Popen("pycharm-professional")
    except:
        print("First, you must run Pycharm, settings folder not found!")


if __name__ == '__main__':
    main()
