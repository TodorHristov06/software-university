def grocery_store(**products):
    sorted_products = sorted(
        products.items(),
        key=lambda x: (-x[1], -len(x[0]), x[0])
    )
    
    result_lines = [f"{name}: {quantity}" for name, quantity in sorted_products]
    return '\n'.join(result_lines)
