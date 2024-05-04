from sql_connection import get_sql_connection

def get_all_products(connection):
    cursor = connection.cursor()
    query = ("select products.product_id, products.name, products.unit, products.price_unit, unit_table.unitName from products inner join unit_table on products.unit=unit_table.unitId")
    cursor.execute(query)
    response = []
    for (product_id, name, unit, price_unit, unitName) in cursor:
        response.append({
            'product_id': product_id,
            'name': name,
            'unit': unit,
            'price_unit': price_unit,
            'unitName': unitName
        })
    return response

def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO products "
             "(name, unit, price_unit)"
             "VALUES (%s, %s, %s)")
    data = (product['product_name'], product['unit'], product['price_unit'])

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products where product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()

    return cursor.lastrowid

if __name__ == '__main__':
    connection = get_sql_connection()
    # print(get_all_products(connection))
    print(insert_new_product(connection, {
        'product_name': 'potatoes',
        'unit': '1',
        'price_unit': 10
    }))