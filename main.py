from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

import settings

documents = [
    Document(
        page_content="Dogs are great companions, known for their loyalty and friendliness.",
        metadata={"source": "mammal-pets-doc"},
    ),
    Document(
        page_content="Cats are independent pets that often enjoy their own space.",
        metadata={"source": "mammal-pets-doc"},
    ),
]

file_path = settings.BASE_DIR + "/example_data/nke-10k-2023.pdf"
loader = PyPDFLoader(file_path)
docs = loader.load()

print(f"Loaded {len(docs)} documents from the PDF.")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    add_start_index=True,
)
docs = text_splitter.split_documents(docs)

print(f"Number of documents after splitting: {len(docs)}")
print(f"First document content preview: {docs[0].page_content[:200]}...")
print(f"First document metadata: {docs[0].metadata}")