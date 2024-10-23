import sqlite3
import random

# SQLite를 활용한 전자제품 데이터 관리 클래스
class ElectronicsDatabase:
    def __init__(self, db_name='electronics.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        # 제품 테이블 생성
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_name TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        self.connection.commit()

    def insert_product(self, product_name, price):
        # 제품 삽입
        self.cursor.execute('''
            INSERT INTO products (product_name, price)
            VALUES (?, ?)
        ''', (product_name, price))
        self.connection.commit()

    def update_product(self, product_id, product_name=None, price=None):
        # 제품 업데이트
        query = "UPDATE products SET "
        params = []
        if product_name is not None:
            query += "product_name = ?, "
            params.append(product_name)
        if price is not None:
            query += "price = ?, "
            params.append(price)
        
        query = query.rstrip(', ')  # 마지막 쉼표 제거
        query += " WHERE product_id = ?"
        params.append(product_id)

        self.cursor.execute(query, tuple(params))
        self.connection.commit()

    def delete_product(self, product_id):
        # 제품 삭제
        self.cursor.execute('''
            DELETE FROM products WHERE product_id = ?
        ''', (product_id,))
        self.connection.commit()

    def select_product(self, product_id):
        # 제품 선택
        self.cursor.execute('''
            SELECT * FROM products WHERE product_id = ?
        ''', (product_id,))
        return self.cursor.fetchone()

    def select_all_products(self):
        # 모든 제품 선택
        self.cursor.execute('''
            SELECT * FROM products
        ''')
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()

# 샘플 데이터를 삽입하는 함수
def generate_sample_data(db, count=100):
    product_names = ["TV", "Laptop", "Smartphone", "Tablet", "Smartwatch", "Headphones", "Camera", "Speaker", "Monitor", "Printer"]
    for _ in range(count):
        name = random.choice(product_names) + " " + str(random.randint(1, 100))
        price = round(random.uniform(50.0, 2000.0), 2)
        db.insert_product(name, price)

# 데이터베이스를 사용한 예시
if __name__ == '__main__':
    db = ElectronicsDatabase()
    
    # 샘플 데이터 100개 생성 및 삽입
    generate_sample_data(db)
    
    # 모든 제품 조회
    all_products = db.select_all_products()
    for product in all_products:
        print(product)

    # 예시: 특정 제품 조회
    product = db.select_product(1)
    print(f"Product 1: {product}")

    # 예시: 제품 업데이트
    db.update_product(1, product_name="Updated TV", price=1500.00)

    # 예시: 제품 삭제
    db.delete_product(2)

    db.close()
