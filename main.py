from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document

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
pdf_documents = loader.load()

print(f"Loaded {len(pdf_documents)} documents from the PDF.")
print(f"First document content preview: {pdf_documents[0].page_content[:200]}...")
print(f"First document metadata: {pdf_documents[0].metadata}")