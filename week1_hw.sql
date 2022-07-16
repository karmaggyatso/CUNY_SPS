
-- Q1
select max(distance), flight from flights
group by flight
order by max(distance) desc limit 1;


-- Q2

select distinct(engines) from planes;

select max(seats), engines from planes  
where (select max(distinct(engines)) from planes)
group by engines;

    
-- Q3
select count(*) from flights  ;

-- Q4
select count(*), carrier from flights  
group by carrier;

-- Q5
select flight, carrier from flights  
order by flight desc;

-- Q6

select flight, carrier from flights  
order by flight desc limit 5;

-- Q7
select flight, carrier, distance from flights where distance >= 1000
order by flight desc;

-- Q8

-- calculate the average distance travel by an aircraft(carrier name)
select avg(distance), carrier from flights
group by carrier