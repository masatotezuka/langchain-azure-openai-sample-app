from src.lib.llm import azure_llm

messages = [
    (
        "system",
        "あなたは通訳者です。日本語を英語に訳してください。",
    ),
    ("human", "こんにちは。今日はいい天気ですね。"),
]
res = azure_llm.invoke(messages)
print(res)
