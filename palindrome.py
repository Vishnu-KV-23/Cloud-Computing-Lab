from pyspark import SparkContext

# Initialize SparkContext
sc = SparkContext('local', 'wordcount')

# Set log level to ERROR to reduce warnings
sc.setLogLevel("ERROR")

# Read a text file
txt = sc.textFile('/home/vishnu/Cloud-Computing-Lab/paltext.txt')

# Split each line into words
val = txt.flatMap(lambda line: line.split(","))

# Create a tuple for each word with count 1
valm = val.map(lambda word: (word, 1))

# Filter palindromic words
ls = valm.filter(lambda s: s[0] == s[0][::-1])

# Sum the counts for each palindrome
red = ls.reduceByKey(lambda a, b: a + b)

# Collect the results and print them
resu = red.collect()
for word, count in resu:
    print(f"palindromes\n{word} = {count}")

# Stop SparkContext
sc.stop()


