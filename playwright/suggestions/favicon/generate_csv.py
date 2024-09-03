import csv
import random
import string

def generate_favicon():
    favicon = random.choice([0, 1])
    return favicon


def is_satisfied(favicon):
    return favicon

def generate_csv(filename, num_entries):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['favicon','is_satisfied']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for _ in range(num_entries):
            favicon = generate_favicon()
            writer.writerow({'favicon': favicon, 'is_satisfied': is_satisfied(favicon)})

def main():
    filename = "data.csv"
    num_entries = 100  # You can adjust the number of entries as needed
    generate_csv(filename, num_entries)
    print(f"CSV file '{filename}' generated successfully with {num_entries} entries.")

if __name__ == "__main__":
    main()
   
