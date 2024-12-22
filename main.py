from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_price_from_db(sku_id):
    conn = sqlite3.connect('fk_fenner_mrp_may_01_2024.db')
    cursor = conn.cursor()

    query = "SELECT price from Fenner WHERE size = ?"
    cursor.execute(query, (sku_id,))
    result = cursor.fetchone()

    conn.close()

    if result:
        return result[0]
    return "SKU_NOT_FOUND"

@app.route('/get_price', methods=['GET'])
def get_price():
    sku_id = request.args.get('sku_id')
    price = get_price_from_db(sku_id)
    return jsonify({'price': price})

if __name__ == '__main__':
    app.run(debug=True)