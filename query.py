from db import get_connection
import datetime

def insert_query(mail_id, mobile_number, query_heading, query_description):
    conn = get_connection()
    cursor = conn.cursor()
    query_created_time = datetime.datetime.now()
    sql = '''
    INSERT INTO queries 
    (mail_id, mobile_number, query_heading, query_description, status, query_created_time, query_closed_time)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    '''
    cursor.execute(sql, (
        mail_id,
        mobile_number,
        query_heading,
        query_description,
        "Open",
        query_created_time,
        None
    ))
    conn.commit()
    cursor.close()
    conn.close()

def fetch_queries(status=None):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    if status:
        cursor.execute("SELECT * FROM queries WHERE status=%s", (status,))
    else:
        cursor.execute("SELECT * FROM queries")
    queries = cursor.fetchall()
    cursor.close()
    conn.close()
    return queries

def close_query(query_id):
    conn = get_connection()
    cursor = conn.cursor()
    closed_time = datetime.datetime.now()
    cursor.execute(
        "UPDATE queries SET status=%s, query_closed_time=%s WHERE query_id=%s",
        ("Closed", closed_time, query_id)
    )
    conn.commit()
    cursor.close()
    conn.close()
def delete_query(query_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM queries WHERE query_id=%s", (query_id,))
    conn.commit()

    cursor.close()
    conn.close()
