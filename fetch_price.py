

def get_price_from_db(sku_id):
    conn = sqlite3.connect("sku_database.db")
    cursor = conn.cursor()
    
    query = "SELECT Price FROM SKUs WHERE SKU_ID = ?"
    cursor.execute(query, (sku_id,))
    result = cursor.fetchone()
    
    conn.close()
    
    if result:
        return result[0]  # Return the price
    return "SKU not found"