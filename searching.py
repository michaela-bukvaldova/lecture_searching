from pathlib import Path
import json

from generators import unordered_sequence


def read_data(file_name, field):
    with open(file_name, mode = "r", encoding = "utf-8") as file:
        soubor = json.load(file)
        if data not in soubor:
            return None

    return data[field]

def linear_search(sequence, target_number):
    positions =[]
    for index, value in enumerate(sequence):
          if value == target_number:
            positions.append(index)
    return {"positions": positions, "count": len(positions)}

def binary_search(sequence, target_number):
    left = 0
    right = len(sequence) + 1
    while left <= right:
        mid = (left + right)//2
        if sequence[mid] == target_number:
            return mid
        elif sequence < target_number:
            left = mid + 1
        else:
            right = mid - 1
    return None
def main():
    unordered = read_data("sequential.json", "unordered_numbers")
    target = 5
    linear_result = linear_search(unordered, target)
    print(linear_result)

if __name__ == "__main__":
    main()
