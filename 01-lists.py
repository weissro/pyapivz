#!/usr/bin/python3

def main():
    mylist = ["bert", 55, "juniper", "cisco", ["bigip", "meraki", "dell"]]
    print(mylist[2])
    print(f"My network providers are {mylist[2]} and {mylist[3]}.")

    print(mylist[4][1])

if __name__ == "__main__":
    main()

