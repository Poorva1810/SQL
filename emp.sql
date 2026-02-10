create table if not EXISTS empl(
Eno char(3),
Ename varchar(15),
age int(2),
gen char(1),
sal int(7),
exp int(2),
loc varchar(15),
dno char(3),
);

insert into empl VALUES
('E01','tenzin',32,'M',50000,2,'Delhi','D03'),
('E02','san',39,'M',400000,8,null,'D02'),
('E03','mady',27,'F',300000,4,'Mumbai','D01'),
('E04','prag',43,'M',500000,3,'Mumbai','D03'),
('E05','mahi',21,'F',450000,5,'Pune','D02')
;
