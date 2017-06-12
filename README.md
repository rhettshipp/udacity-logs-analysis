# Logs Analysis Project

This project analyzes the authors, articles and logs tables in the news database. The logs_analysis.py file is to be run in the terminal and provides answers to three questions:

1-What are the three most popular articles of all time?

2-Who are the most popular authors of all time?

3-On which days did more than 1% of requests lead to errors?

## Getting Started
First, you'll need to setup the news database. To do so, download the newsdata.sql
file here:

https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

After downloading, include the newsdata.sql file in the Udacity-Logs-Project folder. Then run following terminal command:

psql -f news_setup.sql

Simply run "python3 logs_analysis.py" after setting up the news database. The answers to the three above questions will be printed to the terminal window.

## Author

* **Rhett Shipp**
