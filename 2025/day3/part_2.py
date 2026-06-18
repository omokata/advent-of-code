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
    digits = []
    start = 0
    end = len(bank) - 11
    for i in range(11, -1, -1):
        m = max(bank[start:end])
        digits.append(m)
        idx = bank.index(m, start, end)
        start = idx + 1
        end += 1
    return int(''.join(digits))

        
def main():
    filepath = 'real_input.txt'
    content = get_file_content(filepath)
    total = 0
    for line in content.rstrip().split('\n'):
        max_jolt = get_maximum_from_bank(line)
        total += max_jolt
    print(total)


if __name__ == '__main__':
    main()
