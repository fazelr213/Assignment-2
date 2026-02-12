
# The function checks for matching keywords
def find_lines_containing(filename, keyword):
    results = []

    with open("sample-file.txt", "r") as f:
        for i, line in enumerate(f, 1):  # line numbers start at 1
            if keyword.lower() in line.lower():  # case-insensitive
                results.append((i, line.strip()))

    return results


# Test using sample-file.txt and keyword "lorem"
matches = find_lines_containing("sample-file.txt", "lorem")

# Print how many lines matched
print("Number of matches:", len(matches))

# Print first 3 matches
for line_number, text in matches[:3]:
    print(line_number, ":", text)
