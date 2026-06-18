def get_file_content(filepath):
    content = ""
    try:
        with open(filepath, "r") as f:
            content = f.read()
    except OSError as e:
        raise
    return content


def get_maximum_from_bank(bank: str):
    assert type(bank) == str
    first_digit = 0
    first_cursor = 0
    for i, digit in enumerate(bank):
        n = int(digit)
        if i < len(bank) - 1 and n > first_digit:
            first_digit = n
            first_cursor = i
    second_digit = max(bank[first_cursor + 1:])
    return int(f"{first_digit}{second_digit}")
    
    
def main():
    filepath = 'real_input.txt'
    content = get_file_content(filepath)
    total = 0
    for line in content.rstrip().split('\n'):
        print(line)
        max_jolt = get_maximum_from_bank(line)
        total += max_jolt
    print(total)


if __name__ == '__main__':
    main()
