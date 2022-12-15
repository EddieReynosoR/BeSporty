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

    def add(self, item, size, quantity):
        # order = sorted(self.cart)
        # print(order)
        i = 0
        # while i < len(self.cart.keys()):
        #     print(str(i))
        #     i+=1
        # print(self.cart)
        cart2 = {}
        for key in self.cart.keys():
            cart2[str(i)] = self.cart[key].copy()
            i+=1
        # print(cart2)
        self.cart = {}
        self.cart = cart2.copy()
        print(self.cart)
        id=0
        print(self.cart.keys())
        
        if str(id) not in self.cart.keys() and item.id not in self.cart.values():
            self.cart[str(id)] = {
                "item_id": item.id,
                "uid": item.id,
                "name": item.title,
                "price": float(item.price),
                "price_acum": round(float(item.price)*int(quantity),2),
                "type": item.type.name,
                "quantity": int(quantity),
                "size": size,
                "image": item.image.url
            }
            # print(self.cart)
        else:
            if self.cart[str(id)]["item_id"] == item.id and self.cart[str(id)]["size"] == size:
                    # print(id)
                    if int(str(quantity))>1:
                        self.cart[str(id)]["quantity"] += int(quantity)
                        self.cart[str(id)]["price_acum"] += round(float(item.price)*int(quantity),2)
                        self.cart[str(id)]["price_acum"] = round(self.cart[str(id)]["price_acum"])
                    else:
                        self.cart[str(id)]["quantity"] +=1
                        self.cart[str(id)]["price_acum"] += float(item.price)
                        self.cart[str(id)]["price_acum"] = round(self.cart[str(id)]["price_acum"])

                    # print(self.cart[str(id)])
            
            else:
                while str(id) in self.cart.keys():
                    if self.cart[str(id)]["item_id"] == item.id and self.cart[str(id)]["size"] == size:
                        break
                    else:
                        id += 1
                    # print(id)
                if str(id) not in self.cart.keys():
                    self.cart[str(id)] = {
                    "item_id": item.id,
                    "uid": item.id,
                    "name": item.title,
                    "price": float(item.price),
                    "price_acum": round(float(item.price)*int(quantity),2),
                    "type": item.type.name,
                    "quantity": int(quantity),
                    "size": size,
                    "image": item.image.url
                }
                    # print(self.cart)
                else:
                    if self.cart[str(id)]["item_id"] == item.id and self.cart[str(id)]["size"] == size:
                        # print(id)
                        if int(str(quantity))>1:
                            # print(id)
                            self.cart[str(id)]["quantity"] += int(quantity)
                            self.cart[str(id)]["price_acum"] += round(float(item.price)*int(quantity),2),
                            self.cart[str(id)]["price_acum"] = round(self.cart[str(id)]["price_acum"])
                        else:
                            # print(self.cart)
                            self.cart[str(id)]["quantity"] +=1
                            self.cart[str(id)]["price_acum"] += float(item.price)
                            self.cart[str(id)]["price_acum"] = round(self.cart[str(id)]["price_acum"])

                        # print(self.cart[str(id-1)] 
        self.saveCart()
        
    def saveCart(self):
        self.session["cart"] = self.cart
        self.session.modified = True
    
    def delete(self, key):
        id = key
        print(self.cart.keys())
        if id in self.cart:
            self.cart.pop(str(id))
            print(self.cart)
            self.saveCart()

    def substractItem(self, item, key):
        id = key
        print(id)
        if str(id) in self.cart.keys():
            self.cart[str(id)]["quantity"] -= 1
            self.cart[str(id)]["price_acum"] -= float(item.price)
            self.cart[str(id)]["price_acum"] = round(self.cart[str(id)]["price_acum"],2)
            if self.cart[str(id)]["quantity"] <= 0: self.cart.pop(str(id))
            print(self.cart)
            self.saveCart()

    def clean(self):
        self.session["cart"] = {}
        self.session.modified =True
