def total(request):
    total = 0
    if request.user.is_authenticated:
        if "cart" in request.session.keys():
            for key, value in request.session["cart"].items():
                total += float(value["price_acum"])
    return {"total_cost": total}

def totalQuantity(request):
    totalQ = 0
    if request.user.is_authenticated:
        if "cart" in request.session.keys():
            for key, value in request.session["cart"].items():
                totalQ += int(value["quantity"])
    return {"total_quantity": totalQ}