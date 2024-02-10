"""Actividad 5.2 Ejercicio 1 - A01250724"""

import argparse
import json
from pathlib import Path
import time

initial_timestamp = time.time()


# Setting up argument parser
parser = argparse.ArgumentParser(
    prog="A01250724 - Actividad 4.2: Ejercicio 1",
    description="Ejercicio 1 de Actividad 4.2 de Pruebas de software y aseguramiento de la calidad",
)

parser.add_argument("catalogue_filepath")
parser.add_argument("sales_filepath")
args = parser.parse_args()


# Reading JSON files
catalogue_filepath = Path(args.catalogue_filepath)
sales_filepath = Path(args.sales_filepath)

if not(
    catalogue_filepath.exists() and
    catalogue_filepath.is_file() and
    catalogue_filepath.suffix==".json"
    ):
    raise ValueError("Ruta a archivo de catálogo inválida")

if not(sales_filepath.exists() and sales_filepath.is_file() and sales_filepath.suffix==".json"):
    raise ValueError("Ruta a archivo de ventas inválida")

with open(catalogue_filepath, encoding="utf-8") as file:
    catalogue_data = json.load(file)

with open(sales_filepath, encoding="utf-8") as file:
    sales_data = json.load(file)

products_prices = {product["title"]: product["price"]
                   for product in catalogue_data if product["price"]>0}


# Calculating sales totals
total = 0
errors = []

for sale in sales_data:
    try:
        sale_product = sale["Product"]
        product_price = products_prices[sale_product]
    except KeyError:
        error_info = f"    Product {sale_product} was not found in the catalogue. Skipping item."
        errors.append(error_info)
        continue
    total += float(product_price) * float(sale["Quantity"])


# Elapsed time calculation
final_timestamp = time.time()
elapsed_time = final_timestamp - initial_timestamp


# Results compilation
results = [
    f"Sales Total: {total:.2f}",
    f"Elapsed Time: {elapsed_time}",
    "Errors: ",
]

results += errors


# Outputting results to terminal and file

with open("SalesResults.txt", "w", encoding="utf-8") as results_file:
    for result in results:
        results_file.write(result + "\n")
        print(result)
