import csv
import random
import string

def generate_iframe_count():
    iframe_count = random.randint(0,5)
    return iframe_count


def is_satisfied(iframe_count):
    return 1 if iframe_count > 0 else 0


def generate_csv(filename, num_entries):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['iframe_count','is_satisfied']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for _ in range(num_entries):
            iframe_count = generate_iframe_count()

            writer.writerow({'iframe_count': iframe_count, 'is_satisfied': is_satisfied(iframe_count)})

def main():
    filename = "data.csv"
    num_entries = 100  # You can adjust the number of entries as needed
    generate_csv(filename, num_entries)
    print(f"CSV file '{filename}' generated successfully with {num_entries} entries.")

if __name__ == "__main__":
    main()
   
