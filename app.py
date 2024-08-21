from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all origins

# Email configuration
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
SMTP_USERNAME = 'your-email@example.com'
SMTP_PASSWORD = 'your-email-password'
FROM_EMAIL = 'your-email@example.com'

def send_confirmation_email(to_email, order_id):
    subject = 'Order Confirmation'
    body = f'Your order {order_id} has been confirmed!'
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = FROM_EMAIL
    msg['To'] = to_email
    
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(FROM_EMAIL, to_email, msg.as_string())
    except Exception as e:
        print(f'Error sending email: {e}')

@app.route('/order', methods=['GET'])
def create_order():
    #data = request.json
    #order_id = data.get('order_id')
    #customer_email = data.get('email')
    
    # Order processing logic (e.g., saving to database) goes here
    
    #send_confirmation_email(customer_email, order_id)
    
    return jsonify({'status': 'Order confirmed', 'order_id': 12345}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
