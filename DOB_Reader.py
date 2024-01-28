def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            # Read all lines from the file into a list
            content = file.readlines()
        return content
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
    exit()    

def process_data(content):
    names = []
    birthdates = []

    # Iterate through each line in the file
    for line in content:
        # Split the line into a list using space as a separator
        line_details = line.split(" ")

        # Combine the first and second elements to get the full name
        full_name = line_details[0] + " " + line_details[1]
        names.append(full_name)

        # Combine the third, fourth, and fifth elements to get the full birthday
        birthday = line_details[2] + " " + line_details[3] + " " + line_details[4].strip("\n")
        birthdates.append(birthday)

    return names, birthdates

def main():
    file_path = 'DOB.txt'  # Replace with your actual file path
    content = read_file(file_path)

    # Process data
    names, birthdates = process_data(content)

    # Print "names"
    print("\nNames:")
    for name in names:
        print(name)

    # Print "birthdates"
    print("\nBirthdates:")
    for birthday in birthdates:
        print(birthday)


main()

