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



# demo_text = """In topology, knot theory is the study of mathematical knots. While inspired by knots which appear in daily life, such as those in shoelaces and rope, a mathematical knot differs in that the ends are joined so it cannot be undone, the simplest knot being a ring (or "unknot"). In mathematical language, a knot is an embedding of a circle in 3-dimensional Euclidean space, R 3 \mathbb {R} ^{3}. Two mathematical knots are equivalent if one can be transformed into the other via a deformation of R 3 \mathbb {R} ^{3} upon itself (known as an ambient isotopy); these transformations correspond to manipulations of a knotted string that do not involve cutting it or passing it through itself.
# Knots can be described in various ways. Using different description methods, there may be more than one description of the same knot. For example, a common method of describing a knot is a planar diagram called a knot diagram, in which any knot can be drawn in many different ways. Therefore, a fundamental problem in knot theory is determining when two descriptions represent the same knot.
# A complete algorithmic solution to this problem exists, which has unknown complexity.[citation needed] In practice, knots are often distinguished using a knot invariant, a "quantity" which is the same when computed from different descriptions of a knot. Important invariants include knot polynomials, knot groups, and hyperbolic invariants.
# The original motivation for the founders of knot theory was to create a table of knots and links, which are knots of several components entangled with each other. More than six billion knots and links have been tabulated since the beginnings of knot theory in the 19th century.
# To gain further insight, mathematicians have generalized the knot concept in several ways. Knots can be considered in other three-dimensional spaces and objects other than circles can be used; see knot (mathematics). For example, a higher-dimensional knot is an n-dimensional sphere embedded in (n+2)-dimensional Euclidean space. """


# Knot theory is the study of mathematical knots, which are different from the knots we encounter in everyday life. A mathematical knot is an embedding of a circle in 3-dimensional Euclidean space, where the ends are joined and cannot be undone. Knots can be described in various ways, and a fundamental problem in knot theory is determining when two descriptions represent the same knot. Knot invariants, such as knot polynomials, knot groups, and hyperbolic invariants, are used to distinguish knots. The founders of knot theory originally aimed to create a table of knots and links, which are knots of multiple components entangled with each other. Mathematicians have also generalized the concept of knots to include objects other than circles and other three-dimensional spaces.
# Knot theory is a branch of topology that studies mathematical knots. A mathematical knot is different from a regular knot in that its ends are joined and it cannot be undone. Knots can be represented as circles embedded in 3-dimensional space. Two knots are considered equivalent if one can be transformed into the other through deformation of the space. Knots can be described in various ways, and determining when two descriptions represent the same knot is a fundamental problem in knot theory. There is an algorithmic solution to this problem, but its complexity is unknown. Knot invariants, such as knot polynomials and hyperbolic invariants, are used to distinguish knots. The original motivation for knot theory was to create a table of knots and links, which are knots with multiple components. Mathematicians have also generalized the concept of knots to consider other three-dimensional spaces and objects. An example is higher-dimensional knots, which are spheres embedded in higher-dimensional space.
