#!/usr/bin/python3

def main():
    webster = {"f1": "guest-wifi", "f2": "solaris", "f3": "sound physicians"}

    print(webster.get("f2"))
    print(webster["f2"])

    print(webster.get("floor5"))

    zlist = ["westlake", "southlake"]

    webster["f4"] = zlist

    print(webster)
    print("\n")
    print(webster["f4"][1])


main()
