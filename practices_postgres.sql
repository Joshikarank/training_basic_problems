-- Active: 1707114443826@@127.0.0.1@5432@practices@public
create table person
(id int PRIMARY key,
namess VARCHAR(10),
age VARCHAR(3),
car_id INT);

CREATE Table car
(id int PRIMARY key,
model VARCHAR(10),
purchase_date VARCHAR(20),
price VARCHAR(10) );


INSERT into car
VALUES (1,'Tesla','2019-01-01','2323343'),
(2,'BMW', '2019-02-01','45345535'),
(3,'Ferrari', '2019-03-01','34532245');

insert INTO person
VALUES (1,'John', '25', '1'),
(2,'Alice', '30', '3'),
(3,'Max', '28','2');


--implementing JOIN
SELECT * from person 
JOIN car 
on person.car_id = car.id;

SELECT * FROM person
INNER JOIN car ON person.car_id = car.id;


SELECT * FROM person
LEFT JOIN car ON person.car_id = car.id;

SELECT * FROM person
RIGHT JOIN car ON person.car_id = car.id;

SELECT * FROM person
FULL JOIN car ON person.car_id = car.id;

SELECT * FROM person
CROSS JOIN car;


