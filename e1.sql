create table if not EXISTS empl(

Eno char(3),

Ename varchar(15),

age int(2),

gen char(1),

sal int(7),

exp int(2),

loc varchar(15),

dno char(3)

);

insert into empl VALUES

('E01','Tenzin',32,'M',50000,2,'Delhi','D03'),

('E02','San',39,'M',40000,8,NULL,'D02'),

('E03','Mady',27,'F',30000,4,'Mumbai','D01'),

('E04','Arnold',50,'M',50000,9,'Delhi','D02'),

('E05','Prag',43,'M',50000,3,'Mumbai','D04'),

('E06','Sana',38,'F',37000,0,'Pune','D03'),

('E07','Aari',27,'F',48000,1,NULL,'D04'),

('E08','Prabh',40,'M',72000,6,'Pune','D01'),

('E09','Mahi',21,'F',54000,5,'Mumbai','D03')

;

select * from empl;
#display the name and age of employees whose age is more than 30
select ename 
from empl;
select ename,age 
from empl 
where age>30;

#display names of female employees
select Ename
from empl
where gen='F';

#display the employees which are starting with either A or S
select Ename 
from empl 
where ename 
like 'A%' or ename like 'S%';

#display maximum age and minimum experience of the employees whose names are endig with i or a
select max(Age),min(Exp)
from empl
where ename like '%A' or ename like'%I';

#display maximum age for the male employees whose names are more than 3 characters long
select max(age)
from empl
where gen='M' and ename like'____%';

# display the names of female employees in whose name is anywhere and either experience is more than 1 year or age
select Ename 
from empl 
where gen='F' and ename like '%i%' and (exp>1 or age<40);
select *from empl;

#display maximum experience of male employees working in either D01 or D03 departments
select max(exp)
from empl where gen='m'and(dno='D01'or dno='D03');

#display names of employees whose age is more than 30 and names have n or a as 3RD character
select ename
from empl 
where age>30 and(ename like'__n%' or ename like '__m%');

#display average age for female employees
select avg(age)
from empl
where gen='F'

#display unique department numbers in which the employees are working
select dno
from empl;

#display employee number for those employees whose age is between 30 to 40 and working in departmentD01 or D03
select ename 
from empl 
where (age<40 and age>30);

#display employee number and name for those male employees whose experience is more than 5 years and names at least 4 characters long.
select Ename,Eno
from empl
where (exp>5 and Ename like '____%');

#display names of employees whose names have 'a' as charcter and age is less than 40
select Ename 
from empl
where Ename like '%a%' and (age<40);

--display the employee details in asceding order of age
select*
from empl
order by age asc;
--display names of male emplotees in descending order of ther experience
select Ename
from empl
where gen='M'
order by exp desc;
--display employee number and name in ascending order of their salary whose age is more than 30
select eno, Ename
from empl
where age>30
order by sal asc;
--display the maximum age and minimum salary for males and females.age
select max(age),min(sal),gen
from empl
group by gen; 
--display minimum age and maximum salary for employees working in each department
select min(age),max(sal),dno
from empl
group by dno;
--display total experience of employee coming from differentlocation
select sum(exp),loc
from empl
group by loc;
-- display name and age of employees whose location is not mentioned and whose names are more than 4 charecters long
select Ename,age,loc
from empl
where loc is null and Ename like'____%';

--display name,age,location and employee number of theemployees whose names  contain a or e anywhere and age between 30 to 40 and location is mentioned
select ename,age,loc,Eno
from empl
where(ename like'%a%' or ename like '%e%') and age between 30 and 40 and loc is not null;

--display name,gen,salary of those female employees whose salary is not more than 50000 and age between 30 to 40
select Ename,gen,sal,age
from empl
where gen='F' and sal<=50000 and age BETWEEN 30 and 40;
--display employee number and name of those employees whose location is not mentioned but experience is mantioned and names starts or ends with vowel
select eno, ename,loc, exp

from empl

where loc is null and exp is not null and (ename like 'A%' or ename like 'O%' or ename like 'I%' or ename like 'E%' or ename like 'U%') and (ename like '%a' or ename like '%o' or ename like '%i' or ename like '%e' or ename like '%u'); 
--display employee number and name of those employees whose age is mentioned and it should be atleast 30 and salary should be atleast 40000
select Eno,Ename,age,sal
from empl 
where  age is not null and age>=30 and sal>=40000;

--display non repeated locations for male employees whose age is more than 40 in ascending order of age 
select loc
from empl
where DISTINCT loc and gen='M'(age>40)
order by age asc;
--display name and age of employees who is coming from Mumbai or Delhi and whose salary is not less than 40000
select Ename,age
from empl
where loc is Mumbai or Delhi and (sal>=4000);
--display age and employee number of female employees whose salary is between 40 to50 thousand and age is less than 40 and names are more than 3charcaters long
select age,Eno
from empl
where gen='F' and sal BETWEEN 40000 and 50000 and (age<40) and Ename like '___%';