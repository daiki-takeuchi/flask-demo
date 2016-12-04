drop table if exists customer;
drop table if exists orders;
drop table if exists order_detail;
drop table if exists payment;
drop table if exists product;
drop table if exists product_Line;


create table if not exists customer (
  id int not null auto_increment,
  customer_number int not null,
  customer_name varchar(124) not null,
  contact_last_name varchar(124) not null,
  contact_first_name varchar(124) not null,
  phone varchar(32),
  address_line1 varchar(124),
  address_line2 varchar(124),
  city varchar(32),
  state varchar(32),
  postal_code varchar(32),
  country varchar(32),
  sales_rep_employee_number int,
  credit_limit decimal(10,2),
  primary key (id)
) engine = INNODB;

create table if not exists orders (
  id int not null auto_increment,
  order_number int not null,
  order_date date not null,
  required_date date not null,
  shipped_date date,
  status varchar(32),
  comments varchar(256),
  customer_number int,
  primary key (id)
) engine = INNODB;

create table if not exists order_detail (
  id int not null auto_increment,
  order_number int not null,
  product_code varchar(32) not null,
  quantity_ordered int,
  price_each decimal(10,2),
  order_line_number int,
  primary key (id)
) engine = INNODB;

create table if not exists payment (
  id int not null auto_increment,
  customer_number int not null,
  check_number varchar(64) not null,
  payment_date date not null,
  amount decimal(10,2) not null,
  primary key (id)
) engine = INNODB;

create table if not exists product (
  id int not null auto_increment,
  product_code varchar(32) not null,
  product_name varchar(128) not null,
  product_line varchar(32) not null,
  product_scale varchar(32) not null,
  product_vendor varchar(64) not null,
  product_description varchar(1024),
  quantity_in_stock int,
  buy_price decimal(10,2),
  msrp decimal(10,2),
  primary key (id)
) engine = INNODB;

create table if not exists product_line (
  id int not null auto_increment,
  product_line varchar(32) not null,
  text_description varchar(1024),
  html_description varchar(1024),
  image varchar(1024),
  primary key (id)
) engine = INNODB;