-- How many taxi trips were totally made on September 18th 2019?
SELECT
    count(*)
FROM
    taxi
where
    lpep_pickup_datetime >= '2019-09-18 00:00:00'
    and lpep_dropoff_datetime <= '2019-09-18 23:59:59';

-- Which was the pick up day with the largest trip distance Use the pick up time for your calculations.
select
    lpep_pickup_datetime,
    sum(trip_distance)
from
    taxi
group by
    1
order by
    2 desc
limit
    1;

-- Consider lpep_pickup_datetime in '2019-09-18' and ignoring Borough has Unknown
-- Which were the 3 pick up Boroughs that had a sum of total_amount superior to 50000?
select
    z."Borough",
    sum(t.total_amount)
from
    taxi t
    left join zone z on t."PULocationID" = z."LocationID"
where
    lpep_pickup_datetime :: date = '2019-09-18'
group by
    1
having
    sum(t.total_amount) > 50000
order by
    2 desc;

-- For the passengers picked up in September 2019 in the zone name Astoria which was the drop off zone that had the largest tip? We want the name of the zone, not the id.
SELECT
    Zp."Zone" as pickup,
    Zd."Zone" as dropoff,
    T.tip_amount
FROM
    TAXI T
    LEFT JOIN ZONE Zp ON T."PULocationID" = Zp."LocationID"
    LEft join zone Zd ON T."DOLocationID" = Zd."LocationID"
where
    Zp."Zone" = 'Astoria'
    and EXTRACT(
        month
        from
            LPEP_PICKUP_DATETIME :: date
    ) = '9'
    and EXTRACT(
        year
        from
            LPEP_PICKUP_DATETIME :: date
    ) = '2019'
ORDER BY
    t.tip_amount DESC
limit
    1