from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS
import sqlite3

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def getPosts():
    connect = sqlite3.connect('reddit_posts.db')
    cursor = connect.cursor()
    cursor.execute('SELECT title, score, url, created_utc FROM posts')
    rows = cursor.fetchall()

    posts = []
    for row in rows:
        post = {
            "title": row[0],
            "score": row[1],
            "url": row[2],
            "created_utc": row[3]
        }
        posts.append(post)
    connect.close()
    return posts

@app.route('/api/reddit_posts', methods=['GET'])
def reddit_posts():
    posts = getPosts()
    return jsonify(posts)

if __name__ == '__main__':
    app.run(debug=True)
