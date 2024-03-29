import re
import os
import sys
from pyspark.sql import SparkSession
import json

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable


sp = SparkSession.builder \
    .appName("Top20HashtagCounter") \
    .getOrCreate()


def read_data(file_location):
    with open(file_location, 'r', encoding='utf-8') as file:
        return json.load(file)


def mapper(json_data):
    mapped_data = []

    def extract_hashtags(data):
        if isinstance(data, dict):
            for value in data.values():
                extract_hashtags(value)
        elif isinstance(data, list):
            for item in data:
                extract_hashtags(item)
        elif isinstance(data, str):
            hashtags = re.findall(r"#\w+", data.lower())
            for hashtag in hashtags:
                mapped_data.append((hashtag, 1))

    extract_hashtags(json_data)
    return mapped_data

file_location = 's3://p2-inputdata/smallTwitter.json'


json_rdd = sp.read.text(file_location).rdd.map(lambda row: row.value)


mapped = json_rdd.flatMap(mapper)


reduced = mapped.reduceByKey(lambda a, b: a + b)


hashtags_20 = reduced.takeOrdered(20, key=lambda x: -x[1])
output = "\n".join([f"{hashtag} {count}" for hashtag, count in hashtags_20])
print(output)


output_location = "s3://cloudcomputingvt/Prathyusha/p2-group9-output.txt"


sp.sparkContext.parallelize([output]).saveAsTextFile(output_location)


sp.stop()