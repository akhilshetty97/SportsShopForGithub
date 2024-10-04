
few_shots = [
    {'Question' : "How many total Adidas products do we have left?",
     'SQLQuery' : "SELECT sum(stock) FROM products WHERE brand = 'Adidas'",
     'SQLResult': "Result of the SQL query",
     'Answer' : "220"},
    {'Question': "How much is the total price of the inventory for all Adidas products?",
     'SQLQuery':"SELECT SUM(price*stock) FROM products WHERE brand = 'Adidas'",
     'SQLResult': "Result of the SQL query",
     'Answer': "8247.80"},
    {'Question': "If we have to sell all the Nike products today with discounts applied. How much revenue  our store will generate (post discounts)?" ,
     'SQLQuery' : """SELECT sum(a.total_amount * ((100-COALESCE(discounts.discount_percent,0))/100)) as total_revenue from
(select sum(price*stock) as total_amount, product_id from products where brand = 'Nike'
group by product_id) a left join discounts on a.product_id = discounts.product_id
 """,
     'SQLResult': "Result of the SQL query",
     'Answer': "'3144.235"},
]



