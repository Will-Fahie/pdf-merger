import PyPDF2
import os
import sys


# grabs all pdf file paths
def get_pdfs(num):
    paths = []
    for i in range(num):
        file_path = input("Enter PDF file path: ")
        paths.append(file_path)
    return paths


# loops through and merges all pdfs into single file
def pdf_merger(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        if not os.path.exists(pdf):
            print(f"{pdf} does not exist")
        else:
            merger.append(pdf)
            print(f"{pdf} has been merged")
    merger.write("merged.pdf")


if __name__ == "__main__":

    # checks whether file paths are already given as arguments
    if len(sys.argv) > 1:
        file_paths = sys.argv[1:]
        pdf_merger(file_paths)

    # if not, asks user for them
    else:
        # loops until a valid number is received
        while True:
            try:
                # gets number of pdfs
                num_pdf = int(input("How many PDFs would you like to merge? "))
                # gets pdf file paths
                file_paths = get_pdfs(num_pdf)
                # merges pdf files
                pdf_merger(file_paths)
                break
            except ValueError:
                print("Not a valid number")
