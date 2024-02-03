CREATE DATABASE payroll_service;
SELECT datname FROM pg_database;
-- Use the 'payroll_service' database
-- \c payroll_service

-- Create the 'employee_payroll' table
CREATE TABLE employee_payroll (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    salary DECIMAL(10, 2),
    start_date DATE
);

INSERT INTO employee_payroll (name, salary, start_date)
VALUES
    ('Joshi Karan', 1000300.00, '2022-01-01'),
    ('Felix Smith', 1000060.00, '2022-02-15'),
    ('Deepak chandhu', 1000030.00, '2022-03-20'),
    ('yashwant', 1000300.00, '2022-01-01'),
    ('Arthur Morgon' , 1003020.00 ,'2022-01-01'),
    ('Carl Johnson' , 12003020.00 ,'1990-01-01'),
    ('Tommy Vercetti', 10004030.00 , '1982-01-02'),
    ('Bill Aron' , 145000.00 , '1999-01-02');


-- Insert additional employees into the employee_payroll table
INSERT INTO employee_payroll (name, salary, start_date, gender)
VALUES
    ('Alice ', 60000.00, '2023-01-10', 'F'),
    ('Zoe', 70000.00, '2023-02-15', 'F'),
    ('Eva', 55000.00, '2023-03-20', 'F'),
    ('Jenny', 60000.00, '2023-01-10', 'F'),
    ('Lisa', 70000.00, '2023-02-15', 'F'),
    ('Jesse', 55000.00, '2023-03-20', 'F'),
    ('Anna ', 60000.00, '2023-01-10', 'F');
   




WITH CTE AS (
    SELECT
        id,
        name,
        salary,
        start_date,
        gender,
        ROW_NUMBER() OVER (PARTITION BY name ORDER BY id) AS rn
    FROM
        employee_payroll
)
DELETE FROM employee_payroll
WHERE id IN (SELECT id FROM CTE WHERE rn > 1);





SELECT * FROM employee_payroll


SELECT salary FROM employee_payroll
WHERE name = 'Bill'

SELECT * FROM employee_payroll WHERE start_date BETWEEN CAST('2018-01-01' AS DATE) AND CURRENT_DATE;

-- Add 'gender' field after 'name' field
ALTER TABLE employee_payroll ADD COLUMN gender CHAR(1);

-- Update gender for specific employees
UPDATE employee_payroll SET gender = 'M' WHERE name = 'Bill' OR name = 'Charlie';

-- Update all employees to have 'M' as the gender
UPDATE employee_payroll SET gender = 'M';






-- Sum of salary for Male and Female employees
SELECT gender, SUM(salary) AS total_salary
FROM employee_payroll
GROUP BY gender;

-- Average salary for Male and Female employees
SELECT gender, AVG(salary) AS average_salary
FROM employee_payroll
GROUP BY gender;

-- Minimum salary for Male and Female employees
SELECT gender, MIN(salary) AS min_salary
FROM employee_payroll
GROUP BY gender;

-- Maximum salary for Male and Female employees
SELECT gender, MAX(salary) AS max_salary
FROM employee_payroll
GROUP BY gender;

-- Number of Male and Female employees
SELECT gender, COUNT(*) AS employee_count
FROM employee_payroll
GROUP BY gender;





-- Add new columns to the employee_payroll table
ALTER TABLE employee_payroll
ADD COLUMN phone VARCHAR(20);

ALTER TABLE employee_payroll
ADD COLUMN address VARCHAR(255) DEFAULT 'Not Specified' NOT NULL;

ALTER TABLE employee_payroll
ADD COLUMN department VARCHAR(50) NOT NULL;


-- Add the department column without NOT NULL constraint
ALTER TABLE employee_payroll
ADD COLUMN department VARCHAR(50);

-- Update existing records with department information
UPDATE employee_payroll
SET department = 'DefaultDepartment'
WHERE department IS NULL;

-- Add a default value to the department column
ALTER TABLE employee_payroll
ALTER COLUMN department SET DEFAULT 'DefaultDepartment';

-- Alter the department column to NOT NULL
ALTER TABLE employee_payroll
ALTER COLUMN department SET NOT NULL;







-- Add new columns to the employee_payroll table
ALTER TABLE employee_payroll
ADD COLUMN basic_pay DECIMAL(10, 2),
ADD COLUMN deductions DECIMAL(10, 2),
ADD COLUMN taxable_pay DECIMAL(10, 2),
ADD COLUMN income_tax DECIMAL(10, 2),
ADD COLUMN net_pay DECIMAL(10, 2);

-- Update existing records with basic pay, deductions, taxable pay, income tax, and net pay information
UPDATE employee_payroll
SET
    basic_pay = 50000.00,
    deductions = 2000.00,
    taxable_pay = 48000.00,
    income_tax = 1000.00,
    net_pay = 47000.00
WHERE
    basic_pay IS NULL AND
    deductions IS NULL AND
    taxable_pay IS NULL AND
    income_tax IS NULL AND
    net_pay IS NULL;






-- Identify the relevant Employee ID(s) for Terissa
-- Assuming Employee IDs are 1001 and 1002
-- Identify the relevant Employee ID(s) for Terissa
-- Assuming Employee IDs are 1001 and 1002
-- Identify the relevant Employee ID(s) for Terissa
-- Assuming Employee IDs are 1001 and 1002
DO $$ 
DECLARE 
    terissaEmployeeID1 INT;
    terissaEmployeeID2 INT;
BEGIN
    SELECT MAX(id) + 1 INTO terissaEmployeeID1 FROM employee_payroll;
    terissaEmployeeID2 := terissaEmployeeID1 + 1;

    -- Insert the complete employee payroll record for Terissa with Sales and Marketing Department
    INSERT INTO employee_payroll (id, name, salary, start_date, gender, phone, address, department, basic_pay, deductions, taxable_pay, income_tax, net_pay)
    VALUES
        (terissaEmployeeID1, 'Terissa', 60000.00, '2024-01-15', 'F', '123-456-7890', '123 Main St', 'Sales and Marketing', 50000.00, 2000.00, 48000.00, 1000.00, 47000.00);

    INSERT INTO employee_payroll (id, name, salary, start_date, gender, phone, address, department, basic_pay, deductions, taxable_pay, income_tax, net_pay)
    VALUES
        (terissaEmployeeID2, 'Terissa', 60000.00, '2024-01-15', 'F', '123-456-7890', '123 Main St', 'Sales and Marketing', 50000.00, 2000.00, 48000.00, 1000.00, 47000.00);
END $$;

