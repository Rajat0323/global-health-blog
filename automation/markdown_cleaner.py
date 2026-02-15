import os
import re

POSTS_DIR = "../posts"

def clean_markdown(content):
    # Fix "# Heading paragraph"
    content = re.sub(
        r'^(#{1,6})\s+([A-Za-z0-9 ,\-]+)\s+(.*)$',
        r'\1 \2\n\n\3',
        content,
        flags=re.MULTILINE
    )

    # Ensure blank line after headings
    content = re.sub(
        r'(#{1,6} .+)\n([^\n#])',
        r'\1\n\n\2',
        content
    )

    return content


for root, _, files in os.walk(POSTS_DIR):
    for file in files:
        if file.endswith(".md"):
            path = os.path.join(root, file)

            with open(path, "r", encoding="utf-8") as f:
                original = f.read()

            cleaned = clean_markdown(original)

            if cleaned != original:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(cleaned)

                print(f"✅ Fixed: {path}")
