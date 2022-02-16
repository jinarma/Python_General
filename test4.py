from math import ceil


n1 = 'boi'
n2 = 'gay'
def swp(n1,n2):
	temp = n1
	n1 = n2
	n2 = temp
	return(n1, n2)
print(n1, n2)
n1, n2 = swp(n1, n2)
print(n1, n2)
print()
print()
print()

dict1 = {
	'sup':'nig',
	'dank':'true',
	'dik':'Bro'
}
print(dict1['sup'])
dict1['sup'] = dict1['dank']
print(dict1['sup'])
print()
print()
print()
ls1 = ['mysore', 'bangalore']
ls1.sort()
print(ls1)
print(ceil(9/4))