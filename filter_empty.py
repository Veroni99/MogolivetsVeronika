def remove_empty_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as file: 
        lines = file.readlines()

    non_empty_lines = [line for line in lines if line.strip() != '']

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(non_empty_lines)


def main():
    file_path = input()
    remove_empty_lines(file_path)

if name == 'main':
    main()
