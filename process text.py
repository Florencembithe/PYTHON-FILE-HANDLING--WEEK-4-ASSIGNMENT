# Read the contents of input.txt
with open("input.txt", "r") as file:
    content = file.read()

# Count words
word_count = len(content.split())

# Convert text to uppercase
uppercase_text = content.upper()

# Write processed text and word count to output.txt
with open("output.txt", "w") as file:
    file.write("=== PROCESSED TEXT ===\n")
    file.write(uppercase_text)
    file.write("\n=== WORD COUNT ===\n")
    file.write(f"Total words: {word_count}\n")

# Success message
print("✅ output.txt created successfully with processed content and word count.")
