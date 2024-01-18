import os

from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

from dotenv import load_dotenv

load_dotenv()

# os.environ["OPENAI_API_KEY"] = os.environ.get("OPENAI_API_KEY")

llm = ChatOpenAI(temperature=0)
prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name from a company that makes {product}?",
)

chain_var = LLMChain(llm=llm, prompt=prompt, verbose=True)

if __name__ == "__main__":
    print(chain_var.run(prompt))
