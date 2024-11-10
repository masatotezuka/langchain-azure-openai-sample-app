from src.lib.llm import azure_llm


json_llm = azure_llm.bind(response_format={"type": "json_object"})

res = json_llm.invoke(
    "Return a JSON object with key 'random_ints' and a value of 10 random ints in [0-99]"
)
print(res.content)
