import json

input_path = "./data/SystemChat-2.0/SystemChat_filtered.jsonl"
output_path = "./data/SystemChat-2.0/ID_SystemChat_filtered.jsonl"

with open(input_path, "r", encoding="utf-8") as infile, open(output_path, "w", encoding="utf-8") as outfile:
    for idx, line in enumerate(infile):
        data = json.loads(line)
        data["id"] = str(idx)  # You can use int or str depending on your needs
        outfile.write(json.dumps(data, ensure_ascii=False) + "\n")

print(f"✅ Finished writing to {output_path}")
