def rename_to_snake_case(str):
    print('_'.join(str.lower().split()))


if __name__ == "__main__":
    str = input()
    rename_to_snake_case(str)


