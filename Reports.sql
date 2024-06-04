create procedure sales_in_a_City
@city varchar(max) 
as
 begin
 select o.order_id as 'Order Id',o.total_amount as 'Bill',o.date as 'Date',r.name as 'Name',r.email as 'Email',r.phone_number as 'Phone Numbers', r.city as 'City' from orders o inner join registered_users r on o.user_id=r.user_id where r.city=@city
end

exec sales_in_a_City @city='Lahore'
--2
create procedure top_sales_cities
as
begin
select top 10 r.city as 'City',sum(o.total_amount) as 'Total Sales' from registered_users r inner join orders o on o.user_id=r.user_id group by r.city order by sum(o.total_amount) desc
end

exec top_sales_cities

--3
create procedure top_rated_products
as
begin
select top 10 * from products order by rating desc
end

exec top_rated_products
--4
create procedure all_products_sales
as
begin

 select r.city as 'City' , p.name as 'Product' ,sum(i.quantity) as 'Total Units Sold' from  registered_users r 
 inner join orders o on  r.user_id=o.user_id inner join order_items i on i.order_id=o.order_id inner join
 products p on i.product_id=p.product_id  group by  r.city,p.name,i.quantity,p.product_id

 end
exec all_products_sales

--5

 create procedure most_sale_product_in_cities
 as 
 begin 

  select distinct  city,
  (select p.name from products p where product_id 
  in (select top 1 product_id from order_items where order_id in (select order_id from orders where user_id in(select user_id from registered_users where city=r.city) ) group by product_id order by sum(quantity) desc ) ) as 'Product Name',
   (select top 1 sum(quantity) from order_items where order_id in (select order_id from orders where user_id in(select user_id from registered_users where city=r.city) ) group by product_id order by sum(quantity) desc ) as 'Quantity'
  from registered_users r 

 end

 exec most_sale_product_in_cities

--6
create procedure top_customers_in_a_city
@city varchar(max)
as
begin

select top 10 name as 'Name' ,sum (o.total_amount) as 'Total Amount', count(o.order_id) as 'Total Orders' from registered_users r inner join orders o on r.user_id=o.user_id where city=@city group by r.name  order by sum(o.total_amount) desc 

end
exec top_customers_in_a_city @city='Okara'

--1
create view Total_Products_sold as
select p.name as 'Product Name',c.category_name as 'Category Name' ,sum(quantity) as 'Total Units Sold' from products p inner join order_items o on o.product_id=p.product_id inner join product_categories c on p.category_id= c.category_id
group by o.product_id,p.name,c.category_name 

select * from Total_Products_sold
--2
create view category_sales as
select c.category_name,sum(pa.after_discount) as 'Sales' from product_categories c
inner join products p on p.category_id=c.category_id inner join 
order_items o on o.product_id=p.product_id inner join payments pa
on pa.order_id=o.order_id
group by c.category_name

select * from category_sales

--3
create view Totalrevenue as
select sum(net_amount) as 'Revenue' from revenue

select * from Totalrevenue

--4
create view usage_of_shipping_method
as
select s.method as 'Method',count(s.shipping_id) as 'Number of Times Used' from shipping s inner join orders o
on o.shipping_id=s.shipping_id group by s.shipping_id,s.method

select * from usage_of_shipping_method
--5
create view best_retailers
as
select top 10 r.name,sum(rb.bill) as 'Total Purchase',sum(rb.discount) as 'Collective Discount (%)' from retailers r inner join retailers_bill rb on rb.retailer_id=r.retailer_id
group by r.name order by sum(rb.bill) desc

select * from best_retailers 


--1
CREATE VIEW reviews_of_product as
select p.name as 'Product Name', r.review as 'Reviews',r.rating as 'Rating' from reviews r  inner join products p on p.product_id=r.product_id

--2
create view customer_purchase as
select r.name as 'Name' ,p.after_discount 'Bill', o.order_id as 'Order ID',o.date as 'Order Date',p.date as 'Payment Date' from registered_users r inner join orders o on o.user_id=r.user_id inner join payments p on p.order_id=o.order_id

select * from customer_purchase
--3
create view product_purchased as
select p.name as 'Product',sum(quantity) as 'Quantity Purchased' from products p inner join retailers_bill r on r.product_id=p.product_id inner join inventory_audit i
on i.product_id=p.product_id group by p.name
select * from product_purchased


