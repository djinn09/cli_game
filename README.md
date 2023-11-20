
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

To measure the code coverage of your tests, follow these steps:

### Installing Coverage.py

If you haven't already installed `coverage.py`, you can do so using pip:

```bash
pip install coverage
```

### Running Coverage

To run your tests with coverage, use the following command:

```bash
coverage run -m unittest discover
```

This command will execute all your tests and collect coverage data.

### Generating Coverage Report

After running the tests, you can generate a coverage report in two formats:

1. **Terminal Report:**

   ```bash
   coverage report
   ```

   This command will display a coverage report in the terminal.

2. **HTML Report:**

   ```bash
   coverage html
   ```

   This generates a more detailed HTML report in a directory named `htmlcov`. Open `htmlcov/index.html` in a web browser to view it.

### Viewing Coverage Report

- For a quick overview, use the terminal report.
- For a detailed view, including which lines are not covered by tests, use the HTML report.
