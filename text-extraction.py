#%%
from OrderDetails import order_details
import fitz
import re
from os import listdir
from item import Item
item_description=[]
item_price=[]
NAME_EXTRACTION='Sold By :'
PINCODE_EXTRACTION = 'Billing Address :'
data=[]
files = [f for f in listdir('./OrderData/amz')]

def getSKUNameQty(MainSubString):
    item = Item()
    start=re.search(r" \| [A-Z0-9]{10} \(", MainSubString).start()+15
    end = MainSubString.rfind(")")
    if MainSubString.count("-₹")>0:
        start_qty=MainSubString.find("-₹") + len("-₹")
    else:
        start_qty=MainSubString.find("₹") + len("₹")
    re.search(r'(|)[ ][\w\d]{10}[ ][(]',MainSubString).group()
    item.name =MainSubString[2:MainSubString.index(re.search(r'[|][ ][\w\d]{10}[ ][()]',MainSubString).group())].strip().replace("\n"," ")
    item.sku=MainSubString[start:end].strip().replace("\n"," ")
    item.qty=MainSubString[start_qty:start_qty+12].replace("\n"," ").split(" ")[1]
    item.asin= re.search(r'[|][ ][\w\d]{10}[ ][()]',MainSubString).group().split()[1]
    item.price=MainSubString[MainSubString.rfind('₹') : len(MainSubString)]
    return item
#asin
for file in files:
    print(file)
    if file=='.DS_Store':
        continue
    for page in fitz.open('./OrderData/amz/'+file):
        i=2
        items=[]
        address=''
        finalString={}
        text_extracted = page.getText()
        if text_extracted =='':
            continue
        orderDetails = order_details()
        _start = text_extracted.find("Amount\nTotal\nAmount") +  len("Amount\nTotal\nAmount")
        _end = text_extracted.rfind("TOTAL:")
        MainSubString=text_extracted[_start:_end].strip().replace("\n"," ")
        replacement_order=""
        if "Original Order" in MainSubString:
            replacement_order="Rep.|"
        if MainSubString.count("₹") > 7:
            start=re.search(r" \| [A-Z0-9]{10} \(", MainSubString).start()+15
            end = MainSubString.rfind(")")
            start_qty=MainSubString.find("₹") + len("₹")
            StringToWrite=""
            totalCount=int((MainSubString.count("₹")-MainSubString.count("-₹"))/4)
            isError=0
            for q in range(1,totalCount+1):
                try:
                    if q==1:
                        startIndx=re.search(r''+str(q)+' [a-zA-Z]', MainSubString).start()
                    else:
                        startIndx=re.search(r'SGST .* '+str(q)+' [a-zA-Z]', MainSubString)
                        startIndx=len(startIndx.group())+startIndx.start()
                except:
                    isError=1
                try:
                    endIndx=re.search(r'SGST .* '+str(q+1)+" [a-zA-Z]", MainSubString)
                    endIndx=len(endIndx.group())+endIndx.start()
                except:
                    endIndx=len(MainSubString)-1
                if isError == 1:
                    isError=0
                    finalString["StringToWrite"]="Multi Order"
                else:
                    items.append(getSKUNameQty(MainSubString[startIndx:endIndx]))
                    '''if q==1: #q%4 means after 3 sku it should goes to new line
                        StringToWrite=finalString["sku"]+" | Qty: "+ finalString["qty"]
                        finalString["StringToWrite"]=StringToWrite
                    else:
                        StringToWrite=StringToWrite+" # "+finalString["sku"]+" | Qty: "+ finalString["qty"]
                        finalString["StringToWrite"]=StringToWrite
                    '''
        else:
            items.append(getSKUNameQty(MainSubString))
            #finalString["StringToWrite"]=replacement_order+finalString["sku"]+" | "+ finalString["name"] +" | Qty: "+ finalString["qty"]

        orderDetails.item_description=items
        text_extraction_list= text_extracted.split('\n')
        orderDetails.customer_name = text_extraction_list[text_extraction_list.index(NAME_EXTRACTION)+1]
        while text_extraction_list[text_extraction_list.index(PINCODE_EXTRACTION)+i] != 'IN':
            address =  text_extraction_list[text_extraction_list.index(PINCODE_EXTRACTION)+i]
            i+=1
        orderDetails.address = address+' IN'
        address =''
        i=3
        while text_extraction_list[text_extraction_list.index(NAME_EXTRACTION)+i] != 'IN':
            address +=  text_extraction_list[text_extraction_list.index(NAME_EXTRACTION)+i]
            i+=1
        orderDetails.pincode= address.split()[-1:][0]
        orderDetails.pancard_number =re.search(r'(PAN No:)(.*)',text_extracted).group().split(': ')[1]
        orderDetails.gst_registraction_number=re.search(r'(GST Registration No:)(.*)',text_extracted).group().split(': ')[1]
        orderDetails.order_date = re.search(r'(Order Date:)(.*)',text_extracted).group().split(':')[1]
        orderDetails.order_number= re.search(r'(Order Number:)(.*)',text_extracted).group().split(': ')[1]
        data.append(orderDetails)
        if file =='amazon-pdf-croppersJtJDikEionTn7JacdoQCNA.pdf':
            print(text_extracted)
        print(orderDetails,'\n\n')




# %%
