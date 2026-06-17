import sys
import re


def get_file_content(filepath):
    content = ""
    try:
        with open(filepath, "r") as f:
            content = f.read()
    except OSError as e:
        raise
    return content


def is_valid_id(ID: str):
    assert type(ID) == str
    if len(ID) % 2 != 0:
        # Ignore ID that is odd number
        return True
    lower_mid = len(ID) // 2
    if ID[:lower_mid] == ID[lower_mid:]:
        return False
    return True

    
def main():
    filepath = sys.argv[1]
    content = get_file_content(filepath)
    ranges = content.split(',')

    acc_ID = 0

    for rnge in ranges:
        s = rnge.split('-')
        lower_bound = s[0]
        upper_bound = s[1]
        for ID in range(int(lower_bound), int(upper_bound) + 1, 1):
            valid = is_valid_id(str(ID))
            if not valid:
                print(f"Ranges: {lower_bound} - {upper_bound} | ID: {ID} | {valid}")
                acc_ID += ID

    print(acc_ID)
            

if __name__ == '__main__':
    main()
