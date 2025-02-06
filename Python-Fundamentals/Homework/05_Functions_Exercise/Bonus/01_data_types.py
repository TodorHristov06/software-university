# V1 (if-else)
# def format_type(data_type: str, value: str):
#     if data_type == "int":
#         return int(value) * 2
#     elif data_type == "real":
#         return f"{float(value) * 1.5:.2f}"
#     else:
#         return f"${value}$"

# data_type = input()
# value = input()

# print(format_type(data_type, value))

#V2 (case)
# def format_type(data_type: str, value: str):
#    match data_type:
#       case "int":
#          return int(value) * 2
#       case "real":
#          return f"{float(value) * 1.5:.2f}"
#       case "string":
#          return f"${value}$"
#       case _:
#          return "Invalid type"

# data_type = input()
# value = input()

# print(format_type(data_type, value))

def format_type(data_type: str, value: str):
    actions = {
        "int": lambda x: int(x) * 2,
        "real": lambda x: f"{float(x) * 1.5:.2}",
        "string": lambda x: f"${x}$"
    }
    return actions.get(data_type, lambda x: "Invalid type")(value)

data_type = input()
value = input()

print(format_type(data_type, value))
