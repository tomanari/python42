#!/usr/bin/env python3
def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature():
    temp0 = "25"
    temp1 = "abc"
    try:
        temp0 = input_temperature(temp0)
        print(f"Input data is '{temp0}'")
        print(f"Temperature is now '{temp0}ºC'\n")
    except ValueError:
        print(f"Input data is {temp0}")
        print("Caught input_temperature error: invalid literal"
              f"for int() with base 10: '{temp0}'\n")
    try:
        temp1 = input_temperature(temp1)
        print(f"Input data is '{temp1}'")
        print(f"Temperature is now '{temp1}ºC'")
    except ValueError:
        print(f"Input data is {temp1}")
        print("Caught input_temperature error: invalid literal"
              f"for int() with base 10: '{temp1}'\n")
    print("All tests completed - program didn't crash!")


if __name__ == '__main__':
    print("=== Garden Temperature ===\n")

    test_temperature()
