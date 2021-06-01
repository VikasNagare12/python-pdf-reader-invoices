class order_details(object):
    """[summary]
    """
    def __init__(self) -> None:
        self.customer_name = ''
        self.address = ''
        self.pancard_number=''
        self.gst_registraction_number=''
        self.pincode=''
        self.order_number=''
        self.order_date=''
        self.item_description=[]
        self.item_price=[]

    @property.setter
    def customer_name(self, value):
        self.customer_name=value

    @property
    def customer_name(self):
        return self.customer_name

    @property.setter
    def address(self, value)->None:
        self.address=value

    @property
    def address(self)->str:
        return self.address

    @property.setter
    def pancard_number(self, value):
        self.pancard_number = value

    @property
    def pancard_number(self):
        return self.pancard_number

    @property.setter
    def gst_registraction_number(self , value):
        self.gst_registraction_number = value

    @property
    def gst_registraction_number(self):
        return self.gst_registraction_number

    @property.setter
    def pincode(self, value):
        self.pincode = value

    @property
    def pincode(self):
        return self.pincode
    @property.setter
    def order_date(self,value):
        self.order_date = value
    @property
    def order_date(self):
        return self.order_date

    @property.setter
    def order_number(self,value):
        self.order_number = value

    @property
    def order_number(self):
        return self.order_number
    @property.setter
    def item_price(self, value):
        self.item_price = value

    @property
    def item_price(self):
        return self.item_price

    @property.setter
    def item_description(self, value):
        self.item_description = value
    @property
    def item_description(self):
        return self.item_description

