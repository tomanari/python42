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
    i = 0

    while i <= 4:
        try:
            garden_operations(i)
            print("Testing operation 4...")
            print("Operation completed successfully\n")
        except ValueError:
            print("Testing operation 0...")
            print("Caught ValueError: invalid literal"
                  "for int() with base 10: 'abc'")
        except ZeroDivisionError:
            print("Testing operation 1...")
            print("Caught ZeroDivisionError: division by zero")
        except FileNotFoundError:
            print("Testing operation 2...")
            print("Caught FileNotFoundError: [Errno 2] No such file"
                  "or directory: '/non/existent/file'")
        except TypeError:
            print("Testing operation 3...")
            print("Caught TypeError: can only concatenate str "
                  "(not 'int') to str")
        i += 1
    print("All tests completed - program didn't crash!")


if __name__ == '__main__':
    print("=== Garden Temperature Checker ===\n")

    test_error_types()
