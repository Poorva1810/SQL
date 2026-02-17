create table if not EXISTS studt(

Sno char(3),

Sname varchar(15),

Sage int(2),

gen char(1),

loc varchar(15),


);

insert into studt VALUES

('E01','Priya',16,'F','Delhi'),

('E02','Maya',15,'F',NULL),

('E03','Dharmi',17,'F','Mumbai'),

('E04','Sneha',17,'F','Delhi')
;
select * from studt;