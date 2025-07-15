# PDF Summary Model

This project provides an AI-powered service to generate summaries from PDF documents using **Cohere API** as the NLP agent.

The project is designed to be **modular, clean, and easy to maintain**, allowing seamless integration with external services like Cohere.

---

## 📁 Project Structure

Below is a detailed explanation of each folder and its purpose:

### ─ `models/`
Responsible for defining any local ML or DL models (if needed).

- `__init__.py`  
  Makes this folder a Python module.
- `model.py`  
  Can be used to define local model classes, load them, or add any pre/post-processing logic for model predictions.
---

### ─ `services/`
Handles integration with external APIs and services.

- `__init__.py`  
  Initializes the `services` module.
- `cohere_service.py`  
  Contains:
  - Initialization and authentication with Cohere.
  - Functions to call Cohere endpoints (e.g., summarization, embeddings).
  - Logic to parse and return the response in a clean format.

---

### ─ `utils/`
Provides helper utilities and reusable functions.

- `__init__.py`  
  Marks this folder as a module.
- `logging_utils.py`  
  Contains:
  - Standardized logging setup.
  - Functions to log processing steps and errors.

---

### ─ Other Files

- `main.py`  
  The main entry point of the application:
  - Loads the input data (PDF text).
  - Calls the Cohere summarization function.
  - Outputs or saves the summarized text.

- `requirements.txt`  
  Lists all dependencies
