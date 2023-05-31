import os
def print_docs(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isdir(file_path):
            print("Папка:", filename)
            print_docs(file_path)
        else:
            print("Файл:", filename)
directory = r"C:\Users\Xgamerpc1038\OneDrive\Документы\GitHub\Basics_and_methodology_of_programming"
print_docs(directory)