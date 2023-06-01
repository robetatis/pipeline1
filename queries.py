query1 = """
CREATE DATABASE IF NOT EXISTS db;
DROP TABLE IF EXISTS db.tbl1;
CREATE TABLE IF NOT EXISTS db.tbl1(course_id STRING, course_name STRING, author_name STRING, no_reviews STRING);
INSERT INTO db.tbl1 VALUES (1, 'Java', 'FutureX', 45);
INSERT INTO db.tbl1 VALUES (2,'Java','FutureXSkill',56);
INSERT INTO db.tbl1 VALUES (3,'Big Data','Future',100);
INSERT INTO db.tbl1 VALUES (1,'Java','FutureX',45);
INSERT INTO db.tbl1 VALUES (4,'Linux','Future',100);
INSERT INTO db.tbl1 VALUES (5,'Microservices','Future',100);
INSERT INTO db.tbl1 VALUES (6,'CMS','',100);
INSERT INTO db.tbl1 VALUES (7,'Python','FutureX','');
INSERT INTO db.tbl1 VALUES (8,'CMS','Future',56);
INSERT INTO db.tbl1 VALUES (9,'Dot Net','FutureXSkill',34);
INSERT INTO db.tbl1 VALUES (10,'Ansible','FutureX',123);
INSERT INTO db.tbl1 VALUES (11,'Jenkins','Future',32);
INSERT INTO db.tbl1 VALUES (12,'Chef','FutureX',121);
INSERT INTO db.tbl1 VALUES (13,'Go Lang','',105);
ALTER TABLE db.tbl1 SET TBLPROPERTIES('serialization.null.format'='');
"""

query2 = """
CREATE TABLE IF NOT EXISTS db.tbl2 
(
    course_id STRING NOT NULL,
    course_name STRING NOT NULL,
    author_name STRING NOT NULL,
    no_reviews STRING NOT NULL
);
"""

query3 = """
INSERT INTO db.tbl1(course_id, course_name, author_name, course_section, creation_date) VALUES(%s, %s, %s, %s, %s)
"""

insert_tuple1 = (14, 'ML3', 'futureX', '{}', '2020-11-12')