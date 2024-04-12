
# Real-Time Slack Channel Message Processing

## Overview
This project analyzes sentiments of messages from a Slack channel in real-time and visualizes the sentiment trends over time.

## Setup
1. Install required packages: `pip install -r requirements.txt`.
2. Ensure you have Spark installed and properly configured.
3. Replace the placeholder tokens in the scripts with your actual Slack bot token and channel ID.

## Usage
- Run `spark_stream_processor.py` to start the streaming and processing of Slack messages.
- In a separate terminal, run `visualize_sentiments.py` to start the visualization of sentiment data.

## Note
Make sure to handle API rate limits and ensure compliance with data privacy regulations when accessing Slack messages.
    