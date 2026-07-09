from fastapi import FastAPI, Query
import os

app = FastAPI()

# ==========================================
# VULNERABLE VERSION (For your first screenshot)
# ==========================================
# Uncomment the line below to trigger a Secret Scanning alert (Hardcoded Secret)
# SECRET_API_KEY = "sk_live_1234567890abcdef1234567890abcdef"

# ==========================================
# SECURE VERSION (For your final screenshot)
# ==========================================
# Use environment variables instead of hardcoding secrets in the source code
SECRET_API_KEY = os.getenv("API_KEY", "default_safe_key_for_dev")

# Mock database
PRODUCTS = {
    "101": {"name": "Laptop", "price": 1200},
    "102": {"name": "Wireless Mouse", "price": 25},
}

@app.get("/search")
def search_product(product_id: str = Query(..., description="Enter product ID")):
    """Simple business action: Product lookup"""
    if product_id in PRODUCTS:
        return {"status": "success", "data": PRODUCTS[product_id]}
    return {"status": "error", "message": "Product not found"}
