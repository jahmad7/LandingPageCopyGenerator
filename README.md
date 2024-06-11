# Landing Page Copy Generator

## Description

A simple program that takes in a JSON file from LeadPages with the structure of content and outputs a processed JSON file with new content based on the purpose of the landing page provided. The program extracts the text and type of text (e.g., button text, headline, paragraph) and uses OpenAI API to update the copy based on the provided context for the new page.

## Usage

```bash
python LandingPageCopyGenerator/main.py test.json <output_json_file> "<Name of Page: Purpose of page>"
```

## Arguments

- test.json: the input JSON file from LeadPages.
- <output_json_file>: Desired path for the output JSON file with updated content.
- "<Name of Page: Purpose of page>": A string explaining the context of the new page in the format "Name of Page: Purpose of page".

## Example

```bash
python LandingPageCopyGenerator/main.py test.json result.json "New Landing Page: Promoting a Summer Sale"
```

## Requirements

- Python 3.x
- OpenAI API key

## Creating the virtual environment

1. Run `python3 -m venv venv`
2. Run `source venv/bin/activate`


## Installation

1. Clone the repository.

```bash
git clone git@github.com:jahmad7/LandingPageCopyGenerator.git
```

2. cd into the directory.

```bash
cd LandingPageCopyGenerator
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Update the OpenAI API key in the `.env` file.
