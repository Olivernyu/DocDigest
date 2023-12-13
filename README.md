# Python Technology Template

A robust starting point for Python projects, offering an integrated development environment with a complete toolchain.

## Getting Started

Follow these steps to set up and run the template:

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

4. **Run tests**:

    ```bash
    pytest
    ```

5. **Format your code**:

    ```bash
    black .
    ```

6. **Static analysis with Ruff**:

    ```bash
    ruff check .
    ```

## Features

- **Python Version**: 3.11+
- **Testing**: Integrated with Pytest.
- **Continuous Integration**: Set up with GitHub Actions.
- **Static Analysis**: Enhanced with Ruff.
- **Code Formatting**: Beautified with Black.
- **Dependency Management**: Streamlined with Pip.

## Linting with Ruff

We use Ruff for static analysis. It's an efficient linting tool re-implemented in Rust and supports an expansive set of lint rules.

- **Lint the entire project**:

    ```bash
    ruff check .
    ```
  
- **Detailed documentation**: For a deeper understanding and additional commands, refer to the [official Ruff documentation](https://github.com/astral-sh/ruff).

## Testing with Pytest

Pytest facilitates easy and efficient testing in our template.

- **Run all tests**:

    ```bash
    pytest
    ```

- **More about Pytest**: Check the [official Pytest documentation](https://docs.pytest.org/en/stable/).

## Code Formatting with Black

Ensure your code adheres to our standards using Black.

- **Format all source files**:

    ```bash
    black .
    ```

- **Learn more about Black**: Visit the [official Black documentation](https://black.readthedocs.io/en/stable/).

## License

This project adopts the MIT License. See the [LICENSE.md](LICENSE.md) file for comprehensive details.
