from flask import Flask, render_template, request, jsonify, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

# In-memory database (for demonstration purposes)
user_data = {}

@app.route('/')
def index():
    loggedInUser = session.get('user')  # Get user info from session
    return render_template('index.html', loggedInUser=loggedInUser)

@app.route('/api/signup', methods=['POST'])
def signup():
    data = request.json
    # Check if user already exists
    if data['email'] in user_data:
        return jsonify({"message": "User already exists!"}), 409
    
    user_data[data['email']] = data
    return jsonify({"message": "User signed up successfully!"}), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    user_info = user_data.get(data['email'])
    
    if user_info and user_info['password'] == data['password']:
        session['user'] = {
            'name': user_info['name'],  # Assuming 'name' is part of the user data
            'email': user_info['email'],
            'age': user_info['age'],
            'gender': user_info['gender'],
            'phone': user_info['phone'],
            'address': user_info['address'],
            'jobTitle': user_info['jobTitle'],
            'company': user_info['company'],
            'experience': user_info['experience'],
            'skills': user_info['skills']
        }
        return jsonify({"message": "Login successful!", "data": user_info}), 200
    
    return jsonify({"message": "Invalid credentials!"}), 401

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user', None)  # Remove user from session
    return jsonify({"message": "Logout successful!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
