create table registered_users(
    user_id int IDENTITY(1,1) primary key,
    name VARCHAR(100) not null,
    email VARCHAR(100) unique,
    password VARCHAR(100) not null,
    phone_number VARCHAR(20) unique
	 street_address VARCHAR(255) not null,
   city VARCHAR(100) not null,
   postal_code VARCHAR(20) ,
   country VARCHAR(100) not null,
); -- np

create table non_registered_users(
    name VARCHAR(100),
	cookie int primary key
); --np



create table product_categories(
   category_id int IDENTITY(1,1) primary key,
   catrogry_name varchar(100) not null
); --np


create table products(
   product_id int IDENTITY(1,1) primary key,
   name varchar(100) not null,
   category_id int,
   description varchar(max),
   price decimal not null,
   rating decimal
   Foreign key (category_id) references product_categories(category_id)
); --np




create table coupons(
  coupon_id int IDENTITY(1000,110) primary key,
  discount_percent decimal not null,
  start_date DATE,
  end_date DATE,
  limit int,
  status varchar(100)
);  --mv

create table shipping(
  shipping_id int IDENTITY(1,1) primary key,
  method varchar(100) not null,
  fees int,
); --np

create table orders(
   order_id int IDENTITY(1,1) primary key,
   user_id int,
   date DATE not null,
   time Time not null,
   total_amount int not null,
   coupon_id int,
   shipping_id int,
   payment_method varchar(100) not null,
   payment_status varchar(100) not null,

    Foreign key (user_id) references registered_users(user_id),
	Foreign key (coupon_id) references coupons(coupon_id),
	Foreign key (shipping_id) references shipping(shipping_id)
);



create table order_items(
   item_id int IDENTITY(1,1) primary key,
   order_id int,
   product_id int,
   qunatity int not null,
   amount int not null,

   Foreign key (product_id) references products(product_id),
   Foreign key (order_id) references orders(order_id)
);

create table order_tracking(
   tracking_id int IDENTITY(1,1) primary key,
   order_id int,
   status varchar(100) not null,
   date date,
   Foreign key (order_id) references orders(order_id)
);


create table payments(
   payment_id int IDENTITY(1,1) primary key,
   order_id int,
   total_amount int not null,
   after_discount int not null,
   date date not null,
   time TIME not null,

   Foreign key (order_id) references orders(order_id)
);




create table cart(
  cart_id int IDENTITY(1,1) primary key,
  user_id int,
  cookie int,
  total int,
  Foreign key (user_id) references registered_users(user_id),
  Foreign key (cookie) references non_registered_users(cookie),
);



create table cart_items(
  item_id int IDENTITY(1,1) primary key,
  product_id int,
  qunatity int,
  total int,
  cart_id int
  Foreign key (product_id) references products(product_id),
  Foreign key(cart_id) references cart(cart_id)
);

create table return_refunds(
    return_id int IDENTITY(1,1) primary key,
    user_id INT,
    product_id INT, 
	order_id int,
	qunatity int,
    reason VARCHAR(MAX) not null,
	date DATE,
	Foreign key (user_id) references registered_users(user_id),
	Foreign key (product_id) references products(product_id),
    Foreign key (order_id) references orders(order_id)
);

create table reviews(
  review_id int IDENTITY(1,1) primary key,
  product_id int,
  user_id int,
  rating decimal not null,
  review varchar(max),
  Foreign key (product_id) references products(product_id),
  Foreign key (user_id) references registered_users(user_id),
 );

create table prebooking(
  id int IDENTITY(1,1) primary key,
  user_id int,
  product_id int,
  date date,
  Foreign key (product_id) references products(product_id),
  Foreign key (user_id) references registered_users(user_id),

);

create table retailers(
   retailer_id int IDENTITY(1,1) primary key,
   name varchar(100) not null,
   discount decimal,
   phone varchar(25) unique 
);

create table inventory(
   id int IDENTITY(1,1) primary key,
   product_id int,
   qunatity int not null,
   retailer_id int,
   date_modified date,
    Foreign key (retailer_id) references retailers(retailer_id),
   Foreign key (product_id) references products(product_id)
); 

create table retailers_bill(
   bill_id int IDENTITY(1,1) primary key,
   retailer_id int,
   bill int,
   date DATE,
   product_id int,
   Foreign key (retailer_id) references retailers(retailer_id),
  Foreign key (product_id) references products(product_id)
);

create table income_expenditure(
   date DATE primary key,
   income decimal not null,
   expendtiure decimal not null,
   net_amount decimal
);

create table customer_support_tickets(
   ticketnumber int IDENTITY(100,10) primary key,
   user_id int,
   issue VARCHAR(MAX) not null,
   status varchar(max) 

   Foreign key (user_id) references registered_users(user_id)
);

