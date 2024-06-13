import json
import os
import sys
from openai import OpenAI

def extract_text_elements(json_data):
    text_elements = {}

    def recurse_boxes(boxes, section_name=None):
        for box in boxes:
            guid = box['guid']
            if box["level"] == "widget":
                if "options" in box:
                    options = box["options"]
                    if "text" in options:
                        text_elements[guid] = {
                            "type": box.get("type", "unknown"),
                            "text": options["text"],
                            "sectionName": section_name
                        }
                    elif "doc" in options and "content" in options["doc"]:
                        for content in options["doc"]["content"]:
                            if "content" in content:
                                for item in content["content"]:
                                    if "text" in item:
                                        text_elements[guid] = {
                                            "type": content.get("type", "unknown"),
                                            "text": item["text"],
                                            "sectionName": section_name
                                        }
            if "boxes" in box:
                next_section_name = box.get("name", section_name) if box["level"] == "section" else section_name
                recurse_boxes(box["boxes"], next_section_name)

    recurse_boxes(json_data["boxes"])
    return text_elements

def update_text_elements(json_data, updated_texts):
    def recurse_boxes(boxes):
        for box in boxes:
            guid = box['guid']
            if box["level"] == "widget":
                if "options" in box:
                    options = box["options"]
                    if "text" in options and guid in updated_texts:
                        options["text"] = updated_texts[guid]["new_text"]
                    elif "doc" in options and "content" in options["doc"]:
                        for content in options["doc"]["content"]:
                            if "content" in content:
                                for item in content["content"]:
                                    if "text" in item and guid in updated_texts:
                                        item["text"] = updated_texts[guid]["new_text"]
            if "boxes" in box:
                recurse_boxes(box["boxes"])

    recurse_boxes(json_data["boxes"])

def generate_new_texts(text_elements, context):
    new_texts = {}
    client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))
    for guid, element in text_elements.items():
        max_length = int(len(element["text"]) * 1.15)

        section_name = element["sectionName"]
        old_texts_in_section = [e["text"] for e in text_elements.values() if e["sectionName"] == section_name]
        new_texts_in_section = [t["new_text"] for t in new_texts.values() if t["sectionName"] == section_name]


        prompt = (
            f"Generate a new {element['type']} text for a page with the context '{context}'. "
            f"The current text is: '{element['text']}'. "
            f"The text is from the section: '{section_name}', which aims to convert customers into leads. "
            f"The following are all the old texts in this section: {old_texts_in_section}. "
            f"The new texts generated so far in this section are: {new_texts_in_section}. "
            "Analyze the format and content of the current text and generate new text in the same format and context. "
            "For example, if the current text is a company name, the new text should also be a company name. "
            "If the current text is a question, the new text should also be a question. "
            "If the current text is a name and position, the new text should also follow the same format. "
            "If the previous text in the section is a question, the new text should provide an answer to that question."
            "Do not reuse any of the existing content. "
            f"Ensure the new text fits within similar character limits and does not exceed {max_length} characters. "
            "Only provide the new text without any headers or additional information."
        )
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {"role": "system", "content": "You are a helpful assistant designed to create copy for a new landing page."},
                {"role": "user", "content": prompt}
            ]
        )
        new_text = response.choices[0].message.content.strip()
        # print("TYPE: ", element['type'])
        # print("OLD TEXT: ", element['text'])
        # print("NEW TEXT: ",new_text)
        # print("-------------------------------")
        new_texts[guid] = {
            "sectionName": element["sectionName"],
            "type": element["type"],
            "old_text": element["text"],
            "new_text": new_text
        }
    return new_texts

def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <input_json_file> <output_json_file> '<context_string>'")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    context_string = sys.argv[3]
    results_dir = 'results'

    try:
        with open(input_file, 'r') as f:
            input_data = json.load(f)
    except Exception as e:
        print(f"Error reading input file: {e}")
        sys.exit(1)


    text_elements = extract_text_elements(input_data)
    updated_texts = generate_new_texts(text_elements, context_string)
    update_text_elements(input_data, updated_texts)

    if not os.path.exists(results_dir):
        os.makedirs(results_dir)

    output_path = os.path.join(results_dir, output_file)
    extraction_output_path = os.path.join(results_dir, f'extraction_{output_file}')

    try:
        with open(output_path, 'w') as f:
            json.dump(input_data, f, indent=4)
        print(f"Output saved to {output_path}")
    except Exception as e:
        print(f"Error writing output file: {e}")
        sys.exit(1)

    try:
        with open(extraction_output_path, 'w') as f:
            json.dump(updated_texts, f, indent=4)
        print(f"Extraction output saved to {extraction_output_path}")
    except Exception as e:
        print(f"Error writing extraction output file: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
