
import matplotlib.pyplot as plt
import pandas as pd
import time

def plot_sentiment_over_time():
    while True:
        df = spark.sql("SELECT window.start as start_time, AVG(sentiment) as avg_sentiment FROM sentiment_over_time GROUP BY window.start ORDER BY window.start")
        pd_df = df.toPandas()

        plt.figure(figsize=(10, 5))
        plt.plot(pd_df['start_time'], pd_df['avg_sentiment'], marker='o', color='b')
        plt.title('Average Sentiment Over Time')
        plt.xlabel('Time')
        plt.ylabel('Average Sentiment')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        
        time.sleep(60)  # Update the plot every minute

if __name__ == "__main__":
    plot_sentiment_over_time()
    