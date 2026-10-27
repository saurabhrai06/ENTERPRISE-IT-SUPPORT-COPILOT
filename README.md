Enterprise IT Support Copilot 🤖

Agentic RAG | FastAPI | LangGraph | Groq | Pinecone | Docker

An AI-powered IT support assistant that retrieves information from private company knowledge-base documents to answer IT-related questions. It uses an agentic Retrieval-Augmented Generation (RAG) workflow to route questions, retrieve relevant documents, evaluate evidence, and generate grounded responses.

The application can fall back to external web search when the private knowledge base does not contain sufficient evidence.

⸻

📌 Overview

Enterprise IT teams frequently handle repetitive questions about password resets, VPN access, MFA, software installation, laptop configuration, and troubleshooting.

The Enterprise IT Support Copilot aims to simplify this process by allowing users to ask IT support questions in natural language.

Instead of relying entirely on an LLM’s internal knowledge, the application retrieves relevant information from a private knowledge base using vector search.

If the retrieved evidence is insufficient, the agent can search the web and evaluate whether the external information is sufficient to answer the question.

Key Objectives

* Automate repetitive IT support queries.
* Retrieve relevant information from internal documentation.
* Generate answers grounded in available evidence.
* Reduce unsupported or fabricated responses.
* Provide an extensible foundation for enterprise IT support automation.

⸻

✨ Features

* Agentic RAG Workflow: Uses LangGraph to orchestrate routing, retrieval, evidence grading, and answer generation.
* Private Knowledge Base: Retrieves information from indexed company documentation.
* Semantic Search: Uses Hugging Face sentence embeddings and Pinecone vector search.
* Intelligent Routing: Directs greetings to a simple response path and IT-related questions to knowledge retrieval.
* Evidence Evaluation: Evaluates whether retrieved documents sufficiently answer the question.
* Web Search Fallback: Uses Tavily when private knowledge-base evidence is insufficient.
* Query Rewriting: Rewrites queries to improve retrieval and search relevance.
* Source Citations: Returns source information for private knowledge-base answers and external search results.
* Interactive Web Interface: Provides a chat interface for asking IT support questions.
* Document Ingestion: Loads, chunks, and indexes supported knowledge-base files.
* REST API: Exposes application functionality through FastAPI.
* Interactive API Documentation: Supports API exploration through Swagger UI.
* Docker Support: Includes a Dockerfile for containerized deployment.

⸻

🏗️ Architecture

                    User Question
                          |
                          v
                  FastAPI Application
                          |
                          v
                  LangGraph Workflow
                          |
                          v
                   Question Router
                          |
              +-----------+-----------+
              |                       |
              v                       v
         Direct Answer          Private KB Retrieval
                                      |
                                      v
                               Pinecone Search
                                      |
                                      v
                                Evidence Grading
                                      |
                           +----------+----------+
                           |                     |
                      Sufficient              Insufficient
                           |                     |
                           v                     v
                    Generate from KB        Tavily Web Search
                                                 |
                                                 v
                                           Evidence Grading
                                                 |
                                                 v
                                         Generate Web Answer

Knowledge-Base Ingestion

Company Documents
       |
       v
Document Loading
       |
       v
Text Chunking
       |
       v
Hugging Face Embeddings
       |
       v
Pinecone Vector Index
       |
       v
Semantic Retrieval

The ingestion pipeline prepares documents for semantic retrieval. At query time, the workflow retrieves relevant chunks and passes the available evidence to the LLM.

⸻

🛠️ Tech Stack

Technology	Purpose
Python	Application development
FastAPI	Backend and REST API
LangGraph	Agent workflow orchestration
LangChain	LLM and retrieval integrations
Groq	LLM inference
Hugging Face Sentence Transformers	Local text embeddings
Pinecone	Vector database and semantic search
Tavily	External web search fallback
Pydantic Settings	Environment-based configuration
Jinja2	HTML template rendering
HTML, CSS, JavaScript	Frontend interface
Docker	Containerization
Git and GitHub	Version control and source hosting

Embedding Model

sentence-transformers/all-MiniLM-L6-v2

The model generates 384-dimensional embeddings for semantic document retrieval.

⸻

📂 Project Structure

IT_SUPPORT_COPILOT/
│
├── app/
│   ├── api/
│   │   └── routes.py
│   │
│   ├── core/
│   │   └── config.py
│   │
│   ├── rag/
│   │   ├── state.py
│   │   ├── vectorstore.py
│   │   └── workflow.py
│   │
│   ├── services/
│   │   └── ingestion.py
│   │
│   └── main.py
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── app.js
│
├── templates/
│   └── index.html
│
├── sample_kb/
│   └── company_it_handbook.md
│
├── Dockerfile
├── .dockerignore
├── .gitignore
├── requirements.txt
├── ingest_sample_kb.py
├── run.py
└── README.md

The structure above describes the main project components; your local repository may contain additional files.

⸻

⚙️ How It Works

1. Question Routing

The application classifies incoming questions into two broad categories:

* Direct: Greetings and casual conversation.
* Knowledge-based: IT support questions that require company documentation.

2. Document Retrieval

For knowledge-based questions, the application converts the query into an embedding and searches Pinecone for semantically relevant document chunks.

3. Evidence Grading

The retrieved documents are evaluated to determine whether they contain sufficient information to answer the original question.

4. Answer Generation

When the evidence is sufficient, the LLM generates a response grounded in the private knowledge base.

5. Web Search Fallback

If the private knowledge base is insufficient, the workflow can query Tavily for external information and evaluate the search results.

External information is distinguished from private company documentation because vendor guidance may need to be validated against internal IT policies.

6. Query Rewriting

If external search evidence remains insufficient, the workflow can rewrite the query and retry retrieval and search, subject to the configured retry limit.

⸻

🚀 Getting Started

Prerequisites

Install the following:

* Python 3.12
* Git
* A Pinecone account and API key
* A Groq API key
* A Tavily API key for web search fallback
* Docker, if you want to run the containerized application

1. Clone the Repository

git clone https://github.com/saurabhrai06/ENTERPRISE-IT-SUPPORT-COPILOT.git
cd ENTERPRISE-IT-SUPPORT-COPILOT

2. Create a Virtual Environment

On macOS or Linux:

python3.12 -m venv .venv
source .venv/bin/activate

If Python 3.12 is already installed in your environment, you can use that installation to create the virtual environment.

3. Install Dependencies

python -m pip install --upgrade pip
pip install -r requirements.txt

4. Configure Environment Variables

Create a .env file in the project root:

GROQ_API_KEY=your_groq_api_key
PINECONE_API_KEY=your_pinecone_api_key
TAVILY_API_KEY=your_tavily_api_key
PINECONE_INDEX_NAME=your_pinecone_index_name
PINECONE_NAMESPACE=your_pinecone_namespace
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2

Important: The exact environment variable names must match those defined in app/core/config.py. Add any other required settings from your configuration class.

Never commit your .env file or expose API keys in a public repository.

⸻

📚 Knowledge-Base Ingestion

The application uses a document ingestion pipeline to prepare internal documentation for retrieval.

1. Add Documents

Place your supported company knowledge-base files in the configured sample knowledge-base directory.

For example:

sample_kb/
└── company_it_handbook.md

2. Run the Ingestion Script

From the project root:

python ingest_sample_kb.py

The script loads documents, splits them into chunks, and indexes those chunks in Pinecone.

Example output:

Indexed 2 files -> 5 chunks -> 5 Pinecone vectors

The actual counts depend on the documents in the directory and the chunking configuration.

⸻

▶️ Running the Application

Start the FastAPI application:

python run.py

The application runs locally at:

http://127.0.0.1:8080

Open the URL in your browser to access the chat interface.

Interactive API Documentation

FastAPI provides Swagger UI at:

http://127.0.0.1:8080/docs

The OpenAPI schema is available at:

http://127.0.0.1:8080/openapi.json

These endpoints are useful for exploring and testing the available API routes.

⸻

🐳 Docker Deployment

The project includes a Dockerfile for containerized execution.

1. Build the Docker Image

docker build -t it-support-copilot .

2. Run the Container

docker run --env-file .env -p 8080:8080 it-support-copilot

Open the application at:

http://localhost:8080

The container uses the PORT environment variable when supplied and defaults to port 8080.

Keep API keys in runtime environment variables rather than embedding them in the Docker image.

⸻

🔐 Security Considerations

* Store API keys in environment variables.
* Exclude .env and .venv/ from Git.
* Do not expose private company documents in a public repository.
* Validate retrieved information before using it to change company-managed systems.
* Treat external web search results as untrusted input.
* Avoid executing commands or making security-sensitive changes solely because retrieved text recommends them.
* Configure authentication and access controls before exposing sensitive company information to multiple users.

This project is a foundation for an IT support assistant; deployment in a real enterprise environment requires additional security review.

⸻

🔮 Future Improvements

Potential improvements include:

* Add automated tests for API routes and RAG workflow behavior.
* Add document upload and re-indexing capabilities.
* Improve retrieval using metadata filters and relevance thresholds.
* Add observability and structured logging.
* Introduce user authentication and role-based access control.
* Track retrieval quality and answer accuracy.
* Add feedback collection for generated answers.
* Improve document citation and source attribution.
* Add CI/CD with GitHub Actions.
* Optimize model loading and memory consumption for deployment.
* Add evaluation datasets to measure retrieval and answer quality.

⸻

👨‍💻 Author

Saurabh Rai

GitHub: @saurabhrai06

⸻

📄 License

Choose and add an appropriate license before distributing or reusing this project. If no license is specified, normal copyright restrictions apply.
