import os
import fitz
import openai
from dotenv import load_dotenv

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


# Course filename and reading
dirname_ex = "courses"


def read_doc(dirname, filename):
    file = os.path.join(os.path.join(os.path.dirname(__file__), \
                                     dirname), filename)
    _, file_extension = os.path.splitext(file)

    if file_extension == ".pdf":
        document = read_pdf(file)
        return document
    elif file_extension == ".txt":
        document = read_txt(file)
        return document
    else:
        raise Exception("Error : Unsupported filetype")


# Ask ChatGPT and print the answer


def ask_chatGPT(prompts):
    messages = [{"role": "user", "content": prompt} for prompt in prompts]
    responses = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613", messages=messages
    )
    # response["choices"][0]["message"]["content"]
    return [response["message"]["content"] for response in responses["choices"]]


# print(ask_chatGPT(["Who are you ?"]))


def ask_question_to_pdf(question, curfilename, dirname=dirname_ex):
    txtinput = read_doc(dirname, curfilename)
    return ask_chatGPT([question + " : \" " + txtinput + " \" "])


# print(ask_question_to_pdf("Please summarize the following text"))
