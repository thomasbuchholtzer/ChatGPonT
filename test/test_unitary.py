# from io import StringIO
import os
import fitz
import openai
from dotenv import load_dotenv
import pytest

# from nltk.tokenize import sent_tokenize

load_dotenv()


def open_file(filepath):
    with open(filepath, "r", encoding="utf-8") as infile:
        return infile.read()


openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = os.getenv("OPENAI_ORGANIZATION")


# File read functions
def read_pdf(file):
    context = ""

    # Open the PDF file
    with fitz.open(file) as pdf_file:
        # Get the number of pages in the PDF file
        num_pages = pdf_file.page_count

        # Loop through each page in the PDF file
        for page_num in range(num_pages):
            # Get the current page
            page = pdf_file[page_num]

            # Get the text from the current page
            page_text = page.get_text().replace("\n", "")

            # Append the text to context
            context += page_text
    return context


def read_txt(file):
    context = ""
    with open(file) as txt_file:
        context = txt_file.read()
    return context


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
        raise Exception("Wrong filetype")


# Ask ChatGPT and print the answer


def ask_chatGPT(prompts):
    messages = [{"role": "user", "content": prompt} for prompt in prompts]
    responses = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613", messages=messages
    )
    # response["choices"][0]["message"]["content"]
    return [response["message"]["content"]
            for response in responses["choices"]]


# print(ask_chatGPT(["Who are you ?"]))


dirname_1 = "courses"
filename_1 = "napoleon.txt"

dirname_2 = "courses"
filename_2 = "filename.pdf"

dirname_3 = "courses"
filename_3 = "logo.jpg"


def ask_question_to_pdf(question, txtinput=read_doc(dirname_1, filename_1)):
    return ask_chatGPT([question + " : " + txtinput])


# print(ask_question_to_pdf("Please summarize the following text"))


def test_read_doc():
    assert type(read_doc(dirname_1, filename_1)) == str
    assert type(read_doc(dirname_2, filename_2)) == str

    with pytest.raises(Exception) as excinfo:
        read_doc(dirname_3, filename_3)

    assert "Wrong filetype" in str(excinfo.value)
