
# Cli Game

Brief description of your project.

## Getting Started

These instructions will get your copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them:

- Python (version 3.x recommended)
- pip (Python package installer)



## Running the Tests

Explain how to run the automated tests for this system:

```bash
python -m unittest discover
```

## Code Coverage

Current test coverage is 96%.

To measure and view the code coverage of your tests, follow these steps:

### 1. Installing Coverage.py

If you haven't already installed `coverage.py`, you can do so using pip:

```bash
pip install coverage
```

### 2. Running Tests with Coverage

To run your tests and collect coverage data, use the following command in the root directory of the project:

```bash
coverage run -m unittest discover
```
This command executes all tests (files named `test_*.py`) and records which lines of code are exercised.

### 3. Generating Coverage Reports

After the tests have run, you can generate coverage reports in various formats:

#### Terminal Report

For a quick summary in your terminal, run:

```bash
coverage report
```
This will display a table with coverage percentages for each file.

#### HTML Report

For a more detailed, interactive report, generate an HTML version:

```bash
coverage html
```
This command creates a directory named `htmlcov` (by default). Open the `htmlcov/index.html` file in a web browser to explore the coverage details, including which specific lines were covered or missed in each file.

### Viewing Coverage Report

- The **terminal report** is useful for a quick overview of coverage percentages per file.
- The **HTML report** provides an in-depth view, allowing you to navigate through your code and see exactly which lines are tested and which are not. This is highly recommended for identifying areas to improve test coverage.
