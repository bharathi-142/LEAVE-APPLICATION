CREATE DATABASE IF NOT EXISTS leave_db;

USE leave_db;

CREATE TABLE IF NOT EXISTS employee (
    emp_id VARCHAR(20) PRIMARY KEY,
    name VARCHAR(50),
    role VARCHAR(50)
);

INSERT INTO employee (emp_id, name, role) VALUES
('E001', 'Bharathi', 'Developer'),
('E002', 'Deepika', 'Designer'),
('E003', 'Logitha', 'Tester'),
('E004', 'Ravi', 'Manager'),
('E005', 'Priya', 'Designer'),
('E006', 'Anita', 'Tester'),
('E007', 'Karthik', 'Developer'),
('E008', 'Sangeetha', 'HR'),
('E009', 'Ajith', 'Support'),
('E010', 'Nisha', 'Designer');

CREATE TABLE IF NOT EXISTS leave_request (
    leave_id INT AUTO_INCREMENT PRIMARY KEY,
    emp_id VARCHAR(20),
    leave_type VARCHAR(20),
    from_date DATE,
    to_date DATE,
    reason TEXT,
    status VARCHAR(20) DEFAULT 'Pending',
    FOREIGN KEY (emp_id) REFERENCES employee(emp_id)
);

INSERT INTO leave_request (emp_id, leave_type, from_date, to_date, reason) VALUES
('E001', 'Casual', '2026-04-01', '2026-04-03', 'Personal work'),
('E003', 'Sick', '2026-04-05', '2026-04-06', 'Fever and rest'),
('E005', 'Casual', '2026-04-10', '2026-04-11', 'Family function');