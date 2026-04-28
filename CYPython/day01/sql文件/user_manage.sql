SELECT * FROM `user` 
SELECT * FROM user_old 

CREATE table user_old(
 id int primary key auto_increment,
 account char(25) not null,
 password char(25) not null,
 nicname char(25) not null
)
insert into `user`(account,password,nicname) VALUES
("zdcc","123","xzdc"),
("qwe","123","qxzdc")


insert into user_old (account,password,nicname) select account,password,nicname from user where account ='zdc';
delete from user where account ='zdc';