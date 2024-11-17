from pyspark import SparkContext
sc=SparkContext('local','wordcount')
txt=sc.textFile('/home/vishnu/Documents/vys.txt')



x=txt.flatMap(lambda line:line.split(" "))
y=x.map(lambda a:(a,1))
z=y.reduceByKey(lambda a,b:a+b)
q=z.reduce(lambda a,b:a if a[1]>b[1] else b)
print(q)
