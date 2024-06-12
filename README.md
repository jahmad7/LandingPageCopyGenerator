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

## Thought Process for Solving the Problem

To make the solution easy to implement, I created a simple Python program that can be run from the command line. Here's a clear explanation of my approach to solving the problem, which is outlined step-by-step below:

### Overview
The goal is to update the text content of a JSON file representing a landing page. The JSON file contains nested structures where text content is found at the "widget" level within "options" or "doc" objects. We need to:

1. Extract the text elements, including their types and locations.
2. Use OpenAI's API to generate new text content based on a provided context.
3. Replace the old text with the new text in the JSON structure.
4. Save the updated JSON and a summary of the changes.

### Steps to Accomplish the Goal

1. Extract Text from JSON File:

- Recursive Function: I wrote a recursive function to traverse the JSON structure. This function moves through "boxes" until it reaches a "widget" level where it checks for "options" or "doc" objects to find text content.
- Storing Data: The extracted text, along with its type and location (using the GUID), is stored in a hash map. This ensures efficient access and updating of text elements.

2. Use OpenAI API for Text Generation:

- Single API Call: To optimize for time and cost, I designed the solution to make a single call to OpenAI's API. The prompt includes the entire context and structure, asking for updated values for each text field based on the new page context provided by the user.

- Storing New Text: The responses are stored in the same hash map, now including both old and new text for each GUID.

3. Update JSON with New Text:

- Recursive Update: Another recursive function traverses the JSON structure again. It checks each "widget" level using the GUID and updates the text content with the new values from the hash map.

4. Save Output Files:

- Output JSON File: The updated JSON structure is saved to an output file (output.json) in a results folder.
- Extraction Summary File: A separate file (extraction_output_filename.json) is also created. This file contains the GUID, type, old text, and new text for each updated text element, providing a quick reference without needing to parse the entire JSON file.

### Detailed Explanation of the Code
The code is designed to be modular and efficient, ensuring ease of maintenance and scalability. Here are the key functions:

- extract_text_elements(json_data):

Recursively traverses the JSON structure to extract text elements and store them in a hash map with GUID as the key.

- generate_new_texts(text_elements, context):

Uses OpenAI's API to generate new text based on the provided context and updates the hash map with new text values.

- update_text_elements(json_data, updated_texts):

Recursively traverses the JSON structure again to update the text elements with new values from the hash map.
main():

The main function orchestrates the process: reading the input JSON file, extracting text elements, generating new text, updating the JSON structure, and saving the output files.
