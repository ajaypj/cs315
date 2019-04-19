CREATE TABLE user (
  id INTEGER NOT NULL, 
  username VARCHAR(20) NOT NULL, 
  email VARCHAR(120) NOT NULL, 
  image_file VARCHAR(20) NOT NULL, 
  password VARCHAR(60) NOT NULL, 
  PRIMARY KEY (id), 
  UNIQUE (username), 
  UNIQUE (email)
);
CREATE TABLE post (
  id INTEGER NOT NULL, 
  title VARCHAR(100) NOT NULL, 
  date_posted DATETIME NOT NULL, 
  content TEXT NOT NULL, 
  user_id INTEGER NOT NULL, 
  PRIMARY KEY (id), 
  FOREIGN KEY(user_id) REFERENCES user (id)
);

CREATE TABLE patients
(
  patient_id INT NOT NULL,
  name VARCHAR(30) NOT NULL,
  sex INT NOT NULL,
  phone INT NOT NULL,
  dob DATE NOT NULL,
  PRIMARY KEY (patient_id)
);

CREATE TABLE visitor
(
  visitor_id INT NOT NULL,
  name VARCHAR(30) NOT NULL,
  phone INT NOT NULL,
  sex INT NOT NULL,
  age INT NOT NULL,
  PRIMARY KEY (visitor_id)
);

CREATE TABLE visiting
(
  time_in INT,
  time_out INT,
  patient_id INT NOT NULL,
  visitor_id INT NOT NULL,
  FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
  FOREIGN KEY (visitor_id) REFERENCES visitor(visitor_id)
);

CREATE TABLE login
(
  password VARCHAR(20) NOT NULL,
  username VARCHAR(10) NOT NULL,
  email VARCHAR(20) NOT NULL,
  PRIMARY KEY (username),
  UNIQUE (email)
);

CREATE TABLE students
(
  roll_no INT NOT NULL,
  name VARCHAR(30) NOT NULL,
  degree VARCHAR(10) NOT NULL,
  year INT NOT NULL,
  sex INT NOT NULL,
  phone INT NOT NULL,
  dob DATE NOT NULL,
  address VARCHAR(100),
  PRIMARY KEY (roll_no)
);

CREATE TABLE vendors
(
  vendor_id INT NOT NULL,
  name VARCHAR(30) NOT NULL,
  phone INT NOT NULL,
  PRIMARY KEY (vendor_id)
);

CREATE TABLE library
(
  book_id INT NOT NULL,
  book_name VARCHAR(30) NOT NULL,
  edition INT NOT NULL,
  quantity INT NOT NULL,
  PRIMARY KEY (book_id)
);

CREATE TABLE price_list
(
  price_list_id INT NOT NULL,
  category INT NOT NULL,
  price INT NOT NULL,
  desc VARCHAR(30),
  PRIMARY KEY (price_list_id)
);

CREATE TABLE transactions
(
  quantity INT NOT NULL,
  patient_id INT NOT NULL,
  price_list_id INT NOT NULL,
  FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
  FOREIGN KEY (price_list_id) REFERENCES price_list(price_list_id)
);

CREATE TABLE patient_fee
(
  patient_id INT NOT NULL,
  amt_paid INT NOT NULL,
  amt_due INT NOT NULL,
  PRIMARY KEY (patient_id),
  FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);

CREATE TABLE insurance
(
  insurance_id INT NOT NULL,
  name VARCHAR(20) NOT NULL,
  company_name VARCHAR(20) NOT NULL,
  amount INT NOT NULL,
  receiver_id INT NOT NULL,
  receiver_name VARCHAR(30) NOT NULL,
  PRIMARY KEY (insurance_id)
);

CREATE TABLE doctors
(
  doctor_id INT NOT NULL,
  name VARCHAR(30) NOT NULL,
  sex INT NOT NULL,
  phone INT NOT NULL,
  dob DATE NOT NULL,
  degree VARCHAR(20) NOT NULL,
  address VARCHAR(100) NOT NULL,
  dept_id INT NOT NULL,
  desg_id INT NOT NULL,
  PRIMARY KEY (doctor_id),
  FOREIGN KEY (dept_id) REFERENCES dept(dept_id),
  FOREIGN KEY (desg_id) REFERENCES desg(desg_id)
);

CREATE TABLE appointments
(
  doctor_id INT NOT NULL,
  patient_id INT NOT NULL,
  date DATE NOT NULL,
  time INT NOT NULL,
  description VARCHAR(100) NOT NULL,
  PRIMARY KEY (date, time, doctor_id, patient_id),
  FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id),
  FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);

CREATE TABLE employee
(
  emp_id INT NOT NULL,
  name VARCHAR(30) NOT NULL,
  sex INT NOT NULL,
  phone INT NOT NULL,
  dob DATE NOT NULL,
  address VARCHAR(100) NOT NULL,
  dept_id INT NOT NULL,
  desg_id INT NOT NULL,
  PRIMARY KEY (emp_id),
  FOREIGN KEY (dept_id) REFERENCES dept(dept_id),
  FOREIGN KEY (desg_id) REFERENCES desg(desg_id)
);

CREATE TABLE dept
(
  dept_id INT NOT NULL,
  name VARCHAR(30) NOT NULL,
  doctor_id INT,
  PRIMARY KEY (dept_id),
  FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
);

CREATE TABLE desg
(
  desg_id INT NOT NULL,
  name VARCHAR(20) NOT NULL,
  salary INT NOT NULL,
  dept_id INT NOT NULL,
  PRIMARY KEY (desg_id),
  FOREIGN KEY (dept_id) REFERENCES dept(dept_id)
);

CREATE TABLE inventory
(
  equip_id INT NOT NULL,
  dept_id INT NOT NULL,
  name VARCHAR(20) NOT NULL,
  quantity INT NOT NULL,
  PRIMARY KEY (equip_id, dept_id),
  FOREIGN KEY (dept_id) REFERENCES dept(dept_id)
);

CREATE TABLE lib_issued
(
  issue_date DATE NOT NULL,
  book_id INT NOT NULL,
  return_status INT NOT NULL,
  return_date DATE,
  doctor_id INT,
  roll_no INT,
  emp_id INT,
  PRIMARY KEY (issue_date, book_id),
  FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id),
  FOREIGN KEY (roll_no) REFERENCES students(roll_no),
  FOREIGN KEY (emp_id) REFERENCES employee(emp_id),
  FOREIGN KEY (book_id) REFERENCES library(book_id)
);

CREATE TABLE treatment
(
  patient_id INT NOT NULL,
  doctor_id INT NOT NULL,
  date DATE NOT NULL,
  time INT NOT NULL,
  desc VARCHAR(100),
  PRIMARY KEY (date, time, patient_id, doctor_id),
  FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
  FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
);

CREATE TABLE student_doc
(
  roll_no INT NOT NULL,
  doctor_id INT NOT NULL,
  term INT NOT NULL,
  field VARCHAR(20) NOT NULL,
  dept_id INT NOT NULL,
  PRIMARY KEY (roll_no, doctor_id),
  FOREIGN KEY (roll_no) REFERENCES students(roll_no),
  FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id),
  FOREIGN KEY (dept_id) REFERENCES dept(dept_id)
);

CREATE TABLE ambulances
(
  vehicle_no INT NOT NULL,
  emp_id INT NOT NULL,
  model_name VARCHAR(20) NOT NULL,
  type VARCHAR(20) NOT NULL,
  PRIMARY KEY (vehicle_no, emp_id),
  FOREIGN KEY (emp_id) REFERENCES employee(emp_id)
);
