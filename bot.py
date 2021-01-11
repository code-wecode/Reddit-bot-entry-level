import json
import praw

reddit = praw.Reddit("bot1")
FILE_NAME = "config.json"

def conf():
    with open(FILE_NAME) as file:
        file = json.load(file)
    return file

def subreddit_bot(subreddit, search_keywords, message_subject, message):
    for submission in reddit.subreddit(subreddit).stream.submissions():
        for word in search_keywords:
            if word in submission.title:
                reddit.redditor(submission.author.name).message(message_subject, message)
                break

def main():
    setting = conf()
    subreddit = setting["subreddit"]
    search_keyword = setting["search_keywords"]
    message_subject = setting["message_subject"]
    message = setting["message"]
    subreddit_bot(subreddit, search_keyword, message_subject, message)

if __name__ == "__main__":
    main()
