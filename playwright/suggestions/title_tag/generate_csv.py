import csv
import random
import string

def generate_title():
    length = random.randint(40, 80)
    title = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return title

def is_satisfied(title):
    title_length = len(title)
    return 1 if 50 <= title_length <= 70 else 0

def generate_csv(filename, num_entries):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['title_length', 'is_satisfied']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for _ in range(num_entries):
            title = generate_title()
            writer.writerow({'title_length': len(title), 'is_satisfied': is_satisfied(title)})

def main():
    filename = "data.csv"
    num_entries = 100  # You can adjust the number of entries as needed
    generate_csv(filename, num_entries)
    print(f"CSV file '{filename}' generated successfully with {num_entries} entries.")

if __name__ == "__main__":
    main()
   
