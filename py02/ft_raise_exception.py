def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature():
    temp = ["25", "abc", "100", "-50"]
    i = 0

    while i != 4:
        try:
            result = input_temperature(temp[i])
            if result > 40:
                print(f"Input data is '{temp[i]}'")
                print(f"Caught input_temperature error: {temp[i]}ºC "
                      "is too hot for plants (max 40ºC)\n")
            elif result < 0:
                print(f"Input data is '{temp[i]}'")
                print(f"Caught input_temperature error: {temp[i]}ºC "
                      "is too cold for plants (min 0ºC)\n")
            else:
                print(f"Input data is '{temp[i]}'")
                print(f"Temperature is now '{result}ºC'\n")
        except ValueError:
            print(f"Input data is {temp[i]}")
            print("Caught input_temperature error: invalid literal"
                  f"for int() with base 10: '{temp[i]}'\n")
        i += 1
    print("All tests completed - program didn't crash!")


if __name__ == '__main__':
    print("=== Garden Temperature Checker ===\n")

    test_temperature()
