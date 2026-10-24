from app.services.ingestion import chunk_documents
import chunk
from app.services.ingestion import load_file
from pathlib import Path
from app.rag.vectorstore import add_documents

docs=load_file(Path("/Users/saurabhrai/Desktop/IT_SUPPORT_COPILOT/data/sample_kb/company_it_handbook.md"))
chunks=chunk_documents(docs)
add_documents(chunks)