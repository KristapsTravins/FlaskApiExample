# FlaskApiExample
1.Open connection.py change Connection  settings at line 2
conn = pymysql.connect(user='root', passwd='******', db='db')	
2.Install dependencies if not installed ... 
---pip install PyMySQL
---pip install Flask
---pip install -U flask-cors
3.. some api software required (Insomnia, Postman, etc.).... otherwise Only GET requests will work.
4. use chinook.db database
5. ...
6. ...To get API functions you need to Add stored procedures .. 2 options 
7. Option 1 .. you can import StoredProcedures.sql file to  your chinook.db database 
8. Option 2 .. write them  manualy ... 

1.use db;
DELIMITER //
CREATE PROCEDURE update_column(entry_id INT, what_to_change TEXT,change_to_what TEXT) 
BEGIN
IF what_to_change = "FirstName" THEN
UPDATE customers SET FirstName = change_to_what WHERE CustomerID = entry_id;
ELSEIF what_to_change = "LastName" THEN
UPDATE customers SET LastName = change_to_what WHERE CustomerID = entry_id;
ELSEIF what_to_change = "Company" THEN
UPDATE customers SET Company = change_to_what WHERE CustomerID = entry_id;
ELSEIF what_to_change = "Address" THEN
UPDATE customers SET Address = change_to_what WHERE CustomerID = entry_id;
ELSEIF what_to_change = "City" THEN
UPDATE customers SET City = change_to_what WHERE CustomerID = entry_id;
ELSEIF what_to_change = "State" THEN
UPDATE customers SET State = change_to_what WHERE CustomerID = entry_id;
ELSEIF what_to_change = "Country" THEN
UPDATE customers SET Country = change_to_what WHERE CustomerID = entry_id;
ELSEIF what_to_change = "PostalCode" THEN
UPDATE customers SET PostalCode = change_to_what WHERE CustomerID = entry_id;
ELSEIF what_to_change = "Phone" THEN
UPDATE customers SET PostalCode = change_to_what WHERE CustomerID = entry_id;
ELSEIF what_to_change = "Fax" THEN
UPDATE customers SET Fax = change_to_what WHERE CustomerID = entry_id;
ELSEIF what_to_change = "Email" THEN
UPDATE customers SET Email = change_to_what WHERE CustomerID = entry_id;
END IF;
END 
... to update customer collumns 

2.
use db;
DELIMITER //
CREATE PROCEDURE add_customer (cust_name TEXT,cust_lname TEXT, cust_company TEXT, cust_adress TEXT, cust_city TEXT, cust_Country TEXT, cust_postal TEXT,cust_phone TEXT,cust_email TEXT,cust_rank INT)
BEGIN
INSERT INTO customers(FirstName,LastName,Company,Address,City,Country,PostalCode,Phone,Email,SupportRepId)
VALUES(cust_name, cust_lname, cust_company, cust_adress, cust_city, cust_Country, cust_postal, cust_phone, cust_email, cust_rank);
END
.. to add customer collumn

3.

use db;
DELIMITER //
CREATE PROCEDURE delete_custromers (cust_name TEXT, cust_lname TEXT)
BEGIN
DELETE FROM customers WHERE cust_name = FirstName AND cust_lname = LastName;
END
.. to Delete customer collumn

4.

use db;
DELIMITER //
CREATE PROCEDURE get_all_customers()
BEGIN
SELECT * FROM customers;
END
.. to Get all customers


5.

use db;
DELIMITER //
CREATE PROCEDURE get_customer_info(cust_name TEXT, cust_lname TEXT)
BEGIN
SELECT * FROM customers WHERE FirstName = cust_name AND LastName = cust_lname ; 
END
.. to Get customer by Name Last name



.. usage .. 

http://localhost:5000/--- gives all customers 
http://localhost:5000/<name>/<surname>--- gives specific customer 
http://localhost:5000/<name>/<surname>--- (Insomnia) -- POST method --> add querry values example :( company:grindex ) --- has to be  all collumns... 
http://localhost:5000/<name>/<surname> --- (Insomnia) -- Delete  method --> Deletes customer by name and lastname .
http://localhost:5000/<name>/<surname> --- (Insomnia) -- PATCH  method --> Patches collumn value --> add querry ---> example( id:<customerid> , collumn:<collumn>, value:<value >)
