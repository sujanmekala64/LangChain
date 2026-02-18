from langchain_ollama import ChatOllama 
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnablePassthrough, RunnableParallel
from dotenv import load_dotenv 
import os 
load_dotenv() 
llm = ChatOllama(
    model="gpt-oss:20b-cloud",
    base_url = os.getenv("OLLAMA_BASE_URL"),
    headers={"Authorization":f"Bearer {os.getenv("OLLAMA_API_KEY")}"}
)
prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables = ['topic'] 
)
prompt2 = PromptTemplate(
    template='Explain the following Joke - {text}',
    input_variables=['text']
)
parser=StrOutputParser()
# chain=RunnableSequence(prompt1,llm,parser,prompt2,llm,parser)
# output=chain.invoke({'topic':'Deep Learning'})
joke_chain=RunnableSequence(prompt1,llm,parser)
parallel_chain =RunnableParallel({
    'joke':RunnablePassthrough(),
    'explanation':RunnableSequence(prompt2,llm,parser)
})
chain=RunnableSequence(joke_chain,parallel_chain) 
op1=chain.invoke({'topic':'AI'})
print(op1['joke'])
# output=llm.invoke("Who is IPL 2022 Champions")
# print(output.content)