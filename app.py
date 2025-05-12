from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Function to create a connection to MySQL
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Rahul@123",
        database="student"
    )

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        grad_year = request.form['gradYear']
        branch = request.form['branch']
        position = request.form['position']

        conn = get_connection()
        cursor = conn.cursor()
        insert_query = """
            INSERT INTO applicants (name, email, phone, address, grad_year, branch, position)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (name, email, phone, address, grad_year, branch, position))
        conn.commit()
        cursor.close()
        conn.close()

        return "Application submitted successfully!"

    return render_template('uploads/form.html')
@app.route('/records')
def show_records():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM applicants")
    records = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('uploads/records.html', applicants=records)

if __name__ == '__main__':
    app.run(debug=True)
