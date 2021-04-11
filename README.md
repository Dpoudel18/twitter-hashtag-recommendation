# Hashtag Recommendation

Design and evaluation of content-based hashtag recommendation models for Twitter.

## Software Architecture Diagram

![](images/final_final.jpg?raw=true)

## Description of source code

```
tweet_api.py - API connection using valid keys and tokens.
extract_keywords - Pre-processing step.
hashtag_frequency.py - Implementation of TF-IDF model.
naive_bayes.py - Implementation of Naive Bayes model.
cosine_similarity.py - Implementation of Cosine Similarity model.
streamlit_web_application.py - Code for building Streamlit web application.
evaluation.py - Algorithm to calculate all 5 evaluation metrics.
get_data.py - Connection to PostgreSQL database
```


## Requirements

Make sure to have Python 3 installed in your computer!

Make sure to have Tweepy and Streamlit library installed in your computer!

    pip install Tweepy

    pip install Streamlit

Also, you need to have a valid Twitter API key and token to successfuly run this program.

## How to run the Program

Open your terminal and run this command:

    streamlit run streamlit_web_application.py
