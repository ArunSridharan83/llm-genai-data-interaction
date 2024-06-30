import chromadb
import warnings
import openai
from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.question_answering import load_qa_chain
from langchain_openai import OpenAIEmbeddings
from langchain_openai import OpenAI
from chromadb.utils import embedding_functions
from langchain_community.vectorstores import Chroma
import os

os.environ["OPENAI_API_KEY"] = "replace-with-openai-key"
persist_directory='change-to-db-path'

index_name = "langchain"
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
vectorstore = Chroma(persist_directory=persist_directory, embedding_function=embeddings)


def get_similiar_docs(query, k=1, score=False):  # we can control k value to get no. of context with respect to question.
  if score:
    similar_docs = vectorstore.similarity_search_with_score(query, k=k)
  else:
    similar_docs = vectorstore.similarity_search(query, k=k)
  print (similar_docs)
  return similar_docs

def get_answer(query):
  chain = load_qa_chain(OpenAI(temperature=0), chain_type="map_reduce")
  similar_docs = get_similiar_docs(query)
  input_data = {
    'input_documents': similar_docs,
    'question': query,
}
  answer = chain.invoke(input=input_data)
  return answer


running = 1
while running == 1:
    query = input('Enter your Question ?  : ')
    if query == 'exit':
        break
    answer = get_answer(query)
    print(answer['output_text'])
