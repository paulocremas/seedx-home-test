from config import Sale


def transform(sale):
    return Sale(
        SALE_ID=sale["sale_id"],
        SALE_DATE=sale["sale_date"],
        CUSTOMER_ID=sale["customer_id"],
        PRODUCT_NAME=sale["product_name"],
        AMOUNT=sale["amount"],
        CURRENCY=sale["currency"],
        STATUS=sale["status"],
    ).__dict__
