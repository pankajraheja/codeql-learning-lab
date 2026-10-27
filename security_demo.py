import sqlite3
from flask import Flask, request

app = Flask(__name__)


@app.get("/lookup")
def lookup():
    customer = request.args.get("customer", "")

    with sqlite3.connect(":memory:") as connection:
        connection.execute(
            "CREATE TABLE orders (customer TEXT, status TEXT)"
        )

        query = (
            "SELECT status FROM orders "
            f"WHERE customer = '{customer}'"
        )

        rows = connection.execute(query).fetchall()

    return {"orders": rows}
