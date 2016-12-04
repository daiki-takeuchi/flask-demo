create database if not exists sample_db character set utf8;
create user 'test_user' identified by 'test_user';
grant all on sample_db.* to 'test_user';