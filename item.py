class Item(object):

    def __init__(self):
        self._name=''
        self._sku=''
        self._asin=''
        self._price=''
        self._qty = ''
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
    @property
    def sku(self):
        return self._sku
    @sku.setter
    def sku(self, value):
        self._sku = value
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        self._price = value
    @property
    def asin(self):
        return self._asin
    @asin.setter
    def asin(self, value):
        self._asin = value
    @property
    def qty(self):
        return self._qty
    @qty.setter
    def qty(self, value):
        self._qty = value

    def __str__(self):
        return self.name+'\n'+self.sku+'\n'+self.asin+'\n'+self.qty+'\n'+self.price
