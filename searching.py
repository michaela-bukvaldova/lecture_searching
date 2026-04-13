from pathlib import Path
import json


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


def binary_search(numbers_list, target_number):
    for number in numbers_list:
        while number != target_number:
            return None

def main():
    unordered = read_data(file_name:"sequential.json", field:"unordered_numbers")
    target = 5
    linear_result = linear_search(unordered, target)
    print(linear_result)

if __name__ == "__main__":
    main()
