drop database  itcast;

create database itcast default character set utf8;

use itcast;

create table it_user_info(
   ui_user_id bigint unsigned  auto_increment comment '用户ID',
   ui_name varchar(64) not null comment '用户名',
   ui_passwd varchar(128) not null comment '密码',
   ui_age int unsigned null comment '年龄', 
   ui_mobile char(11) not null comment '手机号',
   ui_avatar varchar(128) null comment '头像',
   ui_ctime datetime not null default current_timestamp comment '创建时间',
   ui_utime datetime not null default current_timestamp on update current_timestamp  comment '更新时间',
   primary key (ui_user_id),
   unique (ui_mobile) 
)engine=InnoDB default charset=utf8 comment='用户表';

create table it_house_info(
   hi_house_id bigint unsigned auto_increment comment '房屋id',
   hi_user_id  bigint unsigned not null comment '用户ID',
   hi_name varchar(64) not null comment '房屋名',
   hi_address varchar(256) not null comment '地址',
   hi_price int unsigned not null comment '价格',
   hi_ctime datetime not null default current_timestamp comment '创建时间',
   hi_utime datetime not null default current_timestamp on update current_timestamp  comment '更新时间',
   primary key (hi_house_id),
   constraint foreign key (hi_user_id) references it_user_info(ui_user_id)) engine=InnoDB default charset=utf8 comment='房屋信息表';

create table it_house_image(
   hi_image_id bigint unsigned auto_increment comment '房屋id',
   hi_house_id bigint unsigned  comment '房屋id',
   hi_url varchar(128) not null comment '图片url',
   hi_ctime datetime not null default current_timestamp comment '创建时间',
   hi_utime datetime not null default current_timestamp on update current_timestamp    comment '更新时间',
   primary key (hi_image_id),
   constraint foreign key (hi_image_id) references it_house_info(hi_house_id))
   engine=InnoDB default charset=utf8 comment='房屋图片';
###############################################################
insert into it_user_info(ui_name, ui_passwd,ui_age,
ui_mobile) values("a","a",20,"12345678900"),
("b","a",20,"12345678901"),("c","a",20,"12345678902"),
("d","a",21,"12345678903");
insert into it_house_info(hi_user_id, hi_name,hi_address,hi_price)
values(1,"a的房子","aaaaa",50000),
(1,"a的房子b","bbbbb",30000),(3,"c的房子","ccccc",10000),
(4,"d的房子","ddddd",50000);
insert into it_house_image(hi_house_id,hi_url)values(1,"/a/url");
insert into it_house_image(hi_house_id,hi_url)values(1,"/a/url"),(2,"/a/url"),(1,"/a/url");
select * from it_user_info;
select distinct ui_age from it_user_info;
select *  from it_user_info where ui_age in(20,23);
select *  from it_user_info where ui_age between 20 and 23;
select count(*) from it_user_info;
select count(*) counts from it_user_info;
select *  from it_user_info where ui_age between 20 and 23 order by ui_age desc;
select *  from it_user_info where ui_age between 20 and 23 order by ui_age desc limit 2;
select *  from it_user_info where ui_age between 20 and 23 order by ui_age desc limit 2,1;
select count(ui_age) from it_user_info group by ui_age;
select ui_age,count(ui_age) from it_user_info group by ui_age;
select max(ui_name),ui_age,count(ui_age) from it_user_info group by ui_age;
select ui_age,ui_name,count(ui_age) from it_user_info group by ui_age,ui_name;
alter table it_user_info add ui_area_id int unsigned not null comment '区域id';
alter table it_user_info drop ui_area_id;
select * from it_user_info where ui_user_id=1;
update it_user_info set ui_area_id=1 where ui_user_id=1;
update it_user_info set ui_area_id=1 where ui_user_id=2;
update it_user_info set ui_area_id=1 where ui_user_id=3;
update it_user_info set ui_area_id=2 where ui_user_id=4;
select * from it_user_info;
select ui_area_id, ui_age, count(*) from  it_user_info group by  ui_area_id,ui_age;
select * from it_user_info where ui_user_id=(
   select hi_user_id from it_house_info where hi_house_id=2
);
select * from it_user_info where ui_user_id in (
   select hi_user_id from it_house_info where hi_house_id in (2,3)
);
alter table it_user_info  drop ui_area_id;
it_user_info                it_house_info 
ui_user_id  ui_name         hi_user_id  hi_house_id 
1      a                       1         1 
2      b                       3         2
3      c                       4         3 

join = inner join 
from it_user_info inner join  it_house_info on 
ui_user_id=hi_user_id

user_id = 1,3 

from it_house_info left join  it_user_info on 
ui_user_id=hi_user_id

user_id = 1,3,4 

from it_house_info right join  it_user_info on 
ui_user_id=hi_user_id  

user_id = 1,2,3

from it_house_info  outer join  it_user_info on 
ui_user_id=hi_user_id  where

user_id = 1,2,3,4 

from it_house_info,it_user_info where  
ui_user_id=hi_user_id  和内连接一样

truncate table 保留表结构，删除所有数据
truncate table it_house_image;
delete from  it_house_image;
select *  from  it_house_image;

select *  from it_user_info inner join it_house_info on ui_user_id=hi_user_id 
left join it_house_image on it_house_info.hi_house_id=it_house_image.hi_house_id

select *  from it_user_info a inner join it_house_info b on a.ui_user_id=b.hi_user_id 
left join it_house_image c on b.hi_house_id=c.hi_house_id where a.ui_user_id=1;
4  注入攻击
get(sql,) 
name = a 
passwd = b

select count(*) from ih_user_info where ui_name='a' or 1=1 or ('1'='1' and ui_passwd='abc') or '1'='1'
name = a' or 1=1 or ('1'='1
passwd = abc') or '1'='1

sql = "select count(*) from ih_user_info where ui_name='%s' and ui_passwd='%s'" %(name,passwd)
