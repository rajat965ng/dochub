# Doc Hub

Doc Hub is a sophisticated Python 3.11 application that leverages the Retrieval-Augmented Generation (RAG) approach to efficiently query documents stored in a vector database. Designed for users who require deep insights from large text datasets, Doc Hub interprets and responds to user queries by dynamically sourcing information from embedded document vectors.

## Features

- **Document Ingestor**: Splits text from PDF documents into chunks, transforms these chunks into vectors, and stores them in Pinecone Vector DB.
- **Query Utils**: Handles the QA chain that processes user inputs into vectors, enriching the query context before fetching the final response from an LLM.
- **Frontend Application**: Built with Streamlit, this interface allows users to interact seamlessly with the backend Query Utils, providing an intuitive platform for querying and obtaining answers.

## Tech Stack

- **Python 3.11**: The core programming language.
- **Poetry**: Used for dependency management and build processes.
- **LangChain Framework**: Facilitates the integration of LLM functionalities.
- **Pinecone Vector DB**: Manages the storage and retrieval of vector data.
- **OpenAI LLM**: Powers the intelligent response generation based on vector inputs.
- **Streamlit**: Creates an engaging and interactive user interface.

## Getting Started

Follow these instructions to set up your local development environment.

### Prerequisites

- Install Python 3.11
- Obtain API keys for Pinecone and OpenAI services

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/rajat965ng/dochub.git
   ```
2. Navigate to the project directory:
   ```bash
   cd dochub
   ```
3. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

### Running the Application

Activate the virtual environment and start the Streamlit server:
```bash
poetry shell
poetry run streamlit run frontend/frontend/app.py
```

## Contributing

We welcome contributions to make Doc Hub even better. Here's how you can contribute:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/YourAmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some YourAmazingFeature'`)
4. Push to the Branch (`git push origin feature/YourAmazingFeature`)
5. Open a Pull Request

## Author

**Rajat Nigam**

- [LinkedIn Profile](https://www.linkedin.com/in/rajat-nigam-877208127/)

## Project Link

- [Doc Hub on GitHub](https://github.com/rajat965ng/dochub)

## Acknowledgements

- [OpenAI](https://openai.com/)
- [Pinecone](https://www.pinecone.io/)
- [Streamlit](https://streamlit.io/)
```

This `README.md` provides a comprehensive overview of your project including how to get started, the technology used, and how others can contribute. Modify the licensing and any other project-specific details as needed.