from dotenv import load_dotenv
import os
import json
from openai import OpenAI

load_dotenv()

# check if the API key is being load
# print(os.getenv("OPENAI_API_KEY"))

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def get_weather(location):
    return f"The weather in {location} is sunny with a high of minus 25 degree Celsius"

def get_news(topic):
    return f"The latest news about {topic} is that it's trending worldwide  "

tools = [
    {
        "type": "function",
        "function": {
            "name" : "get_weather",
            "description": "get the current weather for a given location.",
            "parameters":{
                "type":"object",
                "properties":{
                    "location":{
                        "type":"string",
                        "description":"The name of the location to get the weather for."
                    }
                },
                "required":["location"]
            }
        }
    },
    {
       "type":"function",
       "function": {
           "name": "get_news",
           "description": "Get the latest news headlines.",
           "parameters":{
               "type":"object",
               "properties":{
                   "topic":{
                       "type":"string",
                       "description": "The topic to get news about "
                   }
                   
               },
               "required":["topic"]
           }
       } 
    }
]

messages = [
    {"role":"system", "content":"You are a helpful assistant."},
    {"role":"user", "content":"What's the recent weather in India?"} # change here for any single task i.e withing the tool call function (get_nnews/get_weather)
]

# messages = [
#     {
#         "role": "system",
#         "content": (
#             "You are a helpful assistant. "
#             "When a tool returns information, answer ONLY using the tool output. "
#             "Do not add extra facts or assumptions."
#         )
#     },
#     {
#         "role": "user",
#         "content": "What's the weather like in India?"
#     }
# ]


response = client.chat.completions.create(
    # model = "gpt-4o-mini",
    # model="llama-3.1-8b-instant",
    model="llama-3.3-70b-versatile",
    messages= messages,
    tools = tools,
    tool_choice = "auto"   #means it can either respond with text message or with tool calls (client side)
)

message = response.choices[0].message

print(message.tool_calls)

if message.tool_calls:
    tool_call = message.tool_calls[0]
    if tool_call.function.name == "get_weather":
        # args = eval(tool_call.function.arguments)
        args = json.loads(tool_call.function.arguments)
        weather_info = get_weather(args["location"])
        print(weather_info)
        # messages.append(message)
        # messages.append(message.model_dump())
        messages.append({
    "role": "assistant",
    "content": message.content,
    "tool_calls": [
        {
            "id": tool_call.id,
            "type": "function",
            "function": {
                "name": tool_call.function.name,
                "arguments": tool_call.function.arguments
            }
        }
    ]
})
        messages.append({
            "role" :"tool",
            "tool_call_id":tool_call.id,
            "name":"get_weather",
            "content":weather_info
        })
        final_response = client.chat.completions.create(
            # model="llama-3.1-8b-instant",
            model="llama-3.3-70b-versatile",
            messages = messages
        )
        print(final_response.choices[0].message.content)

    elif tool_call.function.name == "get_news":
        args = json.loads(tool_call.function.arguments)
        news_info = get_news(args["topic"])
        print(news_info)
                # messages.append(message)
                # messages.append(message.model_dump())
        messages.append({
    "role": "assistant",
    "content": message.content,
    "tool_calls": [
        {
            "id": tool_call.id,
            "type": "function",
            "function": {
                "name": tool_call.function.name,
                "arguments": tool_call.function.arguments
            }
        }
    ]
})
        messages.append({
            "role" :"tool",
            "tool_call_id":tool_call.id,
            "name":"get_news",
            "content":news_info
        })
        final_response = client.chat.completions.create(
            # model="llama-3.1-8b-instant",
            model="llama-3.3-70b-versatile",
            messages = messages
        )
        print(final_response.choices[0].message.content)    

else:
    print(message.content)



















# available_tools = {
#     "get_weather": get_weather,
#     "get_news": get_news
# }



# for tool_call in message.tool_calls:

#     function_name = tool_call.function.name

#     function = available_tools.get(function_name)

#     args = json.loads(tool_call.function.arguments)

#     result = function(**args)

#     messages.append({
#         "role": "assistant",
#         "content": None,
#         "tool_calls": [{
#             "id": tool_call.id,
#             "type": "function",
#             "function": {
#                 "name": function_name,
#                 "arguments": tool_call.function.arguments
#             }
#         }]
#     })

#     messages.append({
#         "role": "tool",
#         "tool_call_id": tool_call.id,
#         "name": function_name,
#         "content": result
#     })






# final_response = client.chat.completions.create(
#     model="llama-3.3-70b-versatile",
#     messages=messages
# )

# print(final_response.choices[0].message.content)



