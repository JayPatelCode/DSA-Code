
-- select
-- from shipments s
-- join person p on p.product_id = s.product_id 


-- select s.date, s.sales_person, p.team, s.amount
-- from shipments s
-- join people p on p.sp_id = s.sp_id

--  select
--  from shipments s
--  join  products pr.product_id = s.product_id
--  where pr.category= "Bars"



-- select
-- from shipments s
-- join product p on p.product_id=s.product_id


-- select p.amount, p.mode
-- from customer as c
-- join payment as p on c.customer_id=p.customer_id
-- where c.first_name = "Madan"



-- here we join 2 tables in first join we use 2 tables that is shipments and 
-- people which we connect using same column in both table that is sp_id 
-- and for second join we use products table where we connect using prouct_id and 
-- instead of using where clause we can directly connect it to the join using and clause.
select 
from shipments s
join people p on p.sp_id = s.sp_id and p.sales_person = "Barr Faughny"
join products pr on pr.product_id = s.product_id and pr.category = "Barrs"


-- we can do above query using where clause and we can apply order by so that higher order is on top and reduces as it moves down
select 
from shipments s
join persons p on p.sp_id = s.sp_id
join products pr on pr.product_id = s.product_id 
where p.sales_person = "Barr Faughny" and pr.category = "Barrs"
order by s.amount desc


-- bar bar shipmennts grouped by month
select format(s.date, 'MMM yy') as "Month", sum(s.amount) "Sales", sum(s.boxes) "boxes"
from shipements s
join people p on p.sp_id = s.sp_id
join products pr on pr.product_id = s.product_id
where p.sales_person = "Barr Faughny" and pr.category = "Barrs"
group by format(s.date, "MMM yy")