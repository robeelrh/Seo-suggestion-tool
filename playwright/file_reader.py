from docx import Document
import os

def read_docx(file_path):
    try:

        absolute_path = os.path.abspath(file_path)
        print(f"Attempting to read from: {absolute_path}")

        # Attempt to open the file to see if it is locked
        with open(file_path, 'rb') as f:
            print("File can be accessed and is not locked.")

        # If successful, load the document
        doc = Document(absolute_path)
        print(doc)

        # Read and print each paragraph in the document
        for para in doc.paragraphs:
            print(para.text)

    except PermissionError:
        print(f"Permission denied: Unable to access {file_path}. The file may be open in another program or locked.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Replace 'your_file.docx' with the path to the DOCX file you want to read
file_path = 'Avtale_Erfaneh.docx'
read_docx(file_path)