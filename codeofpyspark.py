Palindrome :

# Read the text file
word = sc.textFile("/Users/adithyaraj/Desktop/text.txt").flatMap(lambda line: line.split(" "))

# Filter out palindromic words (words that read the same forwards and backwards)
non_palindromic_words = word.filter(lambda w: w != w[::-1])

# Map each word to a (word, 1) pair
a = non_palindromic_words.map(lambda word: (word, 1))

# Reduce by key to get the word count
b = a.reduceByKey(lambda a, b: a + b)

# Collect the results
result = b.collect()
print(result)

FILTERED words:

# List of words to filter out
stopwords = ["the", "is", "a"]

# Load the text file and split lines into words
words = sc.textFile("/Users/adithyaraj/Desktop/text.txt").flatMap(lambda line: line.split(" "))

# Filter out the specified words
filtered_words = words.filter(lambda word: word.lower() not in stopwords)

# Map each word to (word, 1)
word_counts = filtered_words.map(lambda word: (word, 1))

# Reduce by key to count occurrences
word_counts = word_counts.reduceByKey(lambda a, b: a + b)

# Collect and print the result
result = word_counts.collect()
print(result)

Distinct word count:

# Load the text file and split lines into words
words = sc.textFile("/Users/adithyaraj/Desktop/text.txt").flatMap(lambda line: line.split(" "))

# Find distinct words
distinct_words = words.distinct()

# Count the number of distinct words
distinct_word_count = distinct_words.count()

# Print the result
print("Number of distinct words:", distinct_word_count)


simple wc:

word = sc.textFile("/Users/adithyaraj/Desktop/text.txt").flatMap(lambda line:line.split(" ")) 
>>> a=word.map(lambda word:(word,1)) 
>>> b=a.reduceByKey(lambda a,b:a +b) 
>>> b.collect()
