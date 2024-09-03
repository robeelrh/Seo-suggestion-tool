import csv
import random
import string

def generate_content():
    length = random.randint(0,100)
    content = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return content

def is_empty(content):
    content_length = len(content)
    return 0 if content_length > 0 else 1

def generate_csv(filename, num_entries):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['content_length', 'is_empty']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for _ in range(num_entries):
            content =generate_content()
            writer.writerow({'content_length': len(content), 'is_empty': is_empty(content)})

def main():
    filename = "data.csv"
    num_entries = 100  # You can adjust the number of entries as needed
    generate_csv(filename, num_entries)
    print(f"CSV file '{filename}' generated successfully with {num_entries} entries.")

if __name__ == "__main__":
    main()
   
