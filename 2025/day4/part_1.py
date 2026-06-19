import sys
import os
import copy
import pprint


sys.path.append(os.path.abspath(".."))


from util import get_file_content


PAPER = '@'
EMPTY = '.'


def pad_with_empty(arr):
    """
    Hardcoded solution for this only
    """
    row_len = len(arr[0])
    row_update = "." * (row_len + 2)
    new_list = [
        row_update,
        ]
    new_list.extend([f'{EMPTY}{slot}{EMPTY}' for slot in arr])
    new_list.append(row_update)
    return new_list


def main():
    content = get_file_content('real_input.txt')
    lines = content.rstrip().split('\n')
    padded_lines = pad_with_empty(lines)
    copied = copy.deepcopy(padded_lines)
    accessible_papers = 0
    for i in range(1, len(padded_lines), 1):
        skip = False
        for j in range(1, len(padded_lines[0]), 1):
            slot = padded_lines[i][j]
            if slot == EMPTY:
                continue
            assert slot == PAPER
            if i > 0 and i < len(padded_lines) - 1 and j > 0 and j < len(padded_lines[0]) - 1:
                count = 0
                slots = [
                    padded_lines[i][j + 1], # Right
                    padded_lines[i][j - 1], # left
                    padded_lines[i - 1][j], # top
                    padded_lines[i + 1][j], # bottom
                    padded_lines[i - 1][j + 1], # top right
                    padded_lines[i - 1][j - 1], # top left
                    padded_lines[i + 1][j + 1], # bottom right
                    padded_lines[i + 1][j - 1], # bottom left
                    ]
                
                if slots.count('@') < 4:
                    print(f"MARKED: padded_lines[{i}][{j}]")
                    l = list(copied[i])
                    l[j] = 'x'
                    copied[i] = ''.join(l)
                    accessible_papers += 1

    print(accessible_papers)
    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(copied)
                    
main()
