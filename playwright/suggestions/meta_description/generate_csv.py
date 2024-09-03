import csv
import random
import string

def generate_description():
    length = random.randint(100,400)
    description = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return description

def getDescriptionLength(description):
    return len(description)

def is_satisfied(description_length):
    return 155 <= description_length <=300


def generate_csv(filename, num_entries):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['description_length','is_satisfied']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for _ in range(num_entries):
            description = generate_description()
            description_length = getDescriptionLength(description)
            writer.writerow({'description_length': description_length, 'is_satisfied': is_satisfied(description_length)})

def main():
    filename = "data.csv"
    num_entries = 100  # You can adjust the number of entries as needed
    generate_csv(filename, num_entries)
    print(f"CSV file '{filename}' generated successfully with {num_entries} entries.")

if __name__ == "__main__":
    main()
   
