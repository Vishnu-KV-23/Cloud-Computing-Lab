



from pyspark import SparkContext
sc=SparkContext('local','wordcount')
txt=sc.textFile('/home/vishnu/wordcounter.txt')

val=txt.flatMap(lambda line:line.split(","))

valm=val.map(lambda char:(char,1))
ls=valm.filter(lambda s:s[0]==s[0][::-1])
red=ls.reduceByKey(lambda a,b:a+b)

resu=red.collect()
for char,count in resu:
	print(f"palindromes\n{char}={count}")

