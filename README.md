# Judicial Reports Data Extractor

## Overview
The "Judicial Reports Data Extractor" is a Python script meticulously crafted to streamline the extraction of crucial information from the "Prevention of Future Deaths Reports" published on the UK Judiciary website. These reports, serving as pivotal documents for understanding and mitigating recurring fatalities, are presented in the form of PDF documents linked from individual report pages.

The primary objective of this tool is to provide a robust and automated solution for data collection, enabling researchers, analysts, or stakeholders to effortlessly access and analyze key details within these reports. The script adeptly extracts essential metadata such as the report ID, date, receiver, and content, and organizes the information into a structured CSV file. This CSV format facilitates seamless integration into various data analysis workflows.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Error Handling](#error-handling)
- [Example Usage](#example-usage)
- [Contributing](#contributing)
- [License](#license)

## Installation
1. **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/judicial-reports-data-extractor.git
    ```

2. **Install Dependencies:**
    ```bash
    pip install requests beautifulsoup4 pdf2image pytesseract Pillow PyMuPDF
    ```

3. **Tesseract OCR:**
    Download and install Tesseract OCR from [https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract). Ensure that the `pytesseract.pytesseract.tesseract_cmd` variable in the script points to the correct Tesseract executable on your system.

## Usage
To employ the extractor, populate the `urls` variable in the script with the desired report URLs. Execute the script, and it will generate a CSV file (`output.csv`) containing the meticulously extracted information.

```bash
python extractor.py
```

## Dependencies
- `requests`: For making HTTP requests to fetch web pages and PDFs.
- `beautifulsoup4`: For parsing HTML content.
- `pdf2image`: For converting PDF pages to images.
- `pytesseract`: For performing OCR on images to extract text.
- `Pillow`: For working with images in Python.
- `PyMuPDF`: For extracting text from PDF documents.

## Configuration
The script includes variables that can be configured to adjust its behavior:
- `pytesseract.pytesseract.tesseract_cmd`: Path to the Tesseract executable.
- `section1_start` and `section1_end`: Markers for extracting the first section of the report.
- `section2_start` and `section2_end`: Markers for extracting the second section of the report.

## Error Handling
The script incorporates robust error handling for scenarios where specific sections are not found or exceptions occur during the extraction process. Error messages are displayed in the console, and default values are assigned to the corresponding variables.

## Example Usage
An example usage section is provided in the script, showcasing how to use the extractor with a list of sample URLs. Users can customize the `urls` list to include the specific reports they want to analyze.

```python
urls = [
    "https://www.judiciary.uk/prevention-of-future-death-reports/report1/",
    "https://www.judiciary.uk/prevention-of-future-death-reports/report2/",
    # Add more URLs as needed
]
```

## Contributing
Contributions are encouraged! If you encounter issues or have suggestions for improvements, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
