**Here is a Highlevel flow of the process**

![llm-doc-interactor](https://github.com/ArunSridharan83/llm-genai-data-interaction/assets/68751492/9e910dd5-c89e-4ba6-8c68-0ba7bb6cf43a)

**Clone the repo**

git clone https://github.com/ArunSridharan83/llm-genai-data-interaction.git
Modify the following values

Modify the "change-to-data-folder" to the path where the documents are placed. documents can be of type .pdf,.txt,.csv,.doc,.docx
Modify the openaikey to your openai key. Caution:- Do not share your personal key

Execute

pip3 install openai
pip3 install langchain
pip3 install langchain_community
pip3 install unstructured
pip3 install tiktoken
pip3 install langchain_openai
pip3 install chromadb

python3 upload-vector-embeddings.py
python3 chat-with-data.py



# llm-genai-data-interaction
Python program and Langchain to interact with a rich set of documents using LLM models and Generative AI

This program is designed to load documents from a specified directory, split the documents into smaller chunks, create embeddings for these chunks using the OpenAI model "text-embedding-ada-002", and store these embeddings in a Chroma vector store. Here is a step-by-step explanation:

**Imports and Setup:**

The program imports necessary libraries: chromadb, warnings, openai, and components from the langchain library.
It sets a warning filter to ignore warnings.
The OpenAI API key is set using an environment variable.
Directory Path:

The path to the directory containing the documents is specified: 'data'.
Load Documents:

The load_docs function uses DirectoryLoader to load all documents from the specified directory.
The documents are loaded into a variable documents.

**Split Documents:**

The split_docs function takes the loaded documents and splits them into smaller chunks. This is done using RecursiveCharacterTextSplitter with a specified chunk size (1000 characters) and overlap (20 characters).
The split documents are stored in a variable docs.
Persist Directory:

The path to the directory where the Chroma database will be stored is specified: 'db'.

**Create Embeddings:**

The OpenAIEmbeddings class from langchain is used to create embeddings for the document chunks. The model used is "text-embedding-ada-002".
Create and Persist Vector Store:

The Chroma class from langchain.vectorstores is used to create a Chroma vector store from the document chunks and their embeddings.
The persist_directory specifies where the Chroma database will be stored.
The embeddings are created with a cosine similarity measure as specified by collection_metadata={"hnsw:space": "cosine"}.

Finally, the vector store is persisted using db.persist().
This process effectively prepares your document data for efficient similarity search and retrieval using embeddings, allowing for advanced text-based queries and analysis.


**Load Docuements**

This program is designed to load documents, create embeddings for them, store the embeddings in a Chroma vector store, and then allow users to query this vector store to find similar documents and get answers to questions based on the content of these documents. Here’s a detailed explanation:

**Imports and Setup:**

The program imports necessary libraries: chromadb, warnings, openai, and components from the langchain library.
It sets the OpenAI API key using an environment variable.
Persist Directory:

The path to the directory where the Chroma database will be stored is specified: '/Users/asridharan/Desktop/LLM/myprojects/chroma/db'.
Index Name and Embeddings:

The name of the index is set to "langchain".
The OpenAIEmbeddings class is used to create embeddings for the document chunks. The model used is "text-embedding-ada-002".
A Chroma vector store instance is created with the specified persist directory and embedding function.
Similarity Search Functions:

get_similar_docs: This function takes a query and an optional parameter k (number of similar documents to return) and an optional score parameter (whether to return similarity scores). It uses the Chroma vector store to perform a similarity search.
get_answer: This function takes a query, retrieves similar documents using get_similar_docs, and then uses a question-answering chain to generate an answer based on the similar documents. It uses the map_reduce chain type from langchain with an OpenAI model that has a temperature setting of 0 (to minimize randomness in the response).
Interactive Loop:

The program enters an interactive loop where it repeatedly prompts the user to enter a question.
If the user enters "exit", the loop breaks and the program ends.

For any other query, the program calls get_answer to retrieve an answer based on the documents stored in the vector store.
The retrieved answer is printed to the console.
Here is a breakdown of the interactive loop:

Input Query: The user is prompted to enter a question.
Exit Condition: If the query is "exit", the loop terminates.
Get Answer: For any other query, the get_answer function is called.
Similarity Search: Within get_answer, get_similar_docs is called to find documents similar to the query.
Load QA Chain: A QA chain is loaded using an OpenAI model.
Invoke Chain: The QA chain is invoked with the similar documents and the query to generate an answer.
Output Answer: The answer is printed to the console.

This program allows for interactive question-answering based on the content of documents stored in a vector store, leveraging OpenAI embeddings and the langchain library.
