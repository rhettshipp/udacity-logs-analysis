#!/usr/bin/env python3

import psycopg2

# Set database
DBNAME = "news"


def get_query(query):
    """get_query takes an SQL query as a parameter. Executes the query and
    returns the results as a list of tuples."""
    try:
        connection = psycopg2.connect(database=DBNAME)
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
        connection.close()
    except psycopg2.Error as e:
        print("Unable to connect!")
        print(e.pgerror)
        print(e.diag.message_detail)
        sys.exit(1)


def print_top_articles():
    """Prints out the top 3 articles of all time."""

    popular_articles = """
    SELECT articles.title, count(log.path) AS views FROM articles, log
    WHERE log.path LIKE concat('%',articles.slug)
    AND log.status LIKE '200%'
    AND log.method = 'GET'
    GROUP BY articles.title
    ORDER BY views DESC
    LIMIT 3
    """

    top_articles = get_query(popular_articles)

    formatted_articles = "\n".join([("{} - {} views").format(title, numViews)
                                   for title, numViews in top_articles])

    print("\nThree most popular articles of all time: \n" + formatted_articles)


def print_top_authors():
    """Prints a list of authors ranked by article views."""

    popular_authors = """
    SELECT authors.name, count(log.path) AS views FROM authors, articles, log
    WHERE authors.id = articles.author
    AND log.path LIKE concat('%', articles.slug)
    GROUP BY authors.name
    ORDER BY views DESC
    """

    top_authors = get_query(popular_authors)

    formatted_authors = "\n".join([("{} - {} views").format(name, numViews)
                                  for name, numViews in top_authors])

    print("\nMost popular authors of all time: \n" + formatted_authors)


def print_errors_over_one():
    """Prints out the days where more than 1% of
    logged access requests were errors."""

    errors_over_one = """
    SELECT trim(to_char(errorstatus.day, 'Month')) || ' ' ||
    trim(to_char(errorstatus.day, 'dd, yyyy')) AS day
    ,round((100 * cast(errorstatus.total AS FLOAT)
    / cast(allstatus.total AS FLOAT))::numeric, 2) as percent
    FROM errorstatus
    JOIN allstatus on errorstatus.day = allstatus.day
    WHERE 100 * cast(errorstatus.total AS FLOAT)
    / cast(allstatus.total AS FLOAT) > 1
    GROUP BY errorstatus.day, percent
    """

    high_errors = get_query(errors_over_one)

    formatted_errors = "\n".join([("{} - {} %").format(day, percent)
                                 for day, percent in high_errors])

    print("\nDays with an error rate greater than 1 percent: \n" +
          formatted_errors)

if __name__ == '__main__':
    print_top_articles()
    print_top_authors()
    print_errors_over_one()
