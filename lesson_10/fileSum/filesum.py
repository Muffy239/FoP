

def file_sum(text_file):
    total = 0
    try:
        with open(text_file, 'r') as file:
            for line in file:
                numbers = line.split()
                for num in numbers:
                    total += float(num)
    except FileNotFoundError:
        print(f"{text_file} was not found")
        return 0
    return total


if __name__ == "__main__":
    print(file_sum("num_file.txt"))
