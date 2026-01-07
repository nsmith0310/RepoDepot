class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.c=0
        self.discount = discount
        self.n = n
        
        self.cat = dict()
        i = 0
        while i<len(products):
            self.cat[products[i]]=prices[i]
            i+=1
        

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.c+=1
        if self.c==self.n:
            cost = 0
            i = 0
            while i<len(product):
                cost+=amount[i]*self.cat[product[i]]
                i+=1
            self.c = 0
            return cost - (self.discount*cost)/100
        else:
            cost = 0
            i = 0
            while i<len(product):
                cost+=amount[i]*self.cat[product[i]]
                i+=1
            
            return cost
            


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
