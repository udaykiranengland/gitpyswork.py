from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ProductWiseSales").getOrCreate()

products_df = spark.read.csv("C:\\Users\\Uday Kiran\\PycharmProjects\\pysparkProject1\\products.csv", header=True)
sales_df = spark.read.csv("C:/Users/Uday Kiran/PycharmProjects\pysparkProject1\sales.csv", header=True)

sales_df.createOrReplaceTempView("sales_data")
products_df.createOrReplaceTempView("products_data")

product_wise_sales = spark.sql("""
SELECT product_name, SUM(num_pieces_sold) as total_sales
FROM sales_data s
JOIN products_data p ON s.product_id = p.product_id
GROUP BY product_name
""")

product_wise_sales.show(15)

product_highest_sales = spark.sql("""
SELECT product_name, SUM(num_pieces_sold) as total_sales
FROM sales_data s
JOIN products_data p ON s.product_id = p.product_id
GROUP BY product_name
ORDER BY total_sales DESC
LIMIT 1
""")

product_highest_sales.show(3)