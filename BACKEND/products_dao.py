from sql_connection import get_sql_connection
import mysql.connector

def get_all_products(connection):
    cursor = connection.cursor()

    query = (
        "SELECT products.product_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name "
        "FROM gs.products INNER JOIN gs.uom ON products.uom_id = uom.uom_id;"
    )

    cursor.execute(query)

    response = []

    for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append(
            {
                'product_id': product_id,
                'name': name,
                'uom_id': uom_id,
                'price_per_unit': price_per_unit,
                'uom_name': uom_name
            }
        )

    cursor.close()  # Close the cursor after use
    return response

def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO products "
             "(name, uom_id, price_per_unit) "
             "VALUES (%s, %s, %s)")
    data = (product['product_name'], product['uom_id'], product['price_per_unit'])
    cursor.execute(query, data)
    connection.commit()

    last_id = cursor.lastrowid  # Get the last inserted ID
    cursor.close()  # Close cursor after use
    return last_id

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = "DELETE FROM products WHERE product_id = %s"
    cursor.execute(query, (product_id,))  # Pass product_id as a tuple
    connection.commit()
    cursor.close()  # Close cursor after use

if __name__ == '__main__':
    connection = get_sql_connection()
  
    print(insert_new_product(connection, {
        'product_name': 'makhani',
        'uom_id': '2',
        'price_per_unit': '10'
    }))
    
    # Close the connection after all operations
    connection.close()




