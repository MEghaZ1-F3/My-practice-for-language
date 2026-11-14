def main():
    try:
        u = str(input("Enter a string: "))
        print(u)
    except Exception as i:
        print("An error occurred:", i)

    finally:
      print("This block will always execute, regardless of whether an error occurred or not.")

main()