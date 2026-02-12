

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

bigram_frequency = {}

# Make bigrams and count them
for i in range(len(cleaned_words) - 1):

    bigram = cleaned_words[i] + " " + cleaned_words[i + 1]

    if bigram in bigram_frequency:
        bigram_frequency[bigram] += 1
    else:
        bigram_frequency[bigram] = 1


# Sort bigrams by frequency (largest first)
sorted_bigrams = sorted(bigram_frequency.items(), key=lambda x: x[1], reverse=True)

# Print top 5 bigrams
for i in range(5):
    print(sorted_bigrams[i][0] + " -> " + str(sorted_bigrams[i][1]))
