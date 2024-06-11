import matplotlib
matplotlib.use('Agg')  # Use the Agg backend for rendering plots

from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os
import matplotlib.pyplot as plt

app = Flask(__name__)

# Ensure the uploads directory exists
os.makedirs("uploads", exist_ok=True)

# Define the data structure for expenses and income
data = {'Category': [], 'Amount': [], 'Type': []}

# Function to save data to CSV
def save_data():
    df = pd.DataFrame(data)
    df.to_csv('uploads/finance_data.csv', index=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    categories = request.form.getlist('category[]')
    amounts = request.form.getlist('amount[]')
    types = request.form.getlist('type[]')

    for category, amount, type_ in zip(categories, amounts, types):
        data['Category'].append(category)
        data['Amount'].append(float(amount))
        data['Type'].append(type_)
    save_data()
    return redirect(url_for('index'))

@app.route('/visualize')
def visualize():
    df = pd.read_csv('uploads/finance_data.csv')
    df.groupby('Category')['Amount'].sum().plot(kind='bar')
    plt.savefig('static/expense_chart.png')
    plt.close()  # Close to free memory
    return render_template('visualize.html')

if __name__ == "__main__":
    app.run(debug=True)