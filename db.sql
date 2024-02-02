CREATE TABLE people (person_name text, age int, isadmin boolean);
\d people

INSERT INTO people (person_name, age, isadmin) VALUES ('Danny', '22', 'False');
INSERT INTO people (person_name, age, isadmin) VALUES ('Sammy', '42', 'False');
INSERT INTO people (person_name, age, isadmin) VALUES ('Ron', '19', 'True');
\d people
