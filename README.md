# Project: Log Analysis

This project is part of the course "[Full Stack Web Developer Nanodegree Program](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004)".

The objective of this projects is to make a code using Python to answer 3 questions, based on a Database given by the course.

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## To run de code

You should have [python](https://www.python.org/) installed.

Just run this code on the terminal:

```bash
Python main.py
```

## Code for Views

### View created for Question 1

```SQL
create view most_accessed_articles as
select
  ar.title,
  count(l.path) as "views"
from
  articles ar,
  log l
where
  ar.slug = right(path, strpos('/article/', reverse(path)) - 9)
  group by l.path, ar.title
  order by  views desc
  limit 3;
```

### View created for Question 2

```SQL
create view most_accessed_authors as
select
  au.name,
  count(au.name) as "views"
from
  authors au,
  articles ar,
  log l
where
  ar.slug = right(path, strpos('/article/', reverse(path)) - 9)
  and ar.author = au.id
  group by au.name
  order by  views desc
  limit 3;
```

### Views created for Question 3

```SQL
create view total_views_per_day as
select date(time), count(date(time)) as views_per_day
from log
group by date(time)
order by date(time);

create view errors_views_per_day as
select date(time), count(date(time)) as errors_per_day
from log where status <> '200 ok'
group by date(time)
order by date(time);

create view percent_erros_per_day as
select total_views_per_day.date, (100.0 * errors_views_per_day.errors_per_day / total_views_per_day.views_per_day) as percent
from total_views_per_day, errors_views_per_day
where total_views_per_day.date = errors_views_per_day.date
order by total_views_per_day.date;
```
