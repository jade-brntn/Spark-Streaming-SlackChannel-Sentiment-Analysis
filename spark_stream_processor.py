
from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp, udf, window, col
from pyspark.streaming import StreamingContext
from slack_sdk import WebClient
from textblob import TextBlob

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("Slack Stream Processing with Sentiment Analysis") \
    .config("spark.sql.shuffle.partitions", "1") \
    .getOrCreate()
sc = spark.sparkContext
ssc = StreamingContext(sc, 10)  # 10 seconds window

# Define UDF for sentiment analysis
@udf(returnType='float')
def analyze_sentiment(text):
    return TextBlob(text).sentiment.polarity

# Function to collect messages from Slack
def collect_messages():
    client = WebClient(token='xoxb-your-slack-bot-token')
    response = client.conversations_history(channel='your-channel-id')
    messages = [(msg['text'], current_timestamp()) for msg in response['messages']]
    return sc.parallelize(messages)

# Function to process RDDs
def process_rdd(rdd):
    if not rdd.isEmpty():
        df = spark.createDataFrame(rdd, schema=["text", "timestamp"])
        df = df.withColumn("sentiment", analyze_sentiment(df["text"]))
        df.groupBy(window(df.timestamp, "10 minutes")).avg("sentiment").write.format("memory").mode("append").saveAsTable("sentiment_over_time")

# Setup the DStream
slack_stream = ssc.queueStream([], default=collect_messages())
slack_stream.foreachRDD(process_rdd)

# Start Streaming
ssc.start()
ssc.awaitTermination()
    