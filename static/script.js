document.addEventListener('DOMContentLoaded', (event) => {
    document.getElementById('addRowButton').addEventListener('click', addRow);
    document.getElementById('removeRowButton').addEventListener('click', removeLastRow);
});

function addRow() {
    const tableBody = document.getElementById('transaction-table').getElementsByTagName('tbody')[0];
    const newRow = document.createElement('tr');
    newRow.classList.add('data-row');
    newRow.innerHTML = `
        <td><input type="text" name="category[]" placeholder="Enter Category" required></td>
        <td><input type="number" name="amount[]" placeholder="Enter Amount" step="0.01" required></td>
        <td>
            <select name="type[]" required>
                <option value="" disabled selected>Placeholder</option>
                <option value="Expense">Expense</option>
                <option value="Income">Income</option>
            </select>
        </td>
    `;
    tableBody.appendChild(newRow);
}

function removeLastRow() {
    const tableBody = document.getElementById('transaction-table').getElementsByTagName('tbody')[0];
    const rows = tableBody.getElementsByClassName('data-row');
    if (rows.length > 0) {
        tableBody.removeChild(rows[rows.length - 1]);
    }
}