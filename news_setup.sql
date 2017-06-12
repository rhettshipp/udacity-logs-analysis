DROP DATABASE IF EXISTS news;

CREATE DATABASE news;

\c news

\i newsdata.sql

CREATE VIEW errorstatus AS
    SELECT date_trunc('day',time) AS day, count(status) AS total
    FROM log
    WHERE status LIKE '%4%'
    GROUP BY day;

CREATE VIEW allstatus AS
    SELECT date_trunc('day',time) AS day, count(status) AS total
    FROM log
    GROUP BY day;
