import csv
import random
import string

def get_primary():
    primary_keywords = random.randint(0,5)
    return primary_keywords


def is_satisfied(primary, secondary):
    return primary and secondary


def generate_csv(filename, num_entries):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['no_of_primary_keywords','is_primary_satisfied','is_secondary_satisfied','is_satisfied']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for _ in range(num_entries):
            no_of_primary = get_primary()
            primary = 1 if no_of_primary > 0 else 0
            secondary = random.randint(0,1) # for the time being
            writer.writerow({'no_of_primary_keywords': no_of_primary, 'is_primary_satisfied': primary, 'is_secondary_satisfied': secondary,'is_satisfied': is_satisfied(primary,secondary)})

def main():
    filename = "data.csv"
    num_entries = 100  # You can adjust the number of entries as needed
    generate_csv(filename, num_entries)
    print(f"CSV file '{filename}' generated successfully with {num_entries} entries.")

if __name__ == "__main__":
    main()
   
