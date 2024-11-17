from pyspark import SparkContext
sc=SparkContext('local','avgword')
txt=sc.textFile('/home/vishnu/Documents/val.txt')
x=txt.flatMap(lambda line:line.split(","))
y=x.map(lambda x:len(x))
total_len=y.reduce(lambda x,y:x+y)
totalwords=y.count()
avg=total_len/totalwords
print(f"the average is : {avg}")

