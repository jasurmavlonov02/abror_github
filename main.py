
import psycopg2

db_info = {
    "database":"blog",
    "user":"postgres",
    "password":"admin123",
    "host":"localhost",
    "port":"5432"
    
}
# conn = None

with psycopg2.connect(**db_info) as conn:
    with conn.cursor() as cur:
        select_category_list_query = """select * from category;"""
        cur.execute(select_category_list_query)
        print(cur.fetchall())
         
        

# try:
#     conn = psycopg2.connect(**db_info)    
#     cur = conn.cursor()
# except psycopg2.OperationalError as e:
#     print(e)
    
# else:
#     select_category_list_query = """select * from category;"""
#     cur.execute(select_category_list_query)
#     print(cur.fetchall())
    
# finally:
#     if conn is not None:
#         if cur:
#             cur.close()
#             conn.close()
            
            
        

    
    





# conn = psycopg2.connect(**db_info)
# cur = conn.cursor()

# create_table_blog_query = """ CREATE TABLE IF NOT EXISTS category(
#         id SERIAL PRIMARY KEY,
#         title varchar(255) not null unique,
#         created_at timestamptz default current_timestamp
    
#     );
# """


# # cur.execute(create_table_blog_query)
# # conn.commit()

# insert_category_query = """
# insert into category(title)
# values ('Smartfonlar'),
#        ('Muzlatgichlar');
# """

# # cur.execute(insert_category_query)

# # conn.commit()

# select_category_list_query = """select * from category;"""

# cur.execute(select_category_list_query)

# # fetchall ,

# # categories = cur.fetchall()
# # print(categories)

# # category = """select * from category where id = 1;""" # smartfon
# # cur.execute(category)

# # category = cur.fetchone()
# # print(category)

# # delete_category_query = """DELETE FROM category where id = 2;"""
# # cur.execute(delete_category_query)
# # conn.commit()





# # for category in categories:
# #     print(category) 
# cur.close()
# conn.close()


