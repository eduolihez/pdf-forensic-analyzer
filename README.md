# PDF Dictionary Generator for John the Ripper

## Description
This repository contains a Python script that extracts words from PDF documents and generates custom dictionaries for password auditing with John the Ripper. The script was developed for an authorized educational cybersecurity exercise where we needed to analyze password patterns and demonstrate dictionary attack techniques in a controlled environment.

---

## Table of Contents
- [PDF Dictionary Generator for John the Ripper](#pdf-dictionary-generator-for-john-the-ripper)
  - [Description](#description)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Technologies Used](#technologies-used)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contact](#contact)

---

## Features
- **PDF Text Extraction**: Extracts all text content from PDF documents using PyMuPDF
- **Smart Word Filtering**: Filters words between 4-12 characters (configurable)
- **Number Detection**: Identifies and extracts numerical values from the PDF
- **Dictionary Generation**: Creates custom wordlists by combining words with numbers
- **John the Ripper Compatible**: Outputs formatted text files ready for use with JtR

---

## Installation
Follow these steps to get the script running on your local machine:

1. Clone the repository:
   ```bash
   git clone https://github.com/eduolihez/pdf-forensic-analyzer.git
   ```
2. Navigate to the project directory:
   ```bash
   cd pdf-forensic-analyzer
   ```
3. Install the required dependencies:
   ```bash
   pip install pymupdf
   ```

---

## Usage
To use this script, run the following command in your terminal:

```bash
python pdf-forensic-analyzer.py path/to/your/document.pdf
```

The script will generate a file named `dictionary_john.txt` in the same directory, which contains the custom dictionary.

### Educational Context
This script was specifically developed for a classroom exercise where we needed to find credentials for a user named "Ermessenda". The password followed the pattern: alphabetic characters + 4 digits, with maximum length of 12 characters. The script successfully generated a dictionary that helped identify the password "Girona1035" by combining biographical terms with numerical combinations.

### Code Example
```python
# Core functionality - extract and combine words with numbers
def generate_combinations(words, numbers):
    combinations = set()
    for word in words:
        combinations.add(word)  # Add the word alone
        for number in numbers:
            # Create word+number and number+word combinations
            combinations.add(word + number)
            combinations.add(number + word)
    return combinations
```

---

## Technologies Used
This project was built using:
- **Python**: Core programming language for the script
- **PyMuPDF**: Library for PDF text extraction and parsing
- **Regular Expressions**: For pattern matching and word filtering

---

## Contributing
This is an educational project, but if you have suggestions:
1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Commit your changes
4. Push the branch and open a Pull Request

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contact
- **GitHub**: [your-username](https://github.com/eduolihez)

This project was created for educational purposes in authorized cybersecurity training.
