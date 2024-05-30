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
