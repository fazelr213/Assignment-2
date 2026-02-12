def normalize(line):
    # Convert the line to lowercase
    line = line.lower()

    # Remove whitespace and punctuation (keep only letters and numbers)
    result = ""
    for ch in line:
        if ch.isalnum():
            result += ch
    return result


# Open the file and read all lines into a list
# Open the file and automatically close it after reading
with open("sample-file.txt", "r") as file:
    lines = file.readlines()


# Dictionary to store normalized lines as keys
# and a list of (line number, original text) as values
groups = {}

# Go through each line in the file
for i in range(len(lines)):
    # remove extra spaces/newlines
    original = lines[i].strip()

    # Skip blank lines
    if original == "":
        continue

    # Normalize the line
    norm = normalize(original)

    # Extra safety: skip lines that become empty after normalization
    if norm == "":
        continue

    # Add the line to the dictionary
    if norm in groups:
        groups[norm].append((i + 1, original))
    else:
        groups[norm] = [(i + 1, original)]

# Store only groups that have more than one line (near-duplicates)
duplicates = []
for key in groups:
    if len(groups[key]) > 1:
        duplicates.append(groups[key])

# Print the total number of near-duplicate sets
print("Number of duplicated sets:", len(duplicates))
print()

# Print the first two sets (if they exist)
for i in range(min(2, len(duplicates))):
    print("Set", i + 1)
    for line_number, text in duplicates[i]:
        print(line_number, ":", text)
    print()
