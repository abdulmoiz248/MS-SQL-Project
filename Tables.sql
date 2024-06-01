create table registered_users(
    user_id int IDENTITY(1,1) primary key,
    name VARCHAR(100) not null,
    email VARCHAR(100) unique,
    password VARCHAR(100) not null,
    phone_number VARCHAR(20) unique,
	 street_address VARCHAR(255) not null,
    city VARCHAR(100) not null,
    postal_code VARCHAR(20) ,
    country VARCHAR(100) not null,
	gender char
); 

create table non_registered_users(
    name VARCHAR(100),
	cookie int primary key
); 

create table product_categories(
   category_id int IDENTITY(1,1) primary key,
   category_name varchar(100) not null
); 

create table products(
   product_id int IDENTITY(1,1) primary key,
   name varchar(100) not null,
   category_id int,
   description varchar(max),
   price decimal not null,
   rating decimal
   Foreign key (category_id) references product_categories(category_id)
); 
create table retailers(
   retailer_id int IDENTITY(1,1) primary key,
   name varchar(100) not null,
   phone varchar(25) unique 
);
create table inventory(
   id int IDENTITY(1,1) primary key,
   product_id int,
   quantity int not null,
   retailer_id int,
   date_modified date,
    Foreign key (retailer_id) references retailers(retailer_id),
   Foreign key (product_id) references products(product_id)
); 
create table retailers_bill(
   bill_id int IDENTITY(1,1) primary key,
   retailer_id int,
   bill int,
   discount decimal,
   date DATE,
   product_id int,
   Foreign key (retailer_id) references retailers(retailer_id),
  Foreign key (product_id) references products(product_id)
);

create table revenue(
   date DATE primary key,
   income decimal not null,
   expendtiure decimal not null,
   net_amount decimal
); --autocalculate

create table prebooking(
  id int IDENTITY(1,1) primary key,
  user_id int,
  product_id int,
  date date,
  Foreign key (product_id) references products(product_id),
  Foreign key (user_id) references registered_users(user_id),

); 
create table coupons(
  coupon_id int IDENTITY(1000,110) primary key,
  discount_percent decimal not null,
  start_date DATE,
  end_date DATE,
  limit int,
);
create table shipping(
  shipping_id int IDENTITY(1,1) primary key,
  method varchar(100) not null,
  fees int,
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
