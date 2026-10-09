productName1 = "Green Tea"
productName2 = "Black Tea"
productName3 = "White Tea"

productNames = [productName1, productName2, productName3]
productNames.append("Oolong Tea")
productNames.insert(2, "Herbal Tea")

productNames.remove("Black Tea")
print(productNames[1:3])
print("Green Tea" in productNames)

# for product in productNames:
#     print(product)

# print(productNames[3])

for i in range(len(productNames)):
    print(f"Product {i + 1}: {productNames[i]}")


mixed_list = [productName1, 42, True, 3.14, "Herbal Tea"]
for item in mixed_list:
    print(f"Item: {item}, Type: {type(item)}")
