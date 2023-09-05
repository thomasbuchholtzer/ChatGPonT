# import openai
# import json


# # Example dummy function hard coded to return the same weather
# # In production, this could be your backend API or an external API
# def get_current_weather(location, unit="fahrenheit"):
#     """Get the current weather in a given location"""
#     weather_info = {
#         "location": location,
#         "temperature": "72",
#         "unit": unit,
#         "forecast": ["sunny", "windy"],
#     }
#     return json.dumps(weather_info)


# def run_conversation():
#     # Step 1: send the conversation and available functions to GPT
#     messages = [{"role": "user", "content": "What's the weather like in Boston?"}]
#     functions = [
#         {
#             "name": "get_current_weather",
#             "description": "Get the current weather in a given location",
#             "parameters": {
#                 "type": "object",
#                 "properties": {
#                     "location": {
#                         "type": "string",
#                         "description": "The city and state, e.g. San Francisco, CA",
#                     },
#                     "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
#                 },
#                 "required": ["location"],
#             },
#         }
#     ]
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo-0613",
#         messages=messages,
#         functions=functions,
#         function_call="auto",  # auto is default, but we'll be explicit
#     )
#     response_message = response["choices"][0]["message"]
#     response_message

#     # Step 2: check if GPT wanted to call a function
#     if response_message.get("function_call"):
#         # Step 3: call the function
#         # Note: the JSON response may not always be valid; be sure to handle errors
#         available_functions = {
#             "get_current_weather": get_current_weather,
#         }  # only one function in this example, but you can have multiple
#         function_name = response_message["function_call"]["name"]
#         fuction_to_call = available_functions[function_name]
#         function_args = json.loads(response_message["function_call"]["arguments"])
#         function_response = fuction_to_call(
#             location=function_args.get("location"),
#             unit=function_args.get("unit"),
#         )

#         # Step 4: send the info on the function call and function response to GPT
#         messages.append(response_message)  # extend conversation with assistant's reply
#         messages.append(
#             {
#                 "role": "function",
#                 "name": function_name,
#                 "content": function_response,
#             }
#         )  # extend conversation with function response
#         second_response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo-0613",
#             messages=messages,
#         )  # get a new response from GPT where it can see the function response
#         return second_response


# print(run_conversation())

# ------

# def split_text(text, chunk_size=5000):
#     """
#     Splits the given text into chunks of approximately the specified chunk size.
#     Args:
#     text (str): The text to split.
#     chunk_size (int): The desired size of each chunk (in characters).
#     Returns:
#     List[str]: A list of chunks, each of approximately the specified chunk size.
#     """

#     chunks = []
#     current_chunk = StringIO()
#     current_size = 0
#     sentences = sent_tokenize(text)
#     for sentence in sentences:
#         sentence_size = len(sentence)
#         if sentence_size > chunk_size:
#             while sentence_size > chunk_size:
#                 chunk = sentence[:chunk_size]
#                 chunks.append(chunk)
#                 sentence = sentence[chunk_size:]
#                 sentence_size -= chunk_size
#                 current_chunk = StringIO()
#                 current_size = 0
#         if current_size + sentence_size < chunk_size:
#             current_chunk.write(sentence)
#             current_size += sentence_size
#         else:
#             chunks.append(current_chunk.getvalue())
#             current_chunk = StringIO()
#             current_chunk.write(sentence)
#             current_size = sentence_size
#     if current_chunk:
#         chunks.append(current_chunk.getvalue())
#     return chunks

# chunks = split_text(document)

# Knot theory is the study of mathematical knots, which are different from the knots we encounter in everyday life. A mathematical knot is an embedding of a circle in 3-dimensional Euclidean space, where the ends are joined and cannot be undone. Knots can be described in various ways, and a fundamental problem in knot theory is determining when two descriptions represent the same knot. Knot invariants, such as knot polynomials, knot groups, and hyperbolic invariants, are used to distinguish knots. The founders of knot theory originally aimed to create a table of knots and links, which are knots of multiple components entangled with each other. Mathematicians have also generalized the concept of knots to include objects other than circles and other three-dimensional spaces.
# Knot theory is a branch of topology that studies mathematical knots. A mathematical knot is different from a regular knot in that its ends are joined and it cannot be undone. Knots can be represented as circles embedded in 3-dimensional space. Two knots are considered equivalent if one can be transformed into the other through deformation of the space. Knots can be described in various ways, and determining when two descriptions represent the same knot is a fundamental problem in knot theory. There is an algorithmic solution to this problem, but its complexity is unknown. Knot invariants, such as knot polynomials and hyperbolic invariants, are used to distinguish knots. The original motivation for knot theory was to create a table of knots and links, which are knots with multiple components. Mathematicians have also generalized the concept of knots to consider other three-dimensional spaces and objects. An example is higher-dimensional knots, which are spheres embedded in higher-dimensional space.
