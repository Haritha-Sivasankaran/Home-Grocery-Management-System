from datetime import datetime
from sql_connection import get_sql_connection

def insert_order(connection, order):
    cursor = connection.cursor()

    duedate_query = ("INSERT INTO duedate "
             "(idProduct, quantity, Duedatecol)"
             "VALUES (%s, %s, %s)")
    duedate_data = (duedate['idProduct'], dudate['quantity'], duedate['Duedatecol'])

    cursor.execute(duedate_query, duedate_data)
    dudate_id = cursor.lastrowid

    connection.commit()

    return order_id

    cursor.close()

def get_all_duedate(connection):
    cursor = connection.cursor()
    query = ("SELECT * FROM duedate")
    cursor.execute(query)
    response = []
    for (order_id, customer_name, total, dt) in cursor:
        response.append({
            'order_id': order_id,
            'customer_name': customer_name,
            'total': total,
            'datetime': dt,
        })

    cursor.close()

if __name__ == '__main__':
    connection = get_sql_connection()
    print(get_all_orders(connection))
