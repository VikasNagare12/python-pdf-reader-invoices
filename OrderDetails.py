class order_details:


    def __init__(self) -> None:
        self.custmer_name = ''
        self.addres = ''
        self.pancard_number=''
        self.gst_registraction_number=''
        self.pincode=''
        self.order_number=''
        self.order_date=''
        self.item_discription=[]
        self.item_price=[]

    @property.setter
    def custmer_name(self, value):
        self.custmer_name=value

    @property.setter
    

    def __str__(self) -> str:
        pass