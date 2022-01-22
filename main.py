import praw
import requests
import random


folder_name = #Name of the folder you want to store your memes
SUBREDDIT_NAME = #Name of the subreddit from which you want to get memes
NO_OF_MEMES = #No of memes.
LIMIT = #The amount of memes do you want to select from

def image_check(link):
    """
    To check if the link is an img
    """

    IMG = {'jpg', 'jpeg', 'png'}
    for i in IMG:
        if link.endswith(i):
            return True

# create an application here - https://www.reddit.com/prefs/apps to get access to this
reddit = praw.Reddit(
            client_id = "",
            client_secret = "",
            username = "", 
            user_agent = "",
)

INVALID_SYM = (",", ".", "'", "*", "?", "/", "_", '"', "!")

subreddit = reddit.subreddit(SUBREDDIT_NAME)
lim = subreddit.top(limit=LIMIT)
all_sub = [i for i in lim]


submission = random.sample(all_sub, NO_OF_MEMES)
for i in range(NO_OF_MEMES):
    url = submission[i].url
    title = submission[i].title
    
    for j in title:
        if j in INVALID_SYM:
            title = title.replace(j, "-")    
    
    #if image_check(url) == True:      --> you can enable this you dont want to download .gif
    print(f"{i+1}. {url}")
    r = requests.get(url).content
    with open(f"{folder_name}/{title}.jpg", "wb+") as f:
        f.write(r)
