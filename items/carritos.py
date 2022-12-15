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
    
        id=0
        # print(self.cart)
        if str(id) not in self.cart.keys():
            self.cart[id] = {
                "item_id": item.id,
                "uid": item.id,
                "name": item.title,
                "price": float(item.price),
                "price_acum": round(float(item.price)*int(quantity),2),
                "type": item.type.name,
                "quantity": int(quantity),
                "size": size,
            }
        else:
            if self.cart[str(id)]["item_id"] == item.id and self.cart[str(id)]["size"] == size:
                    # print(id)
                    if int(str(quantity))>1:
                        self.cart[str(id)]["quantity"] += int(quantity)
                        self.cart[str(id)]["price_acum"] += float(item.price)
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
                    self.cart[id] = {
                    "item_id": item.id,
                    "uid": item.id,
                    "name": item.title,
                    "price": float(item.price),
                    "price_acum": round(float(item.price)*int(quantity),2),
                    "type": item.type.name,
                    "quantity": int(quantity),
                    "size": size,
                }
                else:
                    if self.cart[str(id)]["item_id"] == item.id and self.cart[str(id)]["size"] == size:
                        # print(id)
                        if int(str(quantity))>1:
                            print(id)
                            self.cart[str(id)]["quantity"] += int(quantity)
                            self.cart[str(id)]["price_acum"] += float(item.price)
                            self.cart[str(id)]["price_acum"] = round(self.cart[str(id)]["price_acum"])
                        else:
                            self.cart[str(id)]["quantity"] +=1
                            self.cart[str(id)]["price_acum"] += float(item.price)
                            self.cart[str(id)]["price_acum"] = round(self.cart[str(id)]["price_acum"])

                        # print(self.cart[str(id-1)]
            
            
            
            

            # if self.cart[str(id)]["item_id"] == item.id and self.cart[str(id)]["size"] != size:
            #     self.cart[str(id)] = {
            #         "item_id": item.id,
            #         "uid": item.id,
            #         "name": item.title,
            #         "price": float(item.price),
            #         "price_acum": round(float(item.price)*int(quantity),2),
            #         "type": item.type.name,
            #         "quantity": int(quantity),
            #         "size": size,
            #     }

                

           


        # print(self.cart)
        self.saveCart()
        # id = str(item.id)
        # if id not in self.cart.keys():
        #     self.cart[id] = {
        #         "item_id": item.id,
        #         "uid": item.id,
        #         "name": item.title,
        #         "price": float(item.price),
        #         "price_acum": round(float(item.price)*int(quantity),2),
        #         "type": item.type.name,
        #         "quantity": int(quantity),
        #         "size": size,
        #     }
        # elif int(str(quantity))>1:
            
        #     if self.cart[id]["size"] != size:
        #         id = len(self.cart.keys())+1
        #         self.cart[id] = {
        #         "item_id": item.id, 
        #         "uid": id,
        #         "name": item.title,
        #         "price": float(item.price),
        #         "price_acum": round(float(item.price)*int(quantity),2),
        #         "type": item.type.name,
        #         "quantity": int(quantity),
        #         "size": size,
        #     }
        #     else:
        #         self.cart[id]["quantity"] += int(quantity)
        #         self.cart[id]["price_acum"] += float(item.price)*int(quantity)
        #         self.cart[id]["price_acum"] = round(self.cart[id]["price_acum"],2)
        # else:
        #     self.cart[id]["quantity"] +=1
        #     self.cart[id]["price_acum"] += float(item.price)
        #     self.cart[id]["price_acum"] = round(self.cart[id]["price_acum"],2)
        # self.saveCart()

    def saveCart(self):
        self.session["cart"] = self.cart
        self.session.modified = True
    
    def delete(self, item):
        id =str(item.id)
        if id in self.cart:
            del self.cart[id]
            self.saveCart()

    def substractItem(self, item, key):
        id = key
        print(id)
        if str(id) in self.cart.keys():
            self.cart[str(id)]["quantity"] -= 1
            self.cart[str(id)]["price_acum"] -= float(item.price)
            self.cart[str(id)]["price_acum"] = round(self.cart[str(id)]["price_acum"],2)
            if self.cart[str(id)]["quantity"] <= 0: self.cart.pop(str(id))
            self.saveCart()

    def clean(self):
        self.session["cart"] = {}
        self.session.modified =True
