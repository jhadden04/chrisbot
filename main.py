import praw
import time
reddit = praw.Reddit(client_id='*',
                     client_secret='*',
                     user_agent='a reddit instance',
                     username='*',
                     password='*')


def imageposter():
    n = 0
    while True:
        subreddits = ["Johntesting"] # you can add to this/change it

        titles = ["change this"]  # you must change this to your desired title
        reddit.validate_on_submit = True
        text = ["change this"]  # you must change this to the text
        flairtext = ["hello"]
        subreddit = reddit.subreddit(subreddits[n])
        try:
            submission = subreddit.submit(title= titles[0], selftext = text[0])
            choices = submission.flair.choices()
            template_id = next(x for x in choices if x["flair_text_editable"])["flair_template_id"]
            submission.flair.select(template_id, "hello")  # change the hello to change the flair of the post

        except Exception as e:
            print(e)
            time.sleep(900)
            continue
        print(f'posted on r/{subreddit}')
        n += 1
        if n >= len(subreddits):
            n = 0
        time.sleep(900) # you can change this interval which is measured in seconds
        # for example this currently posts once every 15mins (900 seconds)
imageposter()
