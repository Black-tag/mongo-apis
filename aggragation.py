# Modify imports for each tutorial as needed.
from datetime import datetime

from pymongo import MongoClient

# Replace the placeholder with your connection string.
uri = "mongodb://localhost:27017"
client = MongoClient(uri)

try:
    agg_db = client["agg_tutorials_db"]
    person_coll = agg_db["persons"]

    # person_data = [
    #     {
    #         "person_id": "6392529400",
    #         "firstname": "Elise",
    #         "lastname": "Smith",
    #         "dateofbirth": datetime(1972, 1, 13, 9, 32, 7),
    #         "vocation": "ENGINEER",
    #         "address": {
    #             "number": 5625,
    #             "street": "Tipa Circle",
    #             "city": "Wojzinmoj",
    #         },
    #     },
    #     {
    #         "person_id": "1723338115",
    #         "firstname": "Olive",
    #         "lastname": "Ranieri",
    #         "dateofbirth": datetime(1985, 5, 12, 23, 14, 30),
    #         "gender": "FEMALE",
    #         "vocation": "ENGINEER",
    #         "address": {
    #             "number": 9303,
    #             "street": "Mele Circle",
    #             "city": "Tobihbo",
    #         },
    #     },
    #     {
    #         "person_id": "8732762874",
    #         "firstname": "Toni",
    #         "lastname": "Jones",
    #         "dateofbirth": datetime(1991, 11, 23, 16, 53, 56),
    #         "vocation": "POLITICIAN",
    #         "address": {
    #             "number": 1,
    #             "street": "High Street",
    #             "city": "Upper Abbeywoodington",
    #         },
    #     },
    #     {
    #         "person_id": "7363629563",
    #         "firstname": "Bert",
    #         "lastname": "Gooding",
    #         "dateofbirth": datetime(1941, 4, 7, 22, 11, 52),
    #         "vocation": "FLORIST",
    #         "address": {
    #             "number": 13,
    #             "street": "Upper Bold Road",
    #             "city": "Redringtonville",
    #         },
    #     },
    #     {
    #         "person_id": "1029648329",
    #         "firstname": "Sophie",
    #         "lastname": "Celements",
    #         "dateofbirth": datetime(1959, 7, 6, 17, 35, 45),
    #         "vocation": "ENGINEER",
    #         "address": {
    #             "number": 5,
    #             "street": "Innings Close",
    #             "city": "Basilbridge",
    #         },
    #     },
    #     {
    #         "person_id": "7363626383",
    #         "firstname": "Carl",
    #         "lastname": "Simmons",
    #         "dateofbirth": datetime(1998, 12, 26, 13, 13, 55),
    #         "vocation": "ENGINEER",
    #         "address": {
    #             "number": 187,
    #             "street": "Hillside Road",
    #             "city": "Kenningford",
    #         },
    #     },
    # ]
    # person_coll.insert_many(person_data)
    # orders_coll = agg_db["orders"]

    # order_data = [
    # {
    #     "customer_id": "elise_smith@myemail.com",
    #     "orderdate": datetime(2020, 5, 30, 8, 35, 52),
    #     "value": 231,
    # },
    # {
    #     "customer_id": "elise_smith@myemail.com",
    #     "orderdate": datetime(2020, 1, 13, 9, 32, 7),
    #     "value": 99,
    # },
    # {
    #     "customer_id": "oranieri@warmmail.com",
    #     "orderdate": datetime(2020, 1, 1, 8, 25, 37),
    #     "value": 63,
    # },
    # {
    #     "customer_id": "tj@wheresmyemail.com",
    #     "orderdate": datetime(2019, 5, 28, 19, 13, 32),
    #     "value": 2,
    # },
    # {
    #     "customer_id": "tj@wheresmyemail.com",
    #     "orderdate": datetime(2020, 11, 23, 22, 56, 53),
    #     "value": 187,
    # },
    # {
    #     "customer_id": "tj@wheresmyemail.com",
    #     "orderdate": datetime(2020, 8, 18, 23, 4, 48),
    #     "value": 4,
    # },
    # {
    #     "customer_id": "elise_smith@myemail.com",
    #     "orderdate": datetime(2020, 12, 26, 8, 55, 46),
    #     "value": 4,
    # },
    # {
    #     "customer_id": "tj@wheresmyemail.com",
    #     "orderdate": datetime(2021, 2, 28, 7, 49, 32),
    #     "value": 1024,
    # },
    # {
    #     "customer_id": "elise_smith@myemail.com",
    #     "orderdate": datetime(2020, 10, 3, 13, 49, 44),
    #     "value": 102,
    # },
    # ]

    # orders_coll.insert_many(order_data)

    orders_coll = agg_db["orders"]

    order_data = [
    {
        "order_id": 6363763262239,
        "products": [
            {
                "prod_id": "abc12345",
                "name": "Asus Laptop",
                "price": 431,
            },
            {
                "prod_id": "def45678",
                "name": "Karcher Hose Set",
                "price": 22,
            },
        ],
    },
    {
        "order_id": 1197372932325,
        "products": [
            {
                "prod_id": "abc12345",
                "name": "Asus Laptop",
                "price": 429,
            }
        ],
    },
    {
        "order_id": 9812343774839,
        "products": [
            {
                "prod_id": "pqr88223",
                "name": "Morphy Richards Food Mixer",
                "price": 431,
            },
            {
                "prod_id": "def45678",
                "name": "Karcher Hose Set",
                "price": 21,
            },
        ],
    },
    {
        "order_id": 4433997244387,
        "products": [
            {
                "prod_id": "def45678",
                "name": "Karcher Hose Set",
                "price": 23,
            },
            {
                "prod_id": "jkl77336",
                "name": "Picky Pencil Sharpener",
                "price": 1,
            },
            {
                "prod_id": "xyz11228",
                "name": "Russell Hobbs Chrome Kettle",
                "price": 16,
            },
        ],
    },
]

    orders_coll.insert_many(order_data)



    

    # Get a reference to relevant collections.
    # ... some_coll = agg_db["some_coll"]
    # ... another_coll = agg_db["another_coll"]

    # Delete any existing documents in collections if needed.
    # ... some_coll.delete_many({})

    # Insert sample data into the collection or collections.
    # ... some_coll.insert_many(...)

    # Create an empty pipeline array.
    pipeline = []
    # pipeline.append({"$match": {"vocation": "ENGINEER"}})
    # pipeline.append({"$sort": {"dateofbirth": 1}})
    # pipeline.append({"$limit": 5})
    # pipeline.append({"$unset": ["_id", "address"]})
    # pipeline.append({"$match": {
    #     "orderdate": {
    #         "$gte":datetime(2020, 1, 1, 0, 0, 0), 
    #         "$lt":datetime(2021, 1, 1, 0, 0, 0),
    #     }
    # }})


    # pipeline.append({"$sort": {"orderdate": 1}})
    # pipeline.append({
    #     "$group": {
    #         "_id": "$customer_id",
    #         "first_purchase_date": {"$first": "$orderdate"},
    #         "total_value": {"$sum": "$value"},
    #         "total_orders": {"$sum": 1},
    #         "orders": {"$push": {"orderdate": "$orderdate", "value": "$value"}},

    #     }
    # })
    # pipeline.append({"$sort": {"first_purchase_date": 1}})
    # pipeline.append({"$set": {"customer_id": "$_id"}})
    # pipeline.append({"$unset": ["_id"]})

    pipeline.append({"$unwind": {"path": "$products"}})
    pipeline.append({"$match": {"products.price": {"$gt": 15}}})
    pipeline.append(
    {
        "$group": {
            "_id": "$products.prod_id",
            "product": {"$first": "$products.name"},
            "total_value": {"$sum": "$products.price"},
            "quantity": {"$sum": 1},
        }
    }
)
    pipeline.append({"$set": {"product_id": "$_id"}})
    pipeline.append({"$unset": ["_id"]})

    

    aggregation_result = orders_coll.aggregate(pipeline)

    # Print the aggregation results.
    for document in aggregation_result:
        print(document)

finally:
    client.close()


