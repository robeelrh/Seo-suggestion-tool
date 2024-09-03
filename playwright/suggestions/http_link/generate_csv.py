import csv
import random
import string

def generate_url():
    characters = string.ascii_letters + string.digits + "-_."
    url_length = random.randint(5, 15)
    url = ''.join(random.choice(characters) for _ in range(url_length))
    protocol = random.choice(["http", "https"])
    url = f"{protocol}://{url}"

    return url


def is_satisfied(url):
    if "https" in url:
        return True
    return False

def generate_csv(filename, num_entries):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['http','https','is_satisfied']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for _ in range(num_entries):
            url = generate_url()
            writer.writerow({'http': not is_satisfied(url),'https': is_satisfied(url), 'is_satisfied': is_satisfied(url)})

def main():
    filename = "data.csv"
    num_entries = 100  # You can adjust the number of entries as needed
    generate_csv(filename, num_entries)
    print(f"CSV file '{filename}' generated successfully with {num_entries} entries.")

if __name__ == "__main__":
    main()
   
