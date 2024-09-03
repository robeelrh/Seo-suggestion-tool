import csv
import random
import string

def get_links():
    alt_tags = random.randint(40000-100,40000+100)
    return alt_tags

def get_sizes():
    sizes = random.randint(40000000-100, 40000000 + 100)
    return sizes

def is_satisfied(links, sizes):
    return 1 if links < 40000 and sizes < 40000000 else 0


def generate_csv(filename, num_entries):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['no_of_links','size','is_satisfied']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for _ in range(num_entries):
            links = get_links()
            sizes = get_sizes()
            writer.writerow({'no_of_links': links, 'size': sizes, 'is_satisfied': is_satisfied(links,sizes) })

def main():
    filename = "data.csv"
    num_entries = 100  # You can adjust the number of entries as needed
    generate_csv(filename, num_entries)
    print(f"CSV file '{filename}' generated successfully with {num_entries} entries.")

if __name__ == "__main__":
    main()
   
