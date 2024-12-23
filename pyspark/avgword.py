from pyspark import SparkContext

# Initialize SparkContext
sc = SparkContext('local', 'avg_word_length')

# Read a text file
txt = sc.textFile('/home/vishnu/Documents/val.txt')

# Split each line into words
words = txt.flatMap(lambda line: line.split(","))

# Map each word to its length
word_lengths = words.map(lambda word: len(word))

# Compute the total length and the number of words
total_length = word_lengths.reduce(lambda a, b: a + b)
word_count = word_lengths.count()

# Calculate the average word length
average_length = total_length / word_count

# Print the average word length
print(f"Average word length: {average_length}")

# Stop SparkContext
sc.stop()
