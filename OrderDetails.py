class order_details(object):
    """[summary]
    """
    def __init__(self) -> None:
        self._customer_name = ''
        self._address = ''
        self._pancard_number=''
        self._gst_registraction_number=''
        self._pincode=''
        self._order_number=''
        self._order_date=''
        self._item_description=[]

    @property
    def customer_name(self):
        return self._customer_name

    @customer_name.setter
    def customer_name(self, value):
        self._customer_name=value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address=value

    @property
    def pancard_number(self):
        return self._pancard_number

    @pancard_number.setter
    def pancard_number(self, value):
        self._pancard_number = value


    @property
    def gst_registraction_number(self):
        return self._gst_registraction_number

    @gst_registraction_number.setter
    def gst_registraction_number(self , value):
        self._gst_registraction_number = value

    @property
    def pincode(self):
        return self._pincode

    @pincode.setter
    def pincode(self, value):
        self._pincode = value

    @property
    def order_date(self):
        return self._order_date

    @order_date.setter
    def order_date(self,value):
        self._order_date = value

    @property
    def order_number(self):
        return self._order_number

    @order_number.setter
    def order_number(self,value):
        self._order_number = value

    @property
    def item_description(self):
        return self._item_description

    @item_description.setter
    def item_description(self, value):
        self._item_description = value

    def __str__(self):
        items = '\n'.join([e.__str__() for e in self.item_description])
        return self.customer_name+'\n'+self.address+'\n'+self.pancard_number+'\n'+self.gst_registraction_number+'\n'+self.pincode+'\n'+self.order_number+'\n'+self.order_date+' \n'+items+'\n'
