def car_listing(car_prices):
  result = ""
  result = "".join(f"{list(car_prices.values())} costs {list(car_prices.keys())} dollars\n")
  """ for car_name, car_price in car_prices.items():
    result += f"{car_name} costs {car_price} dollars\n" """
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))
