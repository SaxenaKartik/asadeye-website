
Models for asadeye-website 

1. UserProfile
	- id : Int
	- name : String
	- email : Email
	- password : Password
	- phone_no : Phone Number	

1. Address
	- user_id : Int (Foreign Key)
	- id : Int
	- address_line_1 : String
	- address_line_2 : String
	- landmark : String
	- state : String
	- city : String
	- pincode : String

1. Orders
	- order_id : Int
	- user_id : Int (Foreign Key)
	- [product_ids] : List[Int] 
	- order_price : Double
	- address_id : Int (Foreign Key)
	- order_date : Date

1. Products
	- id : Int
	- product_name : String
	- product_price : Double 
	- product_desc : String

1. Images
	- id : Int
	- image_name : String 
	- path : File
	- product_id : Object of type product (Foreign key)

1. Wishlist
	- user_id : Int
	- [product_id] : List[Int]

1. Cart
	- user_id : Int (Foreign Key)
	- number_of_products : Int
	- [product_ids] : List[Int]
	- cart_total : Double

