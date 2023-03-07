from pyspark import SparkConf, SparkContext
import string

conf = SparkConf().setMaster('local').setAppName('WordCount')
sc = SparkContext(conf = conf)

RDDvar = sc.textFile("input.txt")

words = RDDvar.flatMap(lambda line: line.split())

result = words.map(lambda word: (str(word.lower()).translate(None,string.punctuation),1))

aggreg1 = result.reduceByKey(lambda a, b: a+b)

aggreg1.saveAsTextFile("output.txt")