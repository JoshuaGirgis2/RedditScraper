
import praw
import pandas
import sqlite3
from sqlalchemy import create_engine


client_id = 'gVW0D3NbK0TSPQ5eDm7NjQ'
client_secret = 'wVsQXiPy_5xQabHk5z6tfFP7qEaPtw'
user_agent = 'main'

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent
)
subreddit_name = 'berkeley'
subreddit = reddit.subreddit(subreddit_name)

data = []
for submission in subreddit.hot(limit=10):
    data.append({
    "title": submission.title,
   "score": submission.score,
    "URL": submission.url,
    "created_utc": submission.created_utc })

dataFrame = pandas.DataFrame(data)

dataFrame.to_csv("reddit_posts.csv", index=False)

#dataFrame.to_excel("reddit_posts.xlsx", index=False)

engine = create_engine('sqlite:///reddit_posts.db')
dataFrame.to_sql('posts',con = engine, if_exists='replace',index = False)
