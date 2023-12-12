import re


def rename_to_snake_case(str_seq):
    return '_'.join(str_seq.strip('.').lower().split()) if ' ' in str_seq else '_'.join(
        [i.lower() for i in re.findall(r'[a-z, A-Z][^A-Z]*', str_seq.strip('.'))])


if __name__ == "__main__":
    str_seq = input()
    print(rename_to_snake_case(str_seq))
