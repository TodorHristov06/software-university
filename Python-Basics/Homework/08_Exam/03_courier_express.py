Standard = {
    "Less_than_1kg" : 0.03,
    "Between_1_and_10kg" : 0.05,
    "Between_10_and_40kg" : 0.10,
    "Between_40_and_90kg" : 0.15,
    "Between_90_and_150kg" : 0.20
}

Express = {
    "Less_than_1kg" : 0.03,
    "Between_1_and_10kg" : 0.05,
    "Between_10_and_40kg" : 0.10,
    "Between_40_and_90kg" : 0.15,
    "Between_90_and_150kg" : 0.20
}

shipment_weight = float(input()) 
shipment_type = input() 
distance = int(input())  

if shipment_type == "standard":
    if shipment_weight < 1:
        price_per_km = Standard["Less_than_1kg"]
    elif 1 <= shipment_weight <= 10:
        price_per_km = Standard["Between_1_and_10kg"]
    elif 10 <= shipment_weight <= 40:
        price_per_km = Standard["Between_10_and_40kg"]
    elif 40 <= shipment_weight <= 90:
        price_per_km = Standard["Between_40_and_90kg"]
    elif 90 <= shipment_weight <= 150:
        price_per_km = Standard["Between_90_and_150kg"]
    total_price = price_per_km * distance
    print(f"The delivery of your shipment with weight of {shipment_weight:.3f} kg. would cost {total_price:.2f} lv.")

elif shipment_type == "express":
    if shipment_weight < 1:
        price_per_km = Express["Less_than_1kg"]
    elif 1 <= shipment_weight <= 10:
        price_per_km = Express["Between_1_and_10kg"]
    elif 10 <= shipment_weight <= 40:
        price_per_km = Express["Between_10_and_40kg"]
    elif 40 <= shipment_weight <= 90:
        price_per_km = Express["Between_40_and_90kg"]
    elif 90 <= shipment_weight <= 150:
        price_per_km = Express["Between_90_and_150kg"]

    surcharge_per_kg = 0
    if shipment_weight < 1:
        surcharge_per_kg = price_per_km * 0.80
    elif 1 <= shipment_weight <= 10:
        surcharge_per_kg = price_per_km * 0.40
    elif 10 <= shipment_weight <= 40:
        surcharge_per_kg = price_per_km * 0.05
    elif 40 <= shipment_weight <= 90:
        surcharge_per_kg = price_per_km * 0.02
    elif 90 <= shipment_weight <= 150:
        surcharge_per_kg = price_per_km * 0.01

    total_surcharge = surcharge_per_kg * shipment_weight * distance
    total_price = price_per_km * distance + total_surcharge
    print(f"The delivery of your shipment with weight of {shipment_weight:.3f} kg. would cost {total_price:.2f} lv.")
