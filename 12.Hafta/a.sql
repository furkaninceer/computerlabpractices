CREATE TABLE parts(
    part_id INT
    part_name VARCHAR(100)
    suppliers_id INT
    customers_id INT
    Foreign KEY (customers_id) REFERENCES suppliers(suppliers_id)
    Foreign KEY (suppliers_id) REFERENCES customers(customers_id)
)

CREATE TABLE suppliers(
    suppliers_id INT
    suppliers_name VARCHAR(100)
    part_id INT
    customers_id INT
    Foreign KEY (part_id) REFERENCES parts(part_id)
    Foreign KEY (customers_id) REFERENCES customers(customers_id)
)

CREATE TABLE customers(
    customers_id INT
    customers_name VARCHAR(100)
    suppliers_id INT
    part_id INT
    Foreign KEY (part_id) REFERENCES parts(part_id)
    Foreign KEY (suppliers_id) REFERENCES suppliers(suppliers_id)
)


