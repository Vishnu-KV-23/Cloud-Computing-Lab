from pyspark import SparkContext

# Initialize SparkContext
sc = SparkContext('local', 'prime_count')


# Read numbers from a text file (one number per line)
file_path = '/home/vishnu/Documents/primetext.txt'
num_rdd = sc.textFile(file_path)

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
val=num_rdd.flatMap(lambda line: line.split (" "))
Word=val.map(lambda x: int(x))
# Filter the RDD to keep only prime numbers
prime_rdd = Word.filter(is_prime)

# Count the number of prime numbers
prime_count =prime_rdd.count()
print(f"Count of Prime Numbers: {prime_count}")

# Stop SparkContext
sc.stop()
