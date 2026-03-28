from flask import Flask
from pyspark.sql import SparkSession
import os

app = Flask(__name__)

# Get or create Spark session
spark = SparkSession.builder.getOrCreate()

@app.route("/")
def index():
    df = spark.sql("SELECT * FROM my_catalog.my_database.my_table")
    columns = df.columns
    rows = df.collect()

    # Build HTML table
    rows_html = ""
    for row in rows:
        rows_html += "<tr>" + "".join(f"<td>{cell}</td>" for cell in row) + "</tr>"

    headers_html = "".join(f"<th>{col}</th>" for col in columns)

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Table</title>
        <style>
            body {{ font-family: Arial, sans-serif; padding: 40px; }}
            table {{ border-collapse: collapse; width: 100%; }}
            th, td {{ border: 1px solid #ccc; padding: 10px; text-align: left; }}
            th {{ background-color: #4CAF50; color: white; }}
            tr:nth-child(even) {{ background-color: #f2f2f2; }}
        </style>
    </head>
    <body>
        <h2>my_table entries</h2>
        <table>
            <thead><tr>{headers_html}</tr></thead>
            <tbody>{rows_html}</tbody>
        </table>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)