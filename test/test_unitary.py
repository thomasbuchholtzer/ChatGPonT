# from io import StringIO
import os

# Course filename and reading
dirname_ex = "courses"
filename_ex = "napoleon.txt"

def read_doc(dirname, filename):
    file = os.path.join(
        os.path.join(os.path.dirname(__file__), dirname), filename)
    _, file_extension = os.path.splitext(file)

    if file_extension == ".pdf":
        document = read_pdf(file)
        return document
    elif file_extension == ".txt":
        document = read_txt(file)
        return document
    else:
        raise Exception("Error : Unsupported filetype for given resource")

def test_read_doc():
    assert type(read_doc(dirname_ex, filename_ex)) == str
