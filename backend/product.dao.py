from sql_connection import get_sql_connection

def get_all_products(connection):
    cursor = connection.cursor()
    query = ("select product.idProduct,Productname,Productunit,Productquantity from product inner join uom on product.uom_id=uom.Productid")
    cursor.execute(query)
    response = []
    for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append({
            'idProduct': product_id,
            'Productname': name,
            'Productunit': uom_id,
            'Productprice': price_per_unit,
        })
    return response

def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO product "
             "(Productname, Productunit, Productprice)"
             "VALUES (%s, %s, %s)")
    data = (product['Productname'], product['Productunit'], product['Productprice'])

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM product where idProduct=" + str(idProduct))
    cursor.execute(query)
    connection.commit()

    return cursor.lastrowid

if __name__ == '__main__':
    connection = get_sql_connection()
    # print(get_all_products(connection))
    print(insert_new_product(connection, {
        'Productname': 'potatoes',
        'Productunit': '1',
        'Productprice': 10
    }))
