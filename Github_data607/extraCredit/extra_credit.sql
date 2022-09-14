DROP TABLE IF EXISTS APPL_STOCK;
-- The MySQL database is about APPLE(AAPL) stock price for the year 2022. The data is extracting from YAHOO FINANCE in CSV format. 
-- link to YAHOO FINANCE: https://finance.yahoo.com/quote/AAPL/history?period1=1640995200&period2=1662940800&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true
-- date range is from 2022-01-03 till 2022-09-09 and date format is YYYY-MM-DD

-- Creating table with column name matching to the dataset
CREATE TABLE APPL_STOCK (
DATE VARCHAR(50), 
OPEN DECIMAL(6,2),
HIGH DECIMAL(6,2), 
LOW DECIMAL(6,2), 
CLOSE DECIMAL(6,2),
ADJ_CLOSE DECIMAL(6,2),
VOLUME INT
);

-- loading data from the csv to table. The csv file has its header so I have used IGNORE to omit 1st line
LOAD DATA LOCAL INFILE '/Users/karmagyatso/Documents/cunySps/data607/week_3/extraCredit/AAPL.csv'
INTO TABLE APPL_STOCK
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

select * from APPL_STOCK;


-- using CTE(Common Table Expression) syntax. CTE is a named temporary result set that exists within the scope of a single statement and that can be referred to later within that statement, possibly multiple times. 
-- source: https://dev.mysql.com/doc/refman/8.0/en/with.html

-- in this CTE code block, we are taking avg of close column. 
-- YEAR_TO_DAY_AVG calculates the average in total with the year 2022.
-- MONTLY_AVG displays average of CLOSE column on a montly basis. We can see the avg stock price of AAPL of every month. 
-- SIX_DAY_AVG is calculated using window frame bounds with ROWS. we are calculating six day moving avg, 5 PRECEDING MEANING 5 DAYS AFTER CURRENT LOW(LATEST). 
WITH AVG_CLOSE AS (
select DATE, open, high, low, close, adj_close, volume, 
AVG(CLOSE) over(partition by YEAR(DATE)) as YEAR_TO_DAY_AVG,
AVG(CLOSE) over(partition by month(DATE)) as MONTHLY_AVG,
AVG(CLOSE) OVER(PARTITION BY DAY(DATE) ROWS BETWEEN 5 PRECEDING AND CURRENT ROW) AS SIX_DAY_AVG
 from appl_stock
 order by date DESC
 )
 SELECT DATE, close, CAST(YEAR_TO_DAY_AVG AS DECIMAL(6,2)) AS YEAR_TO_DAY_AVG, CAST(MONTHLY_AVG AS DECIMAL(6,2)) AS MONTHLY_AVG, cast(SIX_DAY_AVG as DECIMAL(6,2)) AS SIX_DAY_AVG FROM AVG_CLOSE;
 
