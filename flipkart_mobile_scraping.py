from bs4 import BeautifulSoup
import requests
import csv

# url = 'https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1'

# html_file = requests.get(url).text

# with open('product.html') as html_file:
# 	soup = BeautifulSoup(html_file, "html5lib")

# main_component = soup.findAll('div', class_='_1HmYoV _35HD7C')[1]
# list_sub_components = main_component.findAll('div', class_='bhgxx2 col-12-12')
# page_size = int(list_sub_components[-1].find('div', class_='_2zg3yZ').span.text.split('of')[1].strip())
# print page_size

# for sub_component in list_sub_components:
# 	try:
#         # product name
# 		print sub_component.find('div', class_='_3wU53n').text
# 		# product rating
# 		print sub_component.find('div', class_='hGSR34 _2beYZw').text
# 		# product link
# 		print 'https://www.flipkart.com'+sub_component.find('a', class_='_31qSD5', href=True)['href']
# 		# # product price
# 		print sub_component.find('div', class_='_1vC4OE').text
# 	except Exception as e:
# 		print str(e)

def create_csv_file(productName, productRating, productLink, productPrice):
	csv_file = open('flipkard_mobile_details.csv', 'w')
	csv_writer = csv.writer(csv_file)
	csv_writer.writerow([productName, productRating, productLink, productPrice])
	return [csv_writer, csv_file]

def write_each_data_to_csv(csv_writer, productName, productRating, productLink, productPrice):
	csv_writer.writerow([productName, productRating, productLink, productPrice])

def hit_url_and_get_data(page):
	url = 'https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page='+str(page)
	html_file = requests.get(url).text
	soup = BeautifulSoup(html_file, "html5lib")
	return soup

def extract_and_print_data(data_source, csv_writer):
	import ipdb; ipdb.set_trace()
	main_component = data_source.findAll('div', class_='_1HmYoV _35HD7C')[1]
	list_sub_components = main_component.findAll('div', class_='bhgxx2 col-12-12')
	page_size = int(list_sub_components[-1].find('div', class_='_2zg3yZ').span.text.split('of')[1].strip())

	for sub_component in list_sub_components:
		try:
	        # product name
			product_name = sub_component.find('div', class_='_3wU53n').text
			# product rating
			product_rating = sub_component.find('div', class_='hGSR34 _2beYZw').text
			# product link
			product_link = 'https://www.flipkart.com'+sub_component.find('a', class_='_31qSD5', href=True)['href']
			# # product price
			product_price = sub_component.find('div', class_='_1vC4OE').text
			write_each_data_to_csv(csv_writer, product_name, product_rating, product_link, product_price.encode('utf-8').strip().split('\xe2\x82\xb9')[1])

		except Exception as e:
			print str(e)

def get_total_pages(source_data):

    if source_data != None:
        main_component = source_data.findAll('div', class_='_1HmYoV _35HD7C')[1]
        list_sub_components = main_component.findAll('div', class_='bhgxx2 col-12-12')
        return int(list_sub_components[-1].find('div', class_='_2zg3yZ').span.text.split('of')[1].strip())


# create csv
csv_writer = create_csv_file('Product Name', 'Product Rating', 'Product Link', 'Product Price')
# get data
data = hit_url_and_get_data(1)

# get total pages count
total_pages = get_total_pages(data)

# get data of each page and write in csv
for page in range(51, total_pages+1):
	print page
	data = hit_url_and_get_data(page)
	extract_and_print_data(data, csv_writer[0])

csv_writer[1].close()




