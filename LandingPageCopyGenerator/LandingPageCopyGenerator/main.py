import json
import os
import sys

def process_json(input_json, context):
    # Process the JSON data and add the context information
    # input_json['context'] = context
    return input_json

def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <input_json_file> <output_json_file> <context_string>")
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

    output_data = process_json(input_data, context_string)

    if not os.path.exists(results_dir):
        os.makedirs(results_dir)

    output_path = os.path.join(results_dir, output_file)

    try:
        with open(output_path, 'w') as f:
            json.dump(output_data, f, indent=4)
        print(f"Output saved to {output_path}")
    except Exception as e:
        print(f"Error writing output file: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
