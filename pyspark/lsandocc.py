from pyspark import SparkContext
sc=SparkContext('local','linear')
txt=sc.textFile('/home/vishnu/Documents/vys.txt')


val=txt.flatMap(lambda line:list(line.replace(" ","")))
valm=val.map(lambda x:(x,1))
reducer=valm.reduceByKey(lambda a,b:a+b)
res=reducer.collect()
print(res)
tar='h'
ls=val.filter(lambda x:x==tar).count()

print(f"the linear search outcome is {ls}")

