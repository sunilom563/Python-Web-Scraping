# Python-Web-Scraping  using BeautifulSoup library


##  Technical Requirements 
1. Python3 
2. PostgreSQL Database

## Libraries
1. BeautifulSoup4
2. Requests
3. psycopg2

## Setup Dev Environment
1. Run ```git clone https://github.com/sunilom563/Python-Web-Scraping.git```
2. Run ```cd Python-Web-Scraping```

## How To Install Libraries
Run ```pip install requests beautifulsoup4 psycopg2```

## How To Create Table
Run Query 
```
   CREATE TABLE "public"."webpage" ( 
	"id" INT GENERATED ALWAYS AS IDENTITY NOT NULL,
	"title" Text,
	"subtitle" Text,
	"abstract" Text,
	"download" Text );
  ```
  
## How To Run Dev Server
Run ```final.py```
  
  
  
  
  
