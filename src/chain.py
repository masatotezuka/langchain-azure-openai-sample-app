from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from src.lib.llm import azure_llm

prompt = ChatPromptTemplate.from_template(
    "{target}に最も人気な職業をは?\n職業：",
)
second_prompt = ChatPromptTemplate.from_template(
    "{job}の平均年収を教えて",
)
chain = prompt | azure_llm | StrOutputParser()
composed_chain = (
    chain
    | (lambda input: {"job": input})
    | second_prompt
    | azure_llm
    | StrOutputParser()
)
print(composed_chain.invoke({"target": "男性"}))
