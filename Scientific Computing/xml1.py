import xml.etree.ElementTree as ET

data = """ 
	<person>
		<name>Shubhankar</name>
		<phone type='integer'>7889527828</phone>
		<email hide='yes'/>
	</person>
	 """

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Phone:', tree.find('phone').text)
print('Phone:', str(int(tree.find('phone').text)+2))
print('Phone attr:', tree.find('phone').get('type'))
print('Attr:', tree.find('email').get('hide'))