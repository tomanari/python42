#!/usr/bin/env python3

class   plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age
        print("=== Garden Plant Register ===")
        print(f"{name.capitalize()}: {height}cm, {age} days old")


if __name__ == "__main__":
    plant("Rose", 34, 26)