#Open and REad Text File
def read_file(filename):
    with open(filename,"r") as file:
        return file.read()
#Test
content = read_file("Fight_Club.txt")
print(content[:100])

#Count Number of Lines
def count_lines(content):
    return len(content.split("\n"))
#Test
num_lines = count_lines(content)
print(f"Number of lines:{num_lines}")

#Count Words
def count_words(content):
    return len(content.split())
#Test
num_words = count_words(content)
print(f"Number of words: {num_words}")

#Most Common Word
from collections import Counter

def most_common_word(content):
    words = content.lower().split()
    word_counts = Counter(words)
    return word_counts.most_common(1)[0]

#Exercise 1 - Find unique words
def unique_words(content):
    words = content.lower().split()
    return set(words)
#Test
common_word, count = most_common_word(content)
print(f"Most common word:{common_word} (appears {count} times)")

#Exercise 2 - Find the longest word
def longest_word(content):
    words = content.split()
    return max(words, key=len)

#Exercise 3- Find the occurances of a specfic word
def count_specific_word(content, word):
    words = content.lower().split()
    return words.count(word.lower())

#Exercise 4 - Calculate Percentage of words Longer than Average Word Length
def percentage_longer_than_average(content):
    avg_length = average_word_length(content)
    words = content.split()
    longer_than_average = [word for word in words if len(word) > avg_length]
    return (len(longer_than_average) / len(words)) * 10

#Average Word Length
def average_word_length(content):
    words = content.split()
    total_length = sum(len(word) for word in words)
    return total_length / len(words)
#Test
avg_length = average_word_length(content)
print(f"Average word length: {avg_length: .2f} characters")

#Combining Everything into Main Function
def analyze_text(filename):
    content = read_file(filename)

    num_lines = count_lines(content)
    num_words = count_words(content)
    common_word , count = most_common_word(content)
    avg_length = average_word_length(content)
    unique_word_count = len(unique_words(content))
    find_longest_word = longest_word(content)
    
    print(f"File: {filename}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")
    print(f"Most common word: '{common_word}' (appears {count} times)")
    print(f"Average word length: {avg_length:.2f} characters")
    print(f"Number of unique words: {unique_word_count}")
    print(f"Longest word: {find_longest_word}")
    print(f"Average word length: {avg_length:.2f} characters")
    
    # Count specific word
    specific_word = "fight"  # Change this to the word you want to count
    specific_word_count = count_specific_word(content, specific_word)
    print(f"The word '{specific_word}' appears {specific_word_count} times.")
    # Calculate percentage of words longer than average word length
    percentage = percentage_longer_than_average(content)
    print(f"Percentage of words longer than average word length: {percentage:.2f}%")

# Run the analysis
analyze_text('Fight_Club.txt')