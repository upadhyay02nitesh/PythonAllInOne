# XML - Extensible Markup Language
# Used for store and transport data ,it just similar To Html but here you
# can create own tags

# Elemettree is used to represent whole xml document as a single tree

print("Read Sample.xml file this directory")

# import xml.etree.ElementTree as ET

# file_path = "sample.xml"

# tree = ET.parse(file_path)
# root = tree.getroot()

# customer_id = root.find('customer').get('id')
# customer_name = root.find('customer/name').text

# print(f"Customer ID: {customer_id}")
# print(f"Customer Name: {customer_name}")

# # Print addresses
# print("Addresses:")
# for address in root.findall('customer/address'):
#     street = address.find('street').text if address.find('street') is not None else "N/A"
#     city = address.find('city').text if address.find('city') is not None else "N/A"
#     state = address.find('state').text if address.find('state') is not None else "N/A"
#     zip_code = address.find('zip').text if address.find('zip') is not None else "N/A"

#     print(f"Street: {street}, City: {city}, State: {state}, ZIP: {zip_code}")


print("write Sample1.xml file this directory")

import xml.etree.ElementTree as ET 

root=ET.Element("root")

child1=ET.SubElement(root,'child1')
child2=ET.SubElement(root,'child2')

child1.text="Hi I Am Child 1"
child2.text="Hi I Am Child 2"

tree=ET.ElementTree(root)
tree.write("sample1.xml")
print("Xml Writing Done")