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
    match = re.search(r'^(.+)\1+$', ID)
    length = len(ID)
    if match:
        pattern = match.group(1)
        full_match = match.group(0)
        repeats = full_match.count(pattern)
        if repeats > 1 and repeats == length / len(pattern):
            return False
        else:
            return True
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
