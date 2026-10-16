# Tiny Flask API

A minimal Flask API with exactly three resources, all stored in in-memory Python lists:

- `/users`
- `/products`
- `/orders`

The data disappears whenever the server restarts. There is no database.

## Run it

Requires Python 3.9 or newer.

```bash
cd flask-api-project
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

The API runs at `http://127.0.0.1:5000`.

## Routes

Each resource accepts `GET` to list its data and `POST` to create an item.

| Resource | GET | POST body |
| --- | --- | --- |
| `/users` | List users | `{"name": "Ada", "email": "ada@example.com"}` |
| `/products` | List products | `{"name": "Notebook", "price": 7.5}` |
| `/orders` | List orders | `{"user_id": 1, "product_id": 1, "quantity": 2}` |

Create a user and product before creating an order; order IDs must reference existing user and product IDs.

## Example requests

```bash
# Create a user
curl -X POST http://127.0.0.1:5000/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Ada Lovelace","email":"ada@example.com"}'

# Create a product
curl -X POST http://127.0.0.1:5000/products \
  -H "Content-Type: application/json" \
  -d '{"name":"Notebook","price":7.5}'

# Create an order (after the two requests above)
curl -X POST http://127.0.0.1:5000/orders \
  -H "Content-Type: application/json" \
  -d '{"user_id":1,"product_id":1,"quantity":2}'

# List each resource
curl http://127.0.0.1:5000/users
curl http://127.0.0.1:5000/products
curl http://127.0.0.1:5000/orders
```
