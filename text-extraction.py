#%%
import fitz
from os import listdir

files = [f for f in listdir('./OrderData/amz')]
print(files[0])
doc = fitz.open('./OrderData/amz/amazon-pdf-croppers2nn4gTVpHvr9qJvui7KzBq.pdf')
doctext = ""
names=[]
address=[]
pan_no=[]
gst_reg_no=[]
pincode=[]
order_no=[]
order_date=[]
item_description=[]
item_price=[]
NAME_EXTRACTION='Sold By :'
ORDER_NUMBER_EXTRACTION='Order Number:'
ORDER_DATEEXTRACTION='Order Date:'
PAN_NUMBER_EXTRACTION='PAN No:'
GST_NUMBER_EXTRACTION='GST Registration No:'
PINCODE_EXTRACTION = 'Billing Address :'

for page in doc:                            # iterate the document pages
    text_extracted = page.getText()    # get plain text (is in UTF-8)
    print(text_extracted)
    text_extraction_list= text_extracted.split('\n')
    text_extraction_list.index(ORDER_NUMBER_EXTRACTION)
    
    doctext = doctext + text_extracted


def get_extracted_info_single_line(line):
    return line.split(':')[1]

# %%
print(doctext)
add=''
i=2
while m[m.index('Sold By :')+i] !='IN':
    add+=m[m.index('Sold By :')+i] 
    i+=1
add=add+' IN'
m = doctext.split('\n')
print(add)



# %%
