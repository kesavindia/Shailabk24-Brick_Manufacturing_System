'''
https://www.sqltutorial.org/sql-cheat-sheet/
C:\Program Files\PostgreSQL\16rc1
Data directory: C:\Program Files\PostgreSQL\16rc1\data
PEM  HTTd: C:\Program Files (x86)\edb\pem\httpd
port: 8080
Package: C:\Users\This PC
User: postgres
Pass: Madhu@Python
port: 5432

'''

'''
UI ---> Python  --> Database
        C S D

                    PostgreSQL
                    MySQL
                    Mongodb, Cassandra
                   (Oracle,SQL Server,Sqlite, MSSQL)
                   
1. Gmail signup   : CREATE 
2. Login to Home  : RETRIEVE
3. Update password: UPDATE
4. Delete account : DELETE  

Signup Page:    username,password,firstname,lastname,mobile....
--------------
UI                      Python 
json format  --->     To dictionary 

           
API Call **:
============
1. Request URL
2. Request Method
3. Payload


UI             Python               Database
-------------------------------------------------
FormData       Class (Fields)         Table(Column)
                 Object                 Record 


Employee             Employee
======================================
    eid              eid name   sal
    name             100 MadhuN 10000
    sal

madhu = Employee(100, 'MadhuN', 10000)
# INSERT INTO EMPLOYEE VALUES(...)
'''


'''
RDBMS vs Non RDBMS
SQL VS NOSQL :
------------------
SQL   : Mysql*, Postgresql*, Oracle, Sqlite, Sql server....
NOSQL : Mongodb*, Cassandra

Postgresql 
-------------
DB Installation,DeveloperTool(DBeaver)
Introduction:
 - What is Data
 - What is DBMS
 - DBMS vs RDBMS
 - DBMS vs Filesystem
 - DBMS Architecture 2 Tier
SQL:
 - Syntax
 - Data types
 - Operators
	SQL Arithmetic Operators
	SQL Comparison Operators
	SQL Logical Operators
Database:
 - CREATE, DROP, RENAME,SELECT
Table:
 - CREATE, DROP, RENAME, DELETE , TRUNCATE, COPY, TEMP, ALTER
 - Create Table Syntax 
 - Select records from table UNIQUE,DISTINCT,COUNT,TOP,FIRST,LAST,RANDOM, AS, IN, MULTIPLE, DATE, SUM, NULL
Clauses
 - WHERE AND OR WITH AS 
Order by 
 - ASC DESC RANDOM LIMIT
INSERT 
UPDATE
DELETE
 - Table, Row, all rows,duplicate rows,database, join,view
JOINS
 - INNER LEFT RIGHT FULL SELF CROSS
KEYS
 - PRIMARY FOREIGN COMPOSITE UNIQUE 
Sub Queries

Interview Questions:
--------------------
Sql Injection attacks
Sql vs Nosql
Indexing importance
SQL Performance optimization techniques
Joins 
Sub queries 
Integrity Constraints 
'''