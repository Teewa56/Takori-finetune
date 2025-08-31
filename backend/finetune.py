import json
import os

def load_examples(jsonl_paths, n_examples=100):
    """
    Load up to n_examples Q&A pairs from a list of JSONL files.
    """
    examples = []
    for path in jsonl_paths:
        if not os.path.exists(path):
            continue
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    try:
                        examples.append(json.loads(line))
                    except Exception:
                        continue
                if len(examples) >= n_examples:
                    return examples
    return examples

def build_prompt(user_question, n_examples=100, data_dir="../data"):
    """
    Build a prompt for the AI using Q&A pairs from all available JSONL files in data_dir.
    """
    jsonl_files = [
        os.path.join(data_dir, fname)
        for fname in [
            "qa_data.jsonl",
            "academic_info.jsonl",
            "business_docs.jsonl",
            "schooldata.jsonl"
        ]
    ]
    examples = load_examples(jsonl_files, n_examples)
    prompt = ""
    for ex in examples:
        q = ex["messages"][0]["content"]
        a = ex["messages"][1]["content"]
        prompt += f"Q: {q}\nA: {a}\n"
    prompt += f"Q: {user_question}\nA:"
    return prompt

# Example usage
if __name__ == "__main__":
    user_question = "How do I calculate my GPA at FUTA?"
    prompt = build_prompt(user_question)
    print(prompt)