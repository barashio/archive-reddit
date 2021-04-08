import praw
import pprint
from fpdf import FPDF
from datetime import datetime

reddit = praw.Reddit(
    client_id="",
    client_secret="",
    password="",
    user_agent="",
    username="",
)

for submission in reddit.subreddit("DataHoarder").hot(limit=25):
    # pprint.pprint(vars(submission)) # use this to see all available response values

    title = submission.title.encode('latin-1', 'replace').decode('latin-1')
    author = submission.author
    ups = submission.ups
    num_comments = submission.num_comments
    created = datetime.fromtimestamp(submission.created)
    subreddit = submission.subreddit
    url = submission.url
    summary = "\nAuthor: {0}\nUpvotes: {1}\nComments: {2}\nDate: {3}\nSubreddit: {4}\nLink: {5}\n\n".format(author, ups, num_comments, created, subreddit, url)
    selftext = submission.selftext.encode('latin-1', 'replace').decode('latin-1')

    pdf = FPDF(orientation = 'P', unit = 'mm', format='A4')
    pdf.add_page()
    pdf.set_font("Arial", 'B', size = 13)
    pdf.multi_cell(w = 0, h = 5, txt = str(title), border = 0, align = 'L', fill = False)
    pdf.set_font("Arial", 'I', size = 9)
    pdf.multi_cell(w = 0, h = 5, txt = str(summary), border = 0, align = 'L', fill = False)
    pdf.set_font("Arial", size = 10)
    pdf.multi_cell(w = 0, h = 5, txt = str(selftext), border = 0, align = 'L', fill = False)
    pdf.output("data/{}.pdf".format(submission)) 
    
