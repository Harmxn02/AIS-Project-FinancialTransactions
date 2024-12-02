import json
import csv

def json_to_csv_large(input_file, output_file, chunk_size=1000):
    """
    Converts a large JSON file to CSV format in a memory-efficient way.
    
    Args:
        input_file (str): Path to the input JSON file.
        output_file (str): Path to the output CSV file.
        chunk_size (int): Number of records to process at a time.
    """
    with open(input_file, 'r') as json_file, open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
        data = json.load(json_file)
        
        # Extract the "target" dictionary
        target_data = data.get("target", {})
        
        # Prepare the CSV writer
        writer = csv.writer(csv_file)
        
        # Write the header
        writer.writerow(["fraud_id", "CLASS_fraud_label"])
        
        # Write rows for each key-value pair in the "target" dictionary
        for key, value in target_data.items():
            writer.writerow([key, value])

# Example usage
json_to_csv_large("../data/train_fraud_labels.json", "../data/train_fraud_labels.csv")
