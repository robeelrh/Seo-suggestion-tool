import csv
import random
import string

def generate_doctype():
    choice = random.randint(0,1)
    return choice

def is_satisfied(doctype):
    return doctype

def generate_csv(filename, num_entries):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['doctype', 'is_satisfied']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for _ in range(num_entries):
            doctype = generate_doctype()
            writer.writerow({'doctype': doctype, 'is_satisfied':is_satisfied(doctype) })

def main():
    filename = "data.csv"
    num_entries = 100  # You can adjust the number of entries as needed
    generate_csv(filename, num_entries)
    print(f"CSV file '{filename}' generated successfully with {num_entries} entries.")

if __name__ == "__main__":
    main()
   
