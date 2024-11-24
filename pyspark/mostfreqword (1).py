
from pyspark import SparkContext
sc=SparkContext('local','wordcount')
txt=sc.textFile('/home/vishnu/Documents/vys.txt')
val=txt.flatMap(lambda line: line.split(" "))
valm=val.map(lambda x:(x,1))
r=valm.reduceByKey(lambda a,b:a+b)
re=r.reduce(lambda a,b : a if a[1]>b[1] else b)

print(f"\n{re[0]}=>{re[1]}")
sc.stop()
