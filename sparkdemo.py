import sys
from pyspark import SparkContext, SparkConf

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: full_path\spark.py <file>", sys.stderr)
        exit(-1)
    conf = SparkConf().setAppName("spark").setMaster("local[8]")
    sc = SparkContext(conf=conf)
    lines = sc.textFile(sys.argv[1])

    counts = lines.flatMap(lambda x: x.split(' ')).map(lambda x: (x, 1)).reduceByKey(lambda x,y: x+y)
    output = counts.collect()
    for (word, count) in output:
        print (word.encode('utf-8'), count)

    sc.stop()