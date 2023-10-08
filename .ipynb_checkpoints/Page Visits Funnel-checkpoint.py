# 1

import pandas as pd
import numpy as np
from IPython.display import display # Jupyter Notebooks render HTML tables
from plotly import graph_objects as go

visits = pd.read_csv('visits.csv',parse_dates=[1])
cart = pd.read_csv('cart.csv',parse_dates=[1])
checkout = pd.read_csv('checkout.csv',parse_dates=[1])
purchase = pd.read_csv('adj_purchase.csv',parse_dates=[1])

# 2

print("1. Visits:")
display(visits.head(10))
print("2. Cart:")
display(cart.head(10))
print("3. Checkout:")
display(checkout.head(10))
print("4. Purchase:")
display(purchase.head(10))

count_of_visits = len(visits)       # 2000
count_of_cart = len(cart)           # 348
count_of_checkout = len(checkout)   # 226
count_of_purchase = len(purchase)   # 198

print(f"""
Total visits: {len(visits)}
Total carts: {len(cart)}
Total checkout: {len(checkout)}
Total purchases: {len(purchase)}
""")

# 3

visits_cart = pd.merge(visits,cart,how="left")
display(visits_cart)

print(f"Length of merged `visit` + `cart` tables: {len(visits_cart)}")

null_cart_times = len(visits_cart[visits_cart.cart_time.isnull()])
print(f"Length of `null_cart_times`: {null_cart_times}")

visited_but_didnt_add_to_cart = float(null_cart_times) / float(len(visits_cart))
print(f"Percent of users who visited, but didn't add to cart: {visited_but_didnt_add_to_cart}")

# 4

cart_checkout = pd.merge(cart, checkout, how="left")
display(cart_checkout)

print(f"Length of merged `cart` + `checkout` tables: {len(cart_checkout)}")

null_cart_checkout = len(cart_checkout[cart_checkout.checkout_time.isnull()])
print(f"Length of `null_cart_checkout`: {null_cart_checkout}")

added_to_cart_but_didnt_checkout = float(null_cart_checkout) / float(len(cart_checkout))
print(f"Percent of users who added to cart, but didn't checkout: {added_to_cart_but_didnt_checkout}")

# 5

all_data = visits.merge(cart, how="left").merge(checkout, how="left").merge(purchase, how="left")
display(all_data.head(5))

checkout_time_is_not_null = len(all_data[~all_data.checkout_time.isnull()])
purchase_time_is_null = len(all_data[all_data.purchase_time.isnull()])
purchase_time_is_null_and_checkout_time_is_not_null = len(all_data[all_data.purchase_time.isnull() & ~all_data.checkout_time.isnull()])

print("`checkout_time` is not null:",checkout_time_is_not_null)
print("`purchase time` is null:",purchase_time_is_null)
print("`purchase_time_is_null_and_checkout_time_is_not_null`:",purchase_time_is_null_and_checkout_time_is_not_null)

checkout_but_didnt_purchase = float(purchase_time_is_null_and_checkout_time_is_not_null) / float(checkout_time_is_not_null)
print(f"Percentage of users who checked out, but didn't purchase: {checkout_but_didnt_purchase}")

# 6

all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time
display(all_data.head())
print("Average time to purchase: ",all_data.time_to_purchase.mean())

# 7

fig = go.Figure(
    go.Funnel(
        y = ["Visits", "Carts", "Checkout", "Purchase"],
        x = [count_of_visits, count_of_cart, count_of_checkout, count_of_purchase],
        textposition = "inside",
        textinfo = "value+percent initial",
        opacity = 1, marker = {"color": ["#562c2c", "#f2542d", "#f5dfbb", "#0e9594"]}
    )
)
fig.update_layout(
    autosize=False,
    width=800,
    height=800,
)
fig.show()
