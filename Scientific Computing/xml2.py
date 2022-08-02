import xml.etree.ElementTree as ET
data = """ 
	<stuff>
		<users>
			<user x='2'>
				<id>001</id>
				<name>Jinu</name>
			</user>
			<user x='7'>
				<id>009</id>
				<name>Shubhankar</name>
			</user>
		</users>
	</stuff>
	 """

xml_string = ET.fromstring(data)
lst = xml_string.findall('users/user')
print(f'User count: {len(lst)}')

for ele in lst:
	print(f'Name: {ele.find("name").text}')
	print(f'Id: {ele.find("id").text}')
	print(f'Attribute: {ele.get("x")}')