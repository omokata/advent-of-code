def get_file_content(filepath):
    content = ""
    try:
        with open(filepath, "r") as f:
            content = f.read()
    except OSError as e:
        raise
    return content


in_filepath = "real_input.txt"
content = get_file_content(in_filepath)

instructions = content.rstrip().split("\n")

max_n = 100
dial_pointer = 50
clicks_to_zero = 0
zero_count_any = 0
for instr in instructions:

    direction = instr[0]
    n = int(instr[1:])

    if direction == "L":
        dial_pointer = (dial_pointer - n) % max_n
    elif direction == "R":
        dial_pointer = (dial_pointer + n) % max_n
    else:
        print("Invalid input")
        exit(69)

    if dial_pointer:
        zero_count_any += 1

print(zero_count_any)
