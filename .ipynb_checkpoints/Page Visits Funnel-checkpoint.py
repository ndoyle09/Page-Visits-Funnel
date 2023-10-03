import pandas as pd
import numpy as np
desired_width=320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',10)


visits = pd.read_csv('visits.csv',parse_dates=[1])
cart = pd.read_csv('cart.csv',parse_dates=[1])
checkout = pd.read_csv('checkout.csv',parse_dates=[1])
purchase = pd.read_csv('purchase.csv',parse_dates=[1])

print(visits.head(1))
print(cart.head(1))
print(checkout.head(1))
print(purchase.head(1))

# Step 1 - Inspect DataFrames
count_of_visits = len(visits)       # 2000
count_of_cart = len(cart)           # 348
count_of_checkout = len(checkout)   # 226
count_of_purchase = len(purchase)   # 252

print(f"""
Total visits: {len(visits)}
Total carts: {len(cart)}
Total checkout: {len(checkout)}
Total purchases: {len(purchase)}
""")

# Step 2 -Join visits and cart tables
visits_cart = pd.merge(visits,cart,how="left")
# print(visits_cart)

# Step 3 - length of Joined visits and cart tables: 2000
length_of_visits_cart = len(visits_cart)
print(f"Step 3. Length of merged visit+cart table: {length_of_visits_cart}")

# Step 4 - count of null cart_time in Joined visit+cart table: 1652
null_cart_times = len(visits_cart[visits_cart.cart_time.isnull()])
print(f"Step 4. Count of null_cart_times: {null_cart_times}")

# Step 5 - percentage of users who visited but did not purchase. null cart_time / total visits
visited_but_didnt_add_to_cart = float(null_cart_times) / float(length_of_visits_cart)
print(f"Step 5. Percent of users who visited, but didn't add to cart: {visited_but_didnt_add_to_cart}")

# Step 6a - Join cart and checkout tables
cart_checkout = pd.merge(
  cart,
  checkout,
  how="left")
# print(cart_checkout)

# Step 6b - length of Joined cart and checkout tables: 422
length_of_cart_checkout = len(cart_checkout)
print(f"Step 6b. Length of cart+checkout table: {length_of_cart_checkout}")

# Step 6c - count of null cart_checkout in Joined cart+checkout table: 122
null_cart_checkout = len(cart_checkout[cart_checkout.checkout_time.isnull()])
print(f"Step 6b. Count of null_cart_checkout: {null_cart_checkout}")

# Step 6d - percentage of users who added to cart but did not checkout. null checkout_time / total cart
added_to_cart_but_didnt_checkout = float(null_cart_checkout) / float(length_of_cart_checkout)
print(f"Step 6d. Percent of users who added to cart, but didn't checkout: {added_to_cart_but_didnt_checkout}")

# Step 7 - create all_data table using a series of left joins on all four tables
all_data = visits.merge(cart, how="left") \
  .merge(checkout, how="left") \
  .merge(purchase, how="left")

# print(all_data.head(5))

# Step 8 - % of users who proceeded to checkout, but did not purchase. not null checkout time / null purchase_time
checkout_time_is_not_null = len(all_data[~all_data.checkout_time.isnull()])
purchase_time_is_null = len(all_data[all_data.purchase_time.isnull()])
purchase_time_is_null_and_checkout_time_is_not_null = len(all_data[all_data.purchase_time.isnull() & ~all_data.checkout_time.isnull()])

# print("checkout time is not null:",checkout_time_is_not_null)
# print("purchase time is null:",purchase_time_is_null)
# print("purchase time is null and checkout time is not null:",purchase_time_is_null_and_checkout_time_is_not_null)
# print(purchase_time_is_null / checkout_time_is_not_null)
# print(purchase_time_is_null_and_checkout_time_is_not_null / checkout_time_is_not_null)

checkout_but_didnt_purchase = float(purchase_time_is_null_and_checkout_time_is_not_null) / float(checkout_time_is_not_null)
print(f"Step 8. Percentage of users who checked out, but didn't purchase: {checkout_but_didnt_purchase}")

# Step 9 - which step has the highest percentage of users not completing it?
print("Step 9. {} percent of users who visited the page but did not add to cart".format(round(visited_but_didnt_add_to_cart*100, 2)))
print("Step 9. {} percent of users who added to cart, but did not checkout".format(round(added_to_cart_but_didnt_checkout*100, 2)))
print("Step 9. {} percent of users who checked out, but did not make a purchase".format(round(checkout_but_didnt_purchase*100, 2)))

"""
The weakest part of the funnel is clearly getting a person who visited the site to add a tshirt to their cart.
Once they've added a t-shirt to their cart it is fairly likely they end up purchasing it.
A suggestion could be to make the add-to-cart button more prominent on the front page.
"""

# Step 10 - purchase_time minus visit_time
all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time

# Step 11 - Examine the results
print(all_data.head())

# Step 12 - Calculate the mean
print("Average time to purchase: ",all_data.time_to_purchase.mean())