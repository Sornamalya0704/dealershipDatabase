import psycopg2

conn=psycopg2.connect(host="localhost",database="CDS",user="postgres",port="5432",password="07@April@2005")
cur=conn.cursor()

showroom='''CREATE TABLE IF NOT EXISTS SHOWROOM(SHOWROOM_ID VARCHAR PRIMARY KEY NOT NULL,
                                SHOWROOM_NAME VARCHAR,
                                PINCODE VARCHAR,
                                STATE VARCHAR,
                                CITY VARCHAR)'''
showroom_phone='''CREATE TABLE IF NOT EXISTS SHOWROOM_PHONE(SHOWROOM_ID VARCHAR NOT NULL,
                                PHONE_NUMBER VARCHAR,
                                FOREIGN KEY (SHOWROOM_ID) REFERENCES SHOWROOM(SHOWROOM_ID))'''
showroom_email='''CREATE TABLE IF NOT EXISTS SHOWROOM_EMAIL(SHOWROOM_ID VARCHAR NOT NULL,
                                EMAIL_ID VARCHAR,
                                FOREIGN KEY(SHOWROOM_ID) REFERENCES SHOWROOM(SHOWROOM_ID))'''

admin='''CREATE TABLE IF NOT EXISTS ADMIN(ADMIN_ID VARCHAR PRIMARY KEY NOT NULL, 
                               ADMIN_NAME VARCHAR NOT NULL, USERNAME VARCHAR NOT NULL,
                               PASSWORD VARCHAR NOT NULL,
                               CITY VARCHAR ,
                               STATUS VARCHAR)'''
admin_phone='''CREATE TABLE IF NOT EXISTS ADMIN_PHONE(ADMIN_ID VARCHAR NOT NULL,
                                PHONE_NUMBER VARCHAR,
                                FOREIGN KEY (ADMIN_ID) REFERENCES ADMIN(ADMIN_ID))'''
admin_email='''CREATE TABLE IF NOT EXISTS ADMIN_EMAIL(ADMIN_ID VARCHAR NOT NULL,
                                EMAIL_ID VARCHAR,
                                FOREIGN KEY(ADMIN_ID) REFERENCES ADMIN(ADMIN_ID))'''

dealer='''CREATE TABLE IF NOT EXISTS DEALER(DEALER_ID VARCHAR PRIMARY KEY NOT NULL,
                                DEALER_NAME VARCHAR NOT NULL,
                                USERNAME VARCHAR NOT NULL,
                                PASSWORD VARCHAR NOT NULL,
                                CITY VARCHAR,
                                STATUS VARCHAR,
                                COMPANY_NAME VARCHAR,
                                ADMIN_ID VARCHAR NOT NULL,
                                SHOWROOM_ID VARCHAR NOT NULL,
                                FOREIGN KEY(SHOWROOM_ID) REFERENCES SHOWROOM(SHOWROOM_ID),
                                FOREIGN KEY(ADMIN_ID) REFERENCES ADMIN(ADMIN_ID))'''
dealer_phone='''CREATE TABLE IF NOT EXISTS DEALER_PHONE(DEALER_ID VARCHAR NOT NULL,
                                PHONE_NUMBER VARCHAR,
                                FOREIGN KEY(DEALER_ID) REFERENCES DEALER(DEALER_ID))'''
dealer_email='''CREATE TABLE IF NOT EXISTS DEALER_EMAIL(DEALER_ID VARCHAR NOT NULL,
                                EMAIL_ID VARCHAR,
                                FOREIGN KEY(DEALER_ID) REFERENCES DEALER(DEALER_ID))'''




car='''CREATE TABLE IF NOT EXISTS CAR(CAR_ID VARCHAR PRIMARY KEY NOT NULL,
                                SERIAL_NUM VARCHAR UNIQUE NOT NULL,
                                BRAND VARCHAR,
                                MODEL VARCHAR,
                                FOR_SALE VARCHAR,
                                COLOUR VARCHAR,
                                COST VARCHAR,
                                YEAR VARCHAR,
                                CONSTRAINT CHK_FOR_SALE CHECK(FOR_SALE IN('Y','N')))'''
features='''CREATE TABLE IF NOT EXISTS FEATURES(CAR_ID VARCHAR PRIMARY KEY NOT NULL,
                                COMFORTNESS VARCHAR,
                                RELIABILITY VARCHAR,
                                CONDITION VARCHAR,
                                FUEL_TYPE VARCHAR,
                                MILEAGE VARCHAR,
                                ENGINE_CAPACITY VARCHAR,
                                PERFORMANCE VARCHAR,
                                ENTERTAINMENT VARCHAR,
                                NAVIGATION VARCHAR,
                                SAFETY VARCHAR,
                                FOREIGN KEY(CAR_ID) REFERENCES CAR(CAR_ID))'''
tax='''CREATE TABLE IF NOT EXISTS TAX(TAX_ID VARCHAR PRIMARY KEY NOT NULL,
                                CAR_ID VARCHAR UNIQUE NOT NULL,
                                ROAD_TAX DECIMAL,
                                CAR_TAX DECIMAL,
                                FOREIGN KEY(CAR_ID) REFERENCES CAR(CAR_ID))'''

customer='''CREATE TABLE IF NOT EXISTS CUSTOMER(CUSTOMER_ID VARCHAR PRIMARY KEY NOT NULL,
                                CUSTOMER_NAME VARCHAR,
                                AADHAR_NUMBER VARCHAR,
                                USERNAME VARCHAR,
                                PASSWORD VARCHAR,
                                CITY VARCHAR,
                                STATE VARCHAR,
                                COUNTRY VARCHAR,
                                PINCODE VARCHAR)'''
customer_phone='''CREATE TABLE IF NOT EXISTS CUSTOMER_PHONE(CUSTOMER_ID VARCHAR NOT NULL,
                                PHONE_NUMBER VARCHAR,
                                FOREIGN KEY (CUSTOMER_ID) REFERENCES CUSTOMER(CUSTOMER_ID))'''
customer_email='''CREATE TABLE IF NOT EXISTS CUSTOMER_EMAIL(CUSTOMER_ID VARCHAR NOT NULL,
                                EMAIL_ID VARCHAR,
                                FOREIGN KEY(CUSTOMER_ID) REFERENCES CUSTOMER(CUSTOMER_ID))'''
insurance='''CREATE TABLE IF NOT EXISTS INSURANCE(INSURANCE_ID VARCHAR PRIMARY KEY NOT NULL,
                                INSURANCE_TYPE VARCHAR,
                                INSURANCE_AMOUNT VARCHAR,
                                INSURANCE_DATE VARCHAR,
                                STATUS VARCHAR,
                                BANK_NAME VARCHAR,
                                CUSTOMER_ID VARCHAR,
                                FOREIGN KEY (CUSTOMER_ID) REFERENCES CUSTOMER(CUSTOMER_ID))'''
sales_invoice='''CREATE TABLE IF NOT EXISTS SALES_INVOICE(INVOICE_ID VARCHAR PRIMARY KEY NOT NULL,
                                CUSTOMER_ID VARCHAR,
                                CAR_ID VARCHAR UNIQUE,
                                DEALER_ID VARCHAR,
                                INVOICE_NUMBER VARCHAR,
                                FOREIGN KEY(CUSTOMER_ID) REFERENCES CUSTOMER(CUSTOMER_ID),
                                FOREIGN KEY(CAR_ID) REFERENCES CAR(CAR_ID),
                                FOREIGN KEY(DEALER_ID) REFERENCES DEALER(DEALER_ID))'''
payment='''CREATE TABLE IF NOT EXISTS PAYMENT(PAYMENT_ID VARCHAR PRIMARY KEY NOT NULL,
                                INVOICE_ID VARCHAR,
                                AMOUNT_PAID DECIMAL,
                                DATE_PAID DECIMAL,
                                INSURANCE_ID VARCHAR,
                                FOREIGN KEY(INSURANCE_ID) REFERENCES INSURANCE(INSURANCE_ID),
                                FOREIGN KEY(INVOICE_ID) REFERENCES SALES_INVOICE(INVOICE_ID))'''

cur.execute(showroom)
cur.execute(showroom_email)
cur.execute(showroom_phone)
cur.execute(admin)
cur.execute(admin_phone)
cur.execute(admin_email)
cur.execute(dealer)
cur.execute(dealer_email)
cur.execute(dealer_phone)
cur.execute(car)
cur.execute(features)
cur.execute(tax)
cur.execute(customer)
cur.execute(customer_email)
cur.execute(customer_phone)
cur.execute(insurance)
cur.execute(sales_invoice)
cur.execute(payment)
conn.commit()
conn.close() 