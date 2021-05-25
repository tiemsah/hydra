# import
import os
import platform
import getpass
import sys
import time
from text_to_speech import speak
from touch import touch
import platform
import socket
import psutil
import uuid
import re
# info
windows = []
for info in sys.getwindowsversion():
    windows.append(info)
# main
print(f"Microsoft Windows [Version {windows[0]}.{windows[1]}.{windows[2]}]")
while True:
    print(f"┌──([{getpass.getuser()}]@[{platform.node()}])-[{os.getcwd()}]")
    command = input("└─$ ")
    cml = command.split(" ")
    cmd = cml[0]
    target = " ".join(cml[1:])
    # ls
    if cmd == "ls":
        if len(cml) == 1 and len(cml) < 2:
            files = os.listdir()
            print(f"total = [{len(files)}]")
            for file in files:
                try:
                    mtime = time.strftime("%d/%m/%Y\t%H:%M", time.localtime(os.path.getmtime(file)))
                except FileNotFoundError:
                    if os.path.isdir(file):
                        print(f"##/##/####\t##:##\t<DIR>\t{file}")
                    else:
                        print(f"##/##/####\t##:##\t<FILE>\t{file}")
                else:
                    if os.path.isdir(file):
                        print(f"{mtime}\t<DIR>\t{file}")
                    else:
                        print(f"{mtime}\t<FILE>\t{file}")
        elif len(cml) == 2 or len(cml) > 2:
            try:
                files = os.listdir(target)
            except NotADirectoryError:
                print(f"this is a file -> [{target}] -> ._.")
            except FileNotFoundError:
                print("not found")
            else:
                print(f"total = [{len(files)}]")
                for file in files:
                    try:
                        if target == "\\" or target == "/":
                            mtime = time.strftime("%d/%m/%Y\t%H:%M", time.localtime(os.path.getmtime(target + file)))
                            if os.path.isdir(target + file):
                                print(f"{mtime}\t<DIR>\t{file}")
                            else:
                                print(f"{mtime}\t<FILE>\t{file}")
                        else:
                            mtime = time.strftime("%d/%m/%Y\t%H:%M", time.localtime(os.path.getmtime(target + "\\" + file)))
                            if os.path.isdir(target + "\\" + file):
                                print(f"{mtime}\t<DIR>\t{file}")
                            else:
                                print(f"{mtime}\t<FILE>\t{file}")
                    except FileNotFoundError:
                        if target == "\\" or target == "/":
                            if os.path.isdir(target + file):
                                print(f"##/##/####\t##:##\t<DIR>\t{file}")
                            else:
                                print(f"##/##/####\t##:##\t<FILE>\t{file}")
                        else:
                            if os.path.isdir(target + "\\" + file):
                                print(f"##/##/####\t##:##\t<DIR>\t{file}")
                            else:
                                print(f"##/##/####\t##:##\t<FILE>\t{file}")
                    else:
                        pass
        else:
            print("error")
    # pwd
    elif cmd == "pwd":
        if len(cml) == 1:
            print(f"{os.getcwd()}")
        else:
            print("error")
    # cd
    elif cmd == "cd":
        if len(cml) == 2 or len(cml) > 2:
            try:
                os.chdir(target)
            except FileNotFoundError:
                print("not found")
            except NotADirectoryError:
                print(f"this is a file -> [{cml[1]}] -> ._.")
            else:
                drnm = os.getcwd().split("\\")
                if drnm[0] == "C:" and drnm[1] == "":
                    if cml[1] == "/":
                        print(f"dir changed -> [/]")
                    else:
                        print(f"dir changed -> [\\]")
                else:
                    print(f"dir changed -> [{drnm[-1]}]")
        else:
            print("error")
    # cat
    elif cmd == "cat":
        if len(cml) == 2:
            try:
                file = open(target)
            except PermissionError:
                print("error")
            except FileNotFoundError:
                print("error -> not found")
            else:
                numberOfLines = 1
                for line in file:
                    print(line, end="")
        else:
            print("error")
    # echo
    elif cmd == "echo":
        if len(cml) > 1:
            print(target)
        else:
            print("error")
    # say
    elif cmd == "say":
        if len(cml) > 1:
            if cml[1] == "de":
                language = "de"
                target = " ".join(cml[2:])
            elif cml[1] == "ar":
                language = "ar"
                target = " ".join(cml[2:])
            else:
                language = "en"
            speak(target, language)
    # mkdir
    elif cmd == "mkdir":
        if len(cml) > 1:
            path = "."
            names = cml[1:]
            for name in names:
                try:
                    os.mkdir(f"{path}/{name}")
                except FileExistsError:
                    print(f"already created -> [{name}]")
                except PermissionError:
                    print("PermissionError")
                except FileNotFoundError:
                    print("error")
                else:
                    print(f"dir created -> [{name}]")
        else:
            print("error")
    # touch
    elif cmd == "touch":
        if len(cml) > 1:
            path = "."
            names = cml[1:]
            files = os.listdir()
            for name in names:
                try:
                    if name in files:
                        confirm = input(f"already created -> [{name}] do you want replace? (y = yes, n = no) ")
                        if confirm == "y" or confirm == "yes":
                            touch(f"{path}/{name}")
                            print(f"file created -> [{name}]")
                        else:
                            print("ok")
                    else:
                        touch(f"{path}/{name}")
                        print(f"file created -> [{name}]")
                except FileExistsError:
                    print(f"already created -> [{name}]")
                except PermissionError:
                    print("PermissionError")
                except FileNotFoundError:
                    print("error")
                else:
                    pass
        else:
            print("error")
    # rm
    elif cmd == "rm":
        if len(cml) > 1:
            pass
        else:
            print("error")
    # rn
    elif cmd == "rn":
        if len(cml) > 1:
            pass
        else:
            print("error")
    # rmdir
    elif cmd == "rmdir":
        if len(cml) > 1:
            pass
        else:
            print("error")
    # cp
    elif cmd == "cp":
        if len(cml) > 1:
            pass
        else:
            print("error")
    # mv
    elif cmd == "mv":
        if len(cml) > 1:
            pass
        else:
            print("error")
    # info
    elif cmd == "info":
        if len(cml) == 1:
            print(f"platform\t\t[{platform.system()}]")
            print(f"platform release\t[{platform.release()}]")
            print(f"platform version\t[{platform.version()}]")
            print(f"architecture\t\t[{platform.machine()}]")
            print(f"hostname\t\t[{platform.node()}]")
            print(f"ip address\t\t[{socket.gethostbyname(platform.node())}]")
            print(f"mac address\t\t[{':'.join(re.findall('..', '%012x' % uuid.getnode()))}]")
            print(f"processor\t\t[{platform.processor()}]")
            print(f"ram\t\t\t[{str(round(psutil.virtual_memory().total / (1024.0 **3)))}] GB")
        else:
            print("error")
    # netstat
    elif cmd == "netstat":
        if len(cml) == 1:
            pass
        else:
            print("error")
    # ifconfig
    elif cmd == "ifconfig":
        if len(cml) == 1:
            pass
        else:
            print("error")
    # exit
    elif cmd == "exit":
        if len(cml) == 1:
            exit()
        else:
            print("error")
    else:
        print(f"[{cmd}] -> not found")
