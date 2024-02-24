SELECT a,b 
FROM jenk
WHERE a.c=3;

SELECT A,b
FROM jenk
ORDER BY ADRESS ASC;

SELECT A,b
FROM jenk
ORDER BY ADRESS DESC;

INSERT INTO tablo(column1)
VALUES (23);

UPDATE tablo
SET column1=value1,column2=value2;

DELETE FROM tablo 
where condition;

CREATE tablo (
    ID INT PRIMARY KEY
    NAME1 VARCHAR(50) NOT NULL
    NAME2 VARCHAR(50) NOT NULL
    NAME3 VARCHAR(50) NOT NULL
    part_id INT
    part_name INT
    Foreign KEY (part_id) REFERENCES parts(part_id)
    Foreign KEY (part_name) REFERENCES parts(part_name)

)