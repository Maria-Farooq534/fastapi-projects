
from flask import Flask, request, render_template_string

app = Flask(__name__)

template = """
<!DOCTYPE html>
<html>
<head>
    <title>Multiplication Table</title>
</head>
<body>
    <h1>Multiplication Table</h1>

    <form method="POST">
        <label>Enter a number:</label>
        <input type="number" name="number" required>
        <button type="submit">Submit</button>
    </form>

    {% if number is not none %}
        <h2>Table of {{ number }}</h2>
        <table>
            <tr><th>Multiplier</th><th>Result</th></tr>
            {% for i in range(1, 11) %}
            <tr>
                <td>{{ number }} × {{ i }}</td>
                <td>{{ number * i }}</td>
            </tr>
            {% endfor %}
        </table>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    number = None

    if request.method == "POST":
        number = int(request.form["number"])

    return render_template_string(template, number=number)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
