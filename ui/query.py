import mysql.connector
import pandas as pd
import bcrypt

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            port="3306",
            user="root",
            password="",
            db="cbc"
        )
        return connection
    except mysql.connector.Error as e:
        print(f"Error connecting to the database: {e}")
        return None
def verify_credentials(email, password):
    connection = get_db_connection()
    if connection:
        with connection.cursor(dictionary=True) as cursor:
            query = "SELECT * FROM user WHERE email = %s"
            cursor.execute(query, (email,))
            user = cursor.fetchone()
            connection.close()
            if user and bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
                return user
            else:
                return None
    else:
        return None

def signup(name,email,phone,password):
    connection = get_db_connection()
    if connection:
        with connection.cursor(dictionary=True) as cursor:
            query = "INSERT INTO user (name, email, phone, password) VALUES (%s, %s, %s, %s)"
            record = (name, email, phone, password)
            cursor.execute(query, record)
            new_user_id = cursor.lastrowid
            connection.commit()

            user = get_user_by_id(new_user_id)
            return user
    else:
        return False
def get_news():
    connection = get_db_connection()
    if connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute('SELECT title, content, image_url,link FROM news')
            news_data = cursor.fetchall()
            return news_data
    else:
        return None
    
def insert_feedback(user_id,selected_progress, feedback, satisfaction_level):
    connection = get_db_connection()
    if connection:
        with connection.cursor(dictionary=True) as cursor:
            sql_query = """INSERT INTO feedback (user_id,selected_progress, feedback, satisfaction_level)
                                            VALUES (%s,%s, %s, %s)"""
            record = (user_id,selected_progress, feedback, satisfaction_level)
            cursor.execute(sql_query, record)
            connection.commit()
            # progress = ["Covid19", "Thiếu máu"]
            # if satisfaction_level == 1:
            #     if selected_progress == "Covid19":
            #         #cập
            #     elif selected_progress == "Thiếu máu":
            print("Feedback inserted successfully")
def insert_covid19(user_id,LYM, NEUT, MONO, EOS, BASO,HGB,HCT,MCV,MCH,MCHC,RDW,PLT,MPV,diseased):
    connection = get_db_connection()
    if connection:
        with connection.cursor(dictionary=True) as cursor:
            sql_query = """INSERT INTO covid_test_results (user_id,LYM, NEUT, MONO, EOS, BASO,HGB,HCT,MCV,MCH,MCHC,RDW,PLT,MPV,diseased)
                                         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            record = (user_id,LYM, NEUT, MONO, EOS, BASO, HGB, HCT, MCV, MCH, MCHC, RDW, PLT, MPV, diseased)
            cursor.execute(sql_query, record)
            connection.commit()
            print("covid19 inserted successfully")
def insert_anemia(user_id,LYM, NEUT, MONO, EOS, BASO,HGB,HCT,MCV,MCH,MCHC,RDW,PLT,MPV,RBC,WBC,diseased):
    connection = get_db_connection()
    if connection:
        with connection.cursor(dictionary=True) as cursor:
            sql_query = """INSERT INTO anemia_test_results (user_id,LYM, NEUT, MONO, EOS, BASO,HGB,HCT,MCV,MCH,MCHC,RDW,PLT,MPV,RBC,WBC,diseased)
                                         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            record = (user_id, LYM, NEUT, MONO, EOS, BASO, HGB, HCT, MCV, MCH, MCHC, RDW, PLT, MPV, RBC, WBC, diseased)
            cursor.execute(sql_query, record)
            connection.commit()
            print("Anemia inserted successfully")

def get_user_by_id(id):
    connection = get_db_connection()
    if connection:
        with connection.cursor(dictionary=True) as cursor:
            select_query = "SELECT * FROM user WHERE id = %s"
            cursor.execute(select_query, (id,))
            new_user = cursor.fetchone()
            return new_user
    else:
        return None

def count_tests_by_user(user_id, table_names):
    connection = get_db_connection()
    if connection:
        total_count = 0  # Biến tổng số lần test
        with connection.cursor() as cursor:
            for table_name in table_names:
                query = f"SELECT COUNT(*) FROM `{table_name}` WHERE user_id = %s"
                cursor.execute(query, (user_id,))
                count = cursor.fetchone()[0]
                total_count += count  # Cộng vào tổng số lần test
            connection.close()
        return total_count
    else:
        return 0
def total_test_count(user_id):
    table_names = ["anemia_test_results","covid_test_results","diabetes_test_results"]
    return count_tests_by_user(user_id,table_names)

def get_data_by_user_id(user_id,table_name):
    connection = get_db_connection()
    if connection:
        with connection.cursor(dictionary=True) as cursor:
            query = f"SELECT * FROM `{table_name}` WHERE user_id = %s"
            cursor.execute(query, (user_id,))
            data = cursor.fetchone()
            connection.close()
            return data
    else:
        return None

def count_diseased_covid():
    connection = get_db_connection()
    if connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute('SELECT SUM(IF(diseased = 1, 1, 0)) AS count_1, SUM(IF(diseased = 0, 1, 0)) AS count_0 FROM covid_test_results;')
            result = cursor.fetchone()
            count_1 = result['count_1']
            count_0 = result['count_0']

        return count_1, count_0
    else:
        return None

def count_diseased_anemia():
    connection = get_db_connection()
    if connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute('SELECT SUM(IF(diseased = 1, 1, 0)) AS count_1, SUM(IF(diseased = 0, 1, 0)) AS count_0 FROM anemia_test_results;')
            result = cursor.fetchone()
            count_1 = result['count_1']
            count_0 = result['count_0']

        return count_1, count_0
    else:
        return None
    
def insert_diabetes(user_id,HGB,MCHC,MCH,MCV,MPV,RBC,PLT,RDW,WBC,diseased):
    connection = get_db_connection()
    if connection:
        with connection.cursor(dictionary=True) as cursor:
            sql_query = """INSERT INTO diabetes_test_results(user_id,HGB,MCHC,MCH,MCV,MPV,RBC,PLT,RDW,WBC,diseased)
                                         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            record = (user_id,HGB,MCHC,MCH,MCV,MPV,RBC,PLT,RDW,WBC,diseased)
            cursor.execute(sql_query, record)
            connection.commit()
            print("Diabetes inserted successfully")

def update_data_predict(user_id, diseased, table_name):
    connection = get_db_connection()
    if connection:
        with connection.cursor(dictionary=True) as cursor:
            sql_query = f"UPDATE `{table_name}` SET diseased = %s WHERE user_id = %s"
            record = (diseased, user_id)
            cursor.execute(sql_query, record)
            connection.commit()
            print("Diabetes updated successfully")