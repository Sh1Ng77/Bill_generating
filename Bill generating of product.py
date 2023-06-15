
print("\tBill of product, purchased by you\n")
class store:
	product_code=[]
	product_name=[]
	product_price=[]

	def input_data(self):
		for i in range(3):
			self.product_code.append(int(input("Enter product code :  ")))
			self.product_name.append(input("Enter product name :  "))
			self.product_price.append(float(input("Enter product price :  ")))

	def display_data(self):
		print("product code\t","product name\t\t","product price")
		for i in range(3):
			print("\t",self.product_code[i],"\t\t","\t\t",self.product_name[i],"\t\t\t",self.product_price[i])

	def generate_bill(self):
		total=0
		for i in range(3):
			total=total+self.product_price[i]*qty[i]
		for i in range(3):
			print("\t\t",self.product_code[i],"\t",self.product_name[i],"\t",self.product_price[i],"\t\t",qty[i])
			print("total:-",total)

s=store()
s.input_data()
s.display_data()

qty=[]
for i in range(3):
	print("enter quantity of %d product"% int(i+1))
	qty.append(int(input()))
s.generate_bill()
