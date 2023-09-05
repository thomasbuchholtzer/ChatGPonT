from io import StringIO
import os
import fitz
import openai
from dotenv import load_dotenv
from nltk.tokenize import sent_tokenize

load_dotenv()


def open_file(filepath):
    with open(filepath, "r", encoding="utf-8") as infile:
        return infile.read()


openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = os.getenv("OPENAI_ORGANIZATION")


def read_pdf(filename):
    context = ""

    # Open the PDF file
    with fitz.open(filename) as pdf_file:
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


filename = os.path.join(os.path.dirname(__file__), "filename.pdf")
document = read_pdf(filename)


# Ask ChatGPT and print the answer
def ask_chatGPT(prompts):
    messages = [{"role": "user", "content": prompt} for prompt in prompts]
    responses = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages
    )
    # response["choices"][0]["message"]["content"]
    return [response["message"]["content"] for response in responses["choices"]]


# print(ask_chatGPT(["Who are you ?"]))

def ask_question_to_pdf(question, txtinput=document):
    return ask_chatGPT([question + " : " + txtinput])

# print(ask_question_to_pdf("Please summarize the following text"))