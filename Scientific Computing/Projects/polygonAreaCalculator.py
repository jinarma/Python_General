class Rectangle:
	def __init__(self, width, height):
		self.width = width
		self.height = height

	def __str__(self):
		return f'Rectangle(width={self.width}, height={self.height})'

	def set_width(self, width):
		self.width = width

	def set_height(self, height):
		self.height = height

	def get_area(self):
		return self.width * self.height

	def get_perimeter(self):
		return 2 * (self.width + self.height)

	def get_diagonal(self):
		return (self.width ** 2 + self.height ** 2) ** .5

	def get_picture(self):
		if self.width > 50 or self.height > 50:
			return 'Too big for picture.'
		else:
			res = ''
			for _ in range(self.height):
				res += '*'*self.width+'\n'
		return res

	def get_amount_inside(self, shape):
		# print(self, shape)
		rows, columns = 0, 0
		
		donor_width = self.width
		donor_height = self.height
		occupant_width = shape.width
		occupant_height = shape.height
		while True:
			if donor_width >= occupant_width and donor_height >= occupant_height:
				while donor_width >= occupant_width:
					donor_width -= occupant_width
					rows += 1
			while donor_height >= occupant_height:
				donor_height -= occupant_height
				columns += 1
			break
		return rows * columns
				
class Square(Rectangle):
	
	def __init__(self, side):
		# super().__init__(width=side, height=side)
		self.side = side
		super().__init__(side, side)

	def __str__(self):
		return f'Square(side={self.side})'

	def set_side(self, side):
		self.side = side
		super().set_width(side)
		super().set_height(side)
		
	def set_width(self, width):
		super().set_width(width)
		self.side = width

	def set_height(self, height):
		super().set_height(height)
		self.side = height


rect = Rectangle(15, 10)
print(rect.get_area())
# rect.set_width(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
# print(sq.side)
sq.set_side(5)
print(sq.get_area())
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

print(rect.get_amount_inside(sq))
print(sq.get_amount_inside(rect))
sq.set_width(3)
sq.set_side(2)
print(sq.get_picture())