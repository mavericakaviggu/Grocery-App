def get_uoms(connection):
    cursor = connection.cursor()
    query = "select * from grocery_store.unit_table"
    cursor.execute(query)

    response = []
    for unit, unitName in cursor:
        response.append({"unit": unit, "unitName": unitName})
    return response


if __name__ == "__main__":
    from sql_connection import get_sql_connection

    connection = get_sql_connection()
    # print(get_all_products(connection))
    print(get_uoms(connection))
