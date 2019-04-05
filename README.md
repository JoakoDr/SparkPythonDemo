# SparkPythonDemo
Little example of how to use Spark Command with a project in Python (read a Json, wordCount of a local file)

---------------------------------------------SPARK PYTHON DEMO------------------------------------------------

First thing i have to say is that i use Python 3.7.3, so if you dont have this version, don't try to do it because it's impossible to 
compile without any trouble.

Open PyCharm IDE, write or copy the program that i have in this repository, before this open cmd, go to the spark directory and if you
want to see the results in the cmd you have to write this command: 
"spark-submit --master local[8] PATHofTheFile\PycharmProjects\Spark\jsonRead.py"

With this version of Python urllib2 is deprecated but exits urllib3 that works faster and better, so you have to install the package of urllib3 in your path file of Python3.7.3/Python/Scripts and then run "pip install urllib3" and then you will see a message "Download completed", then restart the IDE(works fine if you dont restart too)  , then you could run this programs.

THANK YOU SO MUCH!!!!!!!
