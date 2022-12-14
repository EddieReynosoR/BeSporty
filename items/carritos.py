class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            self.session["cart"] = {}
            self.cart = self.session["cart"]
        else:
            self.cart = cart

    def add(self, item, size,quantity):
        id=str(item.id)
        if id not in self.cart.keys():
            self.cart[id] = {
                "item_id": item.id,
                "name": item.title,
                "price_acum": round(float(item.price)*int(quantity),2),
                "type": item.type.name,
                "quantity": int(quantity),
                "size": size,
            }
        elif int(str(quantity))>1:
            self.cart[id]["quantity"] += int(quantity)
            self.cart[id]["price_acum"] += float(item.price)*int(quantity)
            self.cart[id]["price_acum"] = round(self.cart[id]["price_acum"],2)
        else:
            self.cart[id]["quantity"] +=1
            self.cart[id]["price_acum"] += float(item.price)
            self.cart[id]["price_acum"] = round(self.cart[id]["price_acum"],2)
        self.saveCart()

    def saveCart(self):
        self.session["cart"] = self.cart
        self.session.modified = True
    
    def delete(self, item):
        id =str(item.id)
        if id in self.cart:
            del self.cart[id]
            self.saveCart()

    def substractItem(self, item):
        id = str(item.id)
        if id in self.cart.keys():
            self.cart[id]["quantity"] -= 1
            self.cart[id]["price_acum"] -= float(item.price)
            self.cart[id]["price_acum"] = round(self.cart[id]["price_acum"],2)
            if self.cart[id]["quantity"] <= 0: self.delete(item) 
            self.saveCart()

    def clean(self):
        self.session["cart"] = {}
        self.session.modified =True