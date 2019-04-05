import sys
import urllib3
import json
from pyspark import SparkContext, SparkConf
from urllib.parse import urlencode

if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("Usage: full_path\ReadJSON.py", sys.stderr)
        #In my case "spark-submit --master local[8] C:\Users\joaquin.diaz.ramirez\PycharmProjects\Spark\jsonRead.py"
        exit(-1)

    conf = SparkConf().setAppName("WordCount").setMaster("local[8]")
    sc = SparkContext(conf=conf)
    print(str(sys.argv))
    url = "https://randomuser.me/api/?results=100"
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    encoded_args = urlencode({'nombre': ['name']})
    data = json.loads(r.data.decode('utf-8'))
    for users in data['results']:
        print(users['name']['first'])

    sc.stop()