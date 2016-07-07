#!/usr/bin/python

import os
import yaml

with open('../config.yaml', 'r') as f:
    conf = yaml.load(f)
user = conf['psql']['user']
os.environ["SPARK_HOME"] = conf['psql']['sparkHome']
os.environ["SPARK_CLASSPATH"] = conf['psql']['sparkClass']

from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext

sc = SparkContext("local", "Simple App")
sqlContext = SQLContext(sc)
df = sqlContext.load(
    url = "jdbc:postgresql://localhost/%s" % (user),
    dbtable = "iraq",
    password = "",
    user =  user,
    source = "jdbc",
    driver = "org.postgresql.Driver"
)

print('\n\n\nJob Started!')
df.show()
print('Job Finished!\n\n\n')
sc.stop()
