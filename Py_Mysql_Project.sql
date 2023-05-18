create database Project;

create table employee(
id int primary key,
name varchar(30) not null,
salary int,
city varchar(20),
phone char(10) unique
);
desc employee;
select * from employee;
