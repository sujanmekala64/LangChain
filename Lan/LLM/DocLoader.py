from langchain_ollama import ChatOllama 
from dotenv import load_dotenv 
from langchain_core.output_parsers import StrOutputParser 
from langchain_core.prompts import PromptTemplate 
from langchain_community.document_loaders import TextLoader 
from langchain_core.runnables import RunnableSequence 
import os
load_dotenv() 
llm = ChatOllama(
    model="gpt-oss:20b-cloud",
    base_url = os.getenv("OLLAMA_BASE_URL"),
    headers = {"Authorization":f"Bearer {os.getenv("OLLAMA_API_KEY")}"}
)
Loader = TextLoader('cricket.txt')
docs = Loader.load()  
prompt = PromptTemplate(
    template = "Who is the best player from the given {text}, give it in only one line",
    input_varaibles=['text'] 
)
parser=StrOutputParser() 
chain = RunnableSequence(prompt,llm,parser) 
res=chain.invoke({'text':docs[0].page_content})
print(res) 
# print(docs[0].page_content)
# print(llm.invoke("Hi"))