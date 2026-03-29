

with open("source.txt", "r") as src:
    # Read content
    content = src.read()

# Open destination file in write mode
with open("destination.txt", "w") as dest:
    # Write content
    dest.write(content)

print("File copied successfully!")