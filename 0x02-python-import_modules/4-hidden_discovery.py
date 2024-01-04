#!/usr/bin/python3
hidden = __import__("4-hidden_discovery.pyc")

if __name__ == "__main__":
    for name in dir(hidden):
        print(name)
