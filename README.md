# Project: Log Analysis

This project is part of the course "[Full Stack Web Developer Nanodegree Program](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004)".

The objective of this projects is to make a code using Python to answer 3 questions, based on a Database given by the course.

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Prerequisites

Download VMbox [here](https://www.virtualbox.org/wiki/Downloads) and install it. This may [help](https://www.virtualbox.org/manual/ch02.html) you.

Download VagrantMachine [here](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip).

Change to the directory after you unzip the file in your terminal with ```cd```. Inside, you will find another directory called vagrant. Change directory to the vagrant directory, and use the command ```vagrant up``` to create the machine.

This machine already has:
  1. postgresql
  2. python3
  3. python
  
After the machine is done you can access it using the command ```vagrant ssh```.
  
Download file to create Database [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).

The file inside is called **newsdata.sql**. Put this file into the **vagrant** directory, which is shared with your virtual machine.

To load the data, ```cd``` into the vagrant directory and use the command ```psql -d news -f newsdata.sql```.
Here's what this command does:

* psql — the PostgreSQL command line program
* -d news — connect to the database named news which has been set up for you
* -f newsdata.sql — run the SQL statements in the file newsdata.sql

_Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data._



## To run de code

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
