import os

device = {
        "magisk" : "unchecked",
        "root" : "unchecked",
        "su_binary" : "unchecked",
        }

def trigger_root():
    global device
    device["root"] = True


def check_for_su_binary():
    global device
    if os.path.isfile("/system/bin/su") == True:
        device["su_binary"] = True
        trigger_root()
    else:
        device["su_binary"] = False
    return 0


def check_for_magisk():
    global device
    if os.path.isfile("/system/bin/magisk") == True:
        device["magisk"] = True
        trigger_root()
    else:
        device["magisk"] = False
    return 0


def check_root():
    global device
    check_for_su_binary()
    check_for_magisk()
    if device["root"] != True:
        device["root"] = False
    return device



