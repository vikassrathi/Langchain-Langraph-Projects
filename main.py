from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
load_dotenv()



def main():
    print("Hello from langchain-langraph-projects!")
    person_name='Narendra Modi'
    summary_template = """
    1. Give information {person_name} i am asking for
    2. Give concise and brief summary of the person.
    """
    summary_prompt = PromptTemplate(input_variables=['person_name'], template=summary_template)
    llm=ChatOllama(temperature=0,model="gemma3:270m")
    chain = summary_prompt | llm
    response=chain.invoke(input={"person_name": person_name})
    print(response.content)

if __name__ == "__main__":
    main()
