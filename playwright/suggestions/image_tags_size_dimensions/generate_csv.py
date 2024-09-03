import csv
import random
import string

def get_alt_tags():
    alt_tags = random.randint(0,1)
    return alt_tags

def get_size():
    sizes = random.randint(0,1)
    return sizes

def get_dimensions():
    dimensions = random.randint(0,1)
    return dimensions

def is_satisfied(alt_tags, sizes, dimensions):
    return alt_tags and sizes and dimensions


def generate_csv(filename, num_entries):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['is_alt_satisfied','is_size_satisfied','is_dimension_satisfied','is_satisfied']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for _ in range(num_entries):
            alt_tags = get_alt_tags()
            sizes = get_size()
            dimensions = get_dimensions()
            writer.writerow({'is_alt_satisfied': alt_tags, 'is_size_satisfied': sizes, 'is_dimension_satisfied': dimensions,'is_satisfied': is_satisfied(alt_tags, sizes, dimensions) })

def main():
    filename = "data.csv"
    num_entries = 100  # You can adjust the number of entries as needed
    generate_csv(filename, num_entries)
    print(f"CSV file '{filename}' generated successfully with {num_entries} entries.")

if __name__ == "__main__":
    main()
   
