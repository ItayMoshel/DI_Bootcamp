SELECT * FROM students;

SELECT first_name, last_name FROM students;

SELECT first_name, last_name FROM students WHERE student_id = 2;

SELECT first_name, last_name FROM students WHERE last_name = 'Benichou' AND first_name = 'Marc';

SELECT first_name, last_name FROM students WHERE last_name = 'Benichou' OR first_name = 'Marc';

SELECT first_name, last_name FROM students WHERE first_name ILIKE '%a%';

SELECT first_name, last_name FROM students WHERE first_name ILIKE 'a%';

SELECT first_name, last_name FROM students WHERE first_name ILIKE '%a';

SELECT first_name, last_name FROM students WHERE student_id = 1 OR student_id = 3;

SELECT * FROM students WHERE birth_date >= '1/01/2000';

SELECT first_name, last_name, birth_date FROM students ORDER BY last_name ASC LIMIT 4 OFFSET 0;
