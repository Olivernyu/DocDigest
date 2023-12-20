# DocDigest
<p align="center">
    <img src="assets/image.png" alt="logo" width="300"/>
</p>

## Purpose of the Project
**DocDigest** is a service that aims to enable users to quickly comprehend and assimilate information from any document on the web.  
The need for efficient information processing in the digital age has led to the conception of DocDigest. It's designed to assist students, researchers, professionals, and journalists in managing extensive information efficiently.  


## Features
DocDigest's backend service has the following features provided in the form of a REST API:
- **Summarization**: Summarize any document on the web.
- **Highlighting**: Highlight the most important sentences in a document.
- **Annotation**: Annotating documents based on AI-generated summaries.
- **Semantic Search (WIP)**: Search for documents based on their semantic similarity to a given query. 

## Installation and Usage
### Running as a Development Server
1. Make sure all the dependencies are installed
2. **Run the command below from project root level**:
    ```bash
    uvicorn app.main:app --reload
    ```
### Running as Daemon (Production Server)
1. Make sure all the dependencies are installed
2. **Run the command below from project root level**:
    ```bash
    gunicorn --worker-class uvicorn.workers.UvicornWorker --bind '127.0.0.1:8000' --daemon app.main:app
    ```

## Development Instructions

### Setting up the Development Environment

1. **Set up a virtual environment**:
    - On macOS and Linux:

      ```bash
      python3 -m venv env
      ```

    - On Windows:

      ```bash
      py -m venv env
      ```

    - Activate the virtual environment:
      - On macOS and Linux: `source env/bin/activate`
      - On Windows: `.\\env\\Scripts\\activate`

2. **Clone this repository**.
3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

### Linting with Ruff

We use Ruff for static analysis. It's an efficient linting tool re-implemented in Rust and supports an expansive set of lint rules.

- **Lint the entire project**:

    ```bash
    ruff check .
    ```
  
- **Detailed documentation**: For a deeper understanding and additional commands, refer to the [official Ruff documentation](https://github.com/astral-sh/ruff).

### Testing with Pytest

Pytest facilitates easy and efficient testing in our template.

- **Run all tests**:

    ```bash
    pytest
    ```

- **More about Pytest**: Check the [official Pytest documentation](https://docs.pytest.org/en/stable/).

### Code Formatting with Black

Ensure your code adheres to our standards using Black.

- **Format all source files**:

    ```bash
    black .
    ```

- **Learn more about Black**: Visit the [official Black documentation](https://black.readthedocs.io/en/stable/).



## Tech Stack

- **Python Version**: 3.11+
- **Testing**: Integrated with Pytest.
- **Continuous Integration**: Set up with GitHub Actions.
- **Static Analysis**: Enhanced with Ruff.
- **Code Formatting**: Beautified with Black.
- **Dependency Management**: Streamlined with Pip.

## Contributing

Thank you for considering contributing to this project! We welcome contributions from everyone. To ensure a smooth collaboration, please follow these guidelines:

### Getting Started

1. Fork the repository and clone it to your local machine.
2. Create a new branch for your feature or bug fix:
    ```bash
    git checkout -b <branch-name>
    ```
3. Make your changes and test them thoroughly.
4. Commit your changes with a descriptive commit message:
    ```bash
    git commit -m "Add feature/fix for ..."
    ```
5. Push your changes to your forked repository:
    ```bash
    git push origin <branch-name>
    ```
6. Open a pull request against the main repository's `main` branch.

### Code Style and Standards

- Follow the existing code style and conventions.
- Ensure your code is properly formatted. You can use the provided code formatting tools (e.g., Black) to automatically format your code.

### Testing

- Write tests for your code changes to ensure they work as expected.
- Run the existing tests to make sure you haven't introduced any regressions:
  ```bash
  pytest
  ```

### Documentation

- Update the documentation if necessary to reflect your changes.
- Ensure your code is well-documented and includes comments where necessary.

### Feedback and Support

If you have any questions or need support, please open an issue on the GitHub repository. We appreciate your feedback and will do our best to assist you.

Thank you for your contributions!



## License

This project adopts the MIT License. See the [LICENSE.md](LICENSE.md) file for comprehensive details.
