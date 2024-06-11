# BudgetBuddy - Personal Finance Tracker

## Project Overview

**BudgetBuddy** is a simple web application designed to help users track and visualize their personal expenses and income. Users can input their transactions, categorize them, and then visualize their spending habits through automatically generated charts. 

## Features

- **Input Transactions:** Add multiple transactions by entering the category, amount, and type (Expense/Income).
- **Dynamic Rows:** Add or remove rows dynamically for ease of input.
- **Data Storage:** Transactions are stored in a CSV file for persistent data management.
- **Data Visualization:** Generate bar charts to visualize spending and income distribution by category.
- **Responsive Design:** The main page layout will be updated for a more user-friendly experience.

## Future Enhancements

- **Chart Customization:** Updates will be made to improve the appearance and functionality of the charts.
- **Main Page Design:** The design of the main page will be enhanced based on user feedback.
- **Feedback Mechanism:** A section for users to provide feedback and suggestions will be added.

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- Pandas
- Matplotlib

### Installation

1. **Clone the Repository:**

   \`\`\`bash
   git clone https://github.com/yourusername/budgetbuddy.git
   cd budgetbuddy
   \`\`\`

2. **Install Required Packages:**

   \`\`\`bash
   pip install flask pandas matplotlib
   \`\`\`

### Running the Application

1. **Start the Flask Server:**

   \`\`\`bash
   python app.py
   \`\`\`

2. **Open the Application:**

   Open your web browser and navigate to `http://127.0.0.1:5000`.

## Project Structure

\`\`\`
budgetbuddy/
├── app.py
├── templates/
│   ├── index.html
│   └── visualize.html
├── static/
│   ├── styles.css
│   └── script.js
├── uploads/
│   └── finance_data.csv
└── README.md
\`\`\`

### Key Files

- **app.py:** The main Flask application file that handles routes and data processing.
- **index.html:** The main page where users can input their transactions.
- **visualize.html:** The page that displays the generated chart.
- **styles.css:** Contains the styles for the web pages.
- **script.js:** JavaScript file for handling dynamic row addition and removal.

## Contributing

We welcome contributions to improve BudgetBuddy! Please fork the repository and create a pull request with your changes. Make sure to follow the coding standards and include relevant tests.

## Feedback

Your feedback is valuable to us! Please provide any suggestions or comments by opening an issue on the GitHub repository or by contacting us directly.
