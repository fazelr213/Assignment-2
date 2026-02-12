

# Reads the file and stores it as a string
with open("sample-file.txt", "r") as file:
    sample_file_data_211 = file.read()

# Converts all words to lowercase
sample_file_data_211 = sample_file_data_211.lower()

# Splits the string into a list of words based on spaces
sample_file_data_211 = sample_file_data_211.split()

cleaned_words = []

# Loop through each word in the list
for word in sample_file_data_211:

    # Remove non-letter characters from the beginning of the word
    while len(word) > 0 and not word[0].isalpha():
        word = word[1:]

    # Remove non-letter characters from the end of the word
    while len(word) > 0 and not word[-1].isalpha():
        word = word[:-1]

    # Count how many alphabetic letters are inside the word
    character_count_in_word = 0
    for character in word:
        if character.isalpha():
            character_count_in_word += 1

    # Only keep words that contain at least 2 letters
    if character_count_in_word >= 2:
        cleaned_words.append(word)

word_frequency = {}

# Count how many times each word appears
for word in cleaned_words:
    if word in word_frequency:
        word_frequency[word] += 1  # Increase count if word already exists
    else:
        word_frequency[word] = 1  # Start count at 1 if new word


# Function that returns the count
def get_count(item):
    return item[1]


# Sort words by frequency
word_frequency_sorted = sorted(word_frequency.items(), key=get_count, reverse=True)

# Print the 10 most frequent words in the required format
for word, count in word_frequency_sorted[:10]:
    print(word + " -> " + str(count))


