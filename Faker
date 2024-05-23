import faker
import pyodbc
from faker import Faker

# Connection details
Driver = 'SQL Server'
server = 'DESKTOP-EQ55Q8H'
database = 'temp3'

# Connection string
connection = f"DRIVER={{{Driver}}};SERVER={server};DATABASE={database};Trusted_Connection=yes;"

try:
    # Establishing connection
    conn = pyodbc.connect(connection)
    cursor = conn.cursor()


    def insert_reg_user(name, email, password, phone_number):
        cursor.execute( "INSERT INTO registered_users(name, email, password,  phone_number) VALUES (  ?, ?, ?, ?)", (name, email, password,  phone_number))
        conn.commit()

    def insert_nonreg_user(cookie,name):
        cursor.execute("INSERT INTO non_registered_users(name,cookie) VALUES (?,?)", (name, cookie))
        conn.commit()

    def insert_prodcut_Category(name):
        cursor.execute(  "INSERT INTO product_categories(cateogory_name) VALUES (?)", (name))
        conn.commit()


    def insert_pre_booking(user_id, product_id,date):
        cursor.execute("exec prebookingpro  @user_id =?,  @product_id =?, @date=?",
                       ( user_id, product_id,date))
        conn.commit()

    def insert_retailers(retailer_name,phone ):
        cursor.execute(
            "INSERT INTO retailers ( retailer_name, phone) VALUES (?, ?)",
            ( retailer_name,phone))
        conn.commit()


    def insert_customer_support_ticket( user_id, issue,status):
        cursor.execute("INSERT INTO customer_support_tickets ( user_id, issue,status) VALUES (?, ?, ?)",
                       ( user_id, issue,status))
        conn.commit()


    def insert_reviews(user_id, product_id, rating, review_text):
        cursor.execute("exec insertreviews  @product_id =?,@user_id =?, @rating =?,@review=?", (user_id, product_id, rating, review_text))
        conn.commit()

    def insert_address(street_add,city,postalcode,country,userid):
        cursor.execute("insert into address values (?,?,?,?,?)",street_add,city,postalcode,country,userid)
        conn.commit()

    def insert_products(name,catid,description,image_url,price,rating):
        cursor.execute("insert into products values (?,?,?,?,?,?)",name,catid,description,image_url,price,rating)
        conn.commit()

    def insert_coupon (discount,start,end,limit):
        cursor.execute("insert into coupons values (?,?,?,?)",discount,start,end,limit)
        conn.commit()

    def insert_shipping_method(method ,fees):
        cursor.execute("insert into shipping values (?,?)",method ,fees)
        conn.commit()

    def insert_rb_fill_inv(p_id,r_id,quantity,discount,date):
     cursor.execute("exec add_retailerbill_fill_inventory @product_id =?, @retailer_id =?, @quantity =?, @discount= ?,@date=?",p_id,r_id,quantity,discount,date)
     conn.commit()

    insert_rb_fill_inv(1,1,20,20,'2024-5-24')
    fake = Faker()

    cursor.close()
    conn.close()

except pyodbc.Error as ex:
    sqlstate = ex.args[1]
    print(f"Error connecting to the database: {sqlstate}")
