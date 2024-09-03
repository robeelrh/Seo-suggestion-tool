import csv
import random
import string

def get_og_image():
    length = random.randint(0,5)
    image_link = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return image_link

def get_og_type():
    length = random.randint(0,5)
    type = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return type

def get_og_title():
    length = random.randint(0,5)
    title = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return title

def get_og_description():
    length = random.randint(0,5)
    description = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return description

def get_og_locale():
    length = random.randint(0,5)
    locale = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return locale


def is_satisfied(og_image, og_type, og_title, og_description, og_locale):
    if len(og_image) > 0 and len(og_type) > 0 and len(og_title) > 0 and len(og_description) > 0 and len(og_locale) > 0:
        return True
    return False


def generate_csv(filename, num_entries):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['og_image','og_type','og_title','og_description', 'og_locale', 'is_satisfied']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for _ in range(num_entries):
            og_image = get_og_image()
            og_type = get_og_type()
            og_title = get_og_title()
            og_description = get_og_description()
            og_locale = get_og_locale()
            writer.writerow({'og_image': len(og_image) > 0, 'og_type': len(og_type) > 0, 'og_title': len(og_title) > 0,'og_description': len(og_description) > 0, "og_locale":len(og_locale) > 0, 'is_satisfied': is_satisfied(og_image, og_type, og_title, og_description, og_locale)})

def main():
    filename = "data.csv"
    num_entries = 100  # You can adjust the number of entries as needed
    generate_csv(filename, num_entries)
    print(f"CSV file '{filename}' generated successfully with {num_entries} entries.")

if __name__ == "__main__":
    main()
   
