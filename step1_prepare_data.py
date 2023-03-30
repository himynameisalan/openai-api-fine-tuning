import csv

# Load Q&A data from CSV file
qa_data = []
with open('raw_data.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        qa_data.append(row)

# Create list of prompt-completion pairs
prompt_completion_pairs = []
for i, qa_pair in enumerate(qa_data):
    # Transform the dataset into your custom format

    # This is a default format
    prompt = f" {qa_pair['question']}"
    completion = f" {qa_pair['answer']}"

    # This is an example of custom format
    # summary = f"\nquestion: {qa_pair['question']}\nanswer: {qa_pair['answer']}"
    # prompt = f"Summary: {summary}\n###\n\nCustomer: {qa_pair['question']}\nBot:"

    prompt_completion_pairs.append({'prompt': prompt, 'completion': completion})

# Write prompt-completion pairs to CSV file
with open('prompt_completion_pairs.csv', 'w', newline='') as f:
    fieldnames = ['prompt', 'completion']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for pair in prompt_completion_pairs:
        writer.writerow(pair)
