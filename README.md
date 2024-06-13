# Landing Page Copy Generator

## Description

A simple program that takes in a JSON file from LeadPages with the structure of content and outputs a processed JSON file with new content based on the purpose of the landing page provided. The program extracts the text and type of text (e.g., button text, headline, paragraph) and uses OpenAI API to update the copy based on the provided context for the new page.

## Usage

```bash
python LandingPageCopyGenerator/main.py test.json output1.json "Leadpages: High-performing landing pages without the hassle"
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

## Running tests

to run all tests, run the following command from the project directory with main.py:

```bash
python -m unittest discover -s tests
```

to run individual tests, run the following command from the project directory with main.py:

```bash
python -m unittest tests.test_main
```

## Thought Process for Solving the Problem

To make the solution easy to implement, I created a simple Python program that can be run from the command line. Here's a clear explanation of my approach to solving the problem, which is outlined step-by-step below:

### Overview

The goal is to update the text content of a JSON file representing a landing page. The JSON file contains nested structures where text content is found at the "widget" level within "options" or "doc" objects. We need to:

1. Extract the text elements, including their types and locations.
2. Use OpenAI's API to generate new text content based on a provided context.
3. Replace the old text with the new text in the JSON structure.
4. Save the updated JSON and a summary of the changes.

### Steps to Accomplish the Goal

1. **Extract Text from JSON File:**

- **Recursive Function:** This function navigates through the JSON structure, reaching "widget" levels to locate text content within "options" or "doc" objects.
- **Section Tracking:** The function also tracks the section name to provide context for each text element.
- **Efficient Storage:** Text elements are stored in a hash map, including the type, location, and section name, ensuring efficient access and updates.

2. ***Use OpenAI API for Text Generation:***

- **API Calls by Section:** Prompts are constructed based on the section context, incorporating old texts, new texts, and section-specific information to guide the AI in generating relevant content.
- Consideration of Format: The prompt instructs the AI to maintain the format of the original text (e.g., company name, question, name and position) and ensure new text aligns with the section's purpose.
- **Storing Responses:** New text responses are stored alongside old texts in the hash map, preserving the section context and ensuring consistency across the page.

3. ***Update JSON with New Text:***

- **Recursive Update:** Another recursive function traverses the JSON structure again. It checks each "widget" level using the GUID and updates the text content with the new values from the hash map.

4. **Save Output Files:**

- Output JSON File: The updated JSON structure is saved to an output file (output.json) in a results folder.
- Extraction Summary File: A separate file (extraction_output_filename.json) is also created. This file contains the GUID, type, old text, and new text for each updated text element, providing a quick reference without needing to parse the entire JSON file.


### Detailed Explanation of the Code

The code is designed to be modular and efficient, ensuring ease of maintenance and scalability. Here are the key functions:

```python
extract_text_elements(json_data)
```

**Purpose:** Recursively traverses the JSON structure to extract text elements.

**Process:** Moves through "boxes" until it reaches "widget" levels, where it looks for "options" or "doc" objects to find text content.

**Output:** Stores the extracted text, type, GUID, and section name in a hash map for efficient access and updating.

```python
generate_new_texts(text_elements, context)
```

**Purpose:** Uses OpenAI's API to generate new text based on the provided context.

**Process:**
Constructs prompts based on the section context, including the section name, old texts, and new texts generated so far.
Ensures the AI generates text that maintains the format of the original text (e.g., company name, question, name and position).
Provides specific instructions to ensure the new text is contextually appropriate and maintains continuity within the section.

**Output:** Updates the hash map with new text values, including the section context.

```python
update_text_elements(json_data, updated_texts)
```

**Purpose:** Recursively traverses the JSON structure again to update the text elements with new values.

**Process:** Uses the hash map to replace old text elements with new ones, ensuring the JSON structure is updated accordingly.

```python
main():
```

**Purpose:** Orchestrates the entire process.

**Process:**

- Reads the input JSON file.
- Extracts text elements using extract_text_elements.
- Generates new text using generate_new_texts.
- Updates the JSON structure with update_text_elements.
- Saves the updated JSON structure and extraction output to output files.

### Future Improvements

1. **Reducing Time to Completion**

Currently, the process to generate new text for the page is somewhat time-consuming, especially with making 37 individual API calls to generate 37 new texts. To improve this:

- ***Batch API Calls:*** I would experiment with batching the requests into a single API call, where all text elements are processed at once. This could significantly reduce the time to completion while maintaining the quality of the responses.
- ***Prioritizing Speed:*** In this challenge, the priority was on the quality of responses over speed. Future iterations would aim to balance both, optimizing for faster response times without compromising on the quality.

2. **Integrating Image Generation**

There are images on the landing page, which are currently not addressed by the text generation process. To enhance the overall page redesign:

- ***Image Generation:*** After generating the new text for each section that includes an image, I would use OPENAI image generation API to create new images that complement the updated copy.
 - ***Consistency:*** Ensuring that the new images align well with the new text will create a more cohesive and visually appealing landing page.

3. **Enhancing Lead Page Effectiveness**

To make the landing page more effective in converting leads:

- ***Understanding Lead Pages***: I would research more about what makes a great lead page, identifying key elements that drive conversions.
- ***Providing Context***: Using this knowledge, I would give the model more context about what each section of the page should accomplish (e.g., capturing interest, building trust, encouraging action).
- ***Scoring Generated Copy***: After generating the copy, I would implement a scoring system where the model evaluates the effectiveness of the text based on predefined criteria. Over time, I would compare these scores with actual user engagement metrics to refine and improve the model's ability to create high-converting copy.
- ***Internet Function Research***: I would also add in functionality to research the internet about the context that the user provides to generate more relevant copy.
