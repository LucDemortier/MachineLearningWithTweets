# MachineLearningWithTweets
Project Fletcher for Spring 2015 Metis Data Science bootcamp (analysis of tweets with K-Means, LDA, MDS,...).
See blog post at [lucdemortier.github.io](http://lucdemortier.github.io/portfolio/4_fletcher.html) for a description of the results.

iPython notebooks and other files used to generate the results and plots for the Fletcher project:

1. **yoga_tweets.py**: Collects tweets from the Twitter API, filtering on the keyword "yoga", and stores them in a Mongo database.  Also uses TextBlob to do a quick sentiment analysis of each tweet.

1. **YogaTweetAnalysis.ipynb**: iPython notebook to read in the tweets from the Mongo database, clean them, and process them through Tf-Idf, Multi-Dimensional Scaling, K-Means clustering, and Latent Dirichlet Allocation topic modeling.
