from datetime import datetime, timedelta

def generate_month_table(start_month, start_year, rows, cols, base_url):
    current_date = datetime.now()
    current_month_year = current_date.strftime('%B %Y')
    start_date = datetime(start_year, start_month, 1)

    total_months = rows * cols
    month_list = [
        (start_date + timedelta(days=30 * i)).strftime('%B %Y')
        for i in range(total_months)
    ]

    while month_list[-1] != current_month_year:
        start_date -= timedelta(days=30)
        month_list = [
            (start_date + timedelta(days=30 * i)).strftime('%B %Y')
            for i in range(total_months)
        ]

    # Start generating the table
    table = '<table border="1" style="border-collapse: collapse; width: 100%;">'
    table += '<thead><tr><th colspan="{}" style="text-align: center;">Months Table</th></tr></thead>'.format(cols)
    table += '<tbody>'
    for i in range(rows):
        table += '<tr>'
        for c in range(cols):
            month_year = month_list.pop(0)
            month, year = month_year.split(' ')
            link = f"{base_url}?month={month}&year={year}"
            if month_year == current_month_year:
                table += f'<td style="background-color: yellow; text-align: center;"><a href="{link}" style="text-decoration: none; color: black;">{month_year}</a></td>'
            else:
                table += f'<td style="text-align: center;"><a href="{link}" style="text-decoration: none; color: black;">{month_year}</a></td>'
        table += '</tr>'
    table += '</tbody>'
    table += '</table>'

    return table

# Generate the HTML content
base_url = 'dashboard'  # Adjust this to the actual URL of your payroll view
table_html = generate_month_table(6, 2024, 3, 4, base_url)

html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    {table_html}
</body>
</html>
"""

# Write to an HTML file
with open("generated_months_table.html", "w") as file:
    file.write(html_content)

print("HTML file generated successfully: generated_months_table.html")
