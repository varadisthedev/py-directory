import json
import os

def extract_conversations(data):
    extracted = {}

    for convo in data:
        title = convo.get("title", "Untitled")
        mapping = convo.get("mapping", {})
        messages = []

        def walk(node_id):
            node = mapping.get(node_id, {})
            msg_data = node.get("message")
            if msg_data:
                role = msg_data["author"]["role"]
                content_obj = msg_data.get("content", {})
                parts = content_obj.get("parts")

                if role in ["user", "assistant"] and parts:
                    # Fix: handle if parts is list of dicts or strings
                    text_parts = []
                    for part in parts:
                        if isinstance(part, str):
                            text_parts.append(part)
                        elif isinstance(part, dict):
                            text_parts.append(part.get("text", ""))

                    content = "\n".join(text_parts).strip()
                    if content:
                        messages.append({"role": role, "text": content})

            for child_id in node.get("children", []):
                walk(child_id)

        root_id = next(iter(mapping), None)
        if root_id:
            walk(root_id)
        extracted[title] = messages

    return extracted

if __name__ == "__main__":
    path = input("Enter path to your chat_export.json: ").strip()

    if not os.path.exists(path):
        print("❌ File not found.")
        exit(1)

    with open(path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            print("❌ Invalid JSON.")
            exit(1)

    if not isinstance(data, list):
        print("❌ Expected a list of conversations at root level.")
        exit(1)

    extracted = extract_conversations(data)

    out_file = "chat_summary.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(extracted, f, indent=2, ensure_ascii=False)

    print(f"✅ Exported organized chat to {out_file}")
