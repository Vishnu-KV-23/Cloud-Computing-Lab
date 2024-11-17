from pyspark import SparkContext
sc=SparkContext('local','palindrome')
txt=sc.textFile('/home/vishnu/Documents/val.txt')
x=txt.flatMap(lambda line:line.split(","))
y=x.map(lambda a:(a,1))
z=y.filter(lambda x:x[0]==x[0][::-1])
p=z.reduceByKey(lambda a,b:a+b)
res=p.collect()
print(res)
