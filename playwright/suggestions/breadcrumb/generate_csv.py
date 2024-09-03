import csv
import random
import string

def generate_breadcrumb():
    breadcrumb = random.choice([0, 1])
    return breadcrumb


def is_satisfied(breadcrumb):
    return breadcrumb

def generate_csv(filename, num_entries):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['breadcrumb','is_satisfied']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for _ in range(num_entries):
            breadcrumb = generate_breadcrumb()
            writer.writerow({'breadcrumb': breadcrumb, 'is_satisfied': is_satisfied(breadcrumb)})

def main():
    filename = "data.csv"
    num_entries = 100  # You can adjust the number of entries as needed
    generate_csv(filename, num_entries)
    print(f"CSV file '{filename}' generated successfully with {num_entries} entries.")

if __name__ == "__main__":
    main()
   
