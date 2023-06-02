import json

def get_product_code():
  """Gets the product code from the user."""
  while True:
    code = input("Enter the product code: ")
    if code.isdigit():
      return code
    else:
      print("Please enter a valid product code.")

def get_product_info(code):
  """Gets the product information from the file."""
  with open("products.json") as f:
    data = json.load(f)

  for product in data["products"]:
    if product["code"] == code:
      return product

def edit_product_info(product):
  """Edits the product information."""
  while True:
    print("What do you want to edit?")
    print("1. Name")
    print("2. Price")
    print("3. Count")

    option = input("Enter your choice: ")

    if option == "1":
      new_name = input("Enter the new name: ")
      product["name"] = new_name
    elif option == "2":
      new_price = input("Enter the new price: ")
      product["price"] = new_price
    elif option == "3":
      new_count = input("Enter the new count: ")
      product["count"] = new_count
    else:
      break

def remove_product(product):
  """Removes the product from the list."""
  data["products"].remove(product)

def buy_product(product, quantity):
  """Buys the product and adds it to the user's shopping cart."""
  if product["count"] >= quantity:
    product["count"] -= quantity
  else:
    print("The requested quantity is not available.")

def print_invoice(products):
  """Prints the invoice."""
  print("Invoice")
  for product in products:
    print(product["name"], product["price"], product["count"])

  print("Total:", sum([product["price"] * product["count"] for product in products]))

def main():
  """The main function."""
  products = []

  with open("products.json") as f:
    data = json.load(f)

    for product in data["products"]:
      products.append(product)

  while True:
    print("What do you want to do?")
    print("1. Edit product information")
    print("2. Remove product")
    print("3. Buy product")
    print("4. Print invoice")
    print("5. Exit")

    option = input("Enter your choice: ")

    if option == "1":
      product_code = get_product_code()
      product = get_product_info(product_code)
      edit_product_info(product)
    elif option == "2":
      product_code = get_product_code()
      product = get_product_info(product_code)
      remove_product(product)
    elif option == "3":
      product_code = get_product_code()
      product = get_product_info(product_code)
      quantity = input("Enter the quantity: ")
      buy_product(product, quantity)
    elif option == "4":
      print_invoice(products)
    elif option == "5":
      break

  with open("products.json", "w") as f:
    json.dump(data, f, indent=4)

if __name__ == "__main__":
  main()