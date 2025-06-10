def sorting_cheeses(**kwargs):
    sorted_cheeses = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    
    result = []
    for cheese, quantities in sorted_cheeses:
        result.append(cheese)
        result.extend(str(q) for q in sorted(quantities, reverse=True))
    
    return "\n".join(result)
