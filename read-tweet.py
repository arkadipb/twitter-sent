# Databricks notebook source
mongo_pwd = <>

##maven coordinate   ---    org.mongodb.spark:mongo-spark-connector_2.12:3.0.1

# COMMAND ----------

from pyspark.sql import SparkSession, SQLContext
from pyspark import SparkConf, SparkContext
import pyspark
spark = SparkSession \
    .builder \
    .appName("mongodbtest1") \
    .config("spark.mongodb.input.uri", "mongodb+srv://rw_user:"+mongo_pwd+"@clustertest.6jkle.mongodb.net/tweets.tbl_tweet?retryWrites=true&w=majority") \
    .config("spark.mongodb.output.uri", "mongodb+srv://rw_user:"+mongo_pwd+"@clustertest.6jkle.mongodb.net/tweets.tbl_tweet?retryWrites=true&w=majority") \
    .config('spark.jars.packages', 'org.mongodb.spark:mongo-spark-connector_2.12:3.0.1') \
    .getOrCreate()


# COMMAND ----------

df = spark.read.format("com.mongodb.spark.sql.DefaultSource").option("Database", "tweets").option("Collection", "tbl_tweet").option("uri", "mongodb+srv://rw_user:"+mongo_pwd+"@clustertest.6jkle.mongodb.net/tweets.tbl_tweet?retryWrites=true&w=majority").load()

# COMMAND ----------

df.count()

# COMMAND ----------


