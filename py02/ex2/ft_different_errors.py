#!/usr/bin/env python3
def garden_operations(operation_number: int) -> None:

    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        10 / 0
    elif operation_number == 2:
        open("unknown.py")
    elif operation_number == 3:
        "42" + 0
    else:
        return


def test_error_types():
    operations = [0, 1, 2, 3, 4]
    for i in operations:
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
            print("Operation completed successfully\n")
        except (ValueError,
                ZeroDivisionError,
                FileNotFoundError,
                TypeError
        ) as ex:
            print(f"Caught {type(ex).__name__}: {ex}")

    print("All tests completed - program didn't crash!")


if __name__ == '__main__':
    print("=== Garden Temperature Checker ===\n")

    test_error_types()
