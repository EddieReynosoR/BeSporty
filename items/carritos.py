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

    def add(self, item):
        id=str(item.id)
        if id not in self.cart.keys():
            self.cart[id] = {
                "item_id": item.id,
                "name": item.title,
                "price_acum": float(item.price),
                "type": item.type.name,
                "quantity": 1,
                "size": item.size.sizeName,
            }
        else:
            self.cart[id]["quantity"] +=1
            self.cart[id]["price_acum"] += float(item.price)
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

            if self.cart[id]["quantity"] <= 0: self.delete(item) 
            self.saveCart()

    def clean(self):
        self.session["cart"] = {}
        self.session.modified =True
