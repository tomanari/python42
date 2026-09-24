def garden_operations(operation_number: int) -> None:
  i = 0

  try:
      if i >= 0 and i <= 4:
          print(f"Input data is '{operation_number[i]}'")
          print(f"Temperature is now '{result}ºC'\n")
  except ValueError:
      print(f"Input data is {operation_number[i]}")
      print("Caught input_temperature error: invalid literal"
            f"for int() with base 10: '{operation_number[i]}'\n")
  except ZeroDivisionError:
      print(f"Input data is {operation_number[i]}")
      print("Caught input_temperature error: invalid literal"
            f"for int() with base 10: '{operation_number[i]}'\n")
  except FileNotFoundError:
        print(f"Input data is {operation_number[i]}")
        print("Caught input_temperature error: invalid literal"
              f"for int() with base 10: '{operation_number[i]}'\n")
  except TypeError:
        print(f"Input data is {operation_number[i]}")
        print("Caught input_temperature error: invalid literal"
              f"for int() with base 10: '{operation_number[i]}'\n") 
  print("All tests completed - program didn't crash!")


if __name__ == '__main__':
    print("=== Garden Temperature Checker ===\n")

    test_temperature()
