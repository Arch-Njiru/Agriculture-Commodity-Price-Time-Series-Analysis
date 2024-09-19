import scrapy
import os
import csv

class CommoditySpider(scrapy.Spider):
    name = "commodities"

    # List of products to scrape from product 190 to 272
    product_ids = list(range(190, 273))  # This will generate a list from 190 to 272 inclusive

    per_page = 3000  # Number of rows per page
    completed_products = []  # To track completed products
    
    def start_requests(self):
        """Initiate the scraping requests for the selected products."""
        for product_id in self.product_ids:
            url = f'https://amis.co.ke/site/market?product={product_id}&per_page={self.per_page}'
            yield scrapy.Request(url=url, callback=self.parse, meta={'product_id': product_id, 'page_number': 1})

    def parse(self, response):
        """Parse the table rows and handle pagination."""
        product_id = response.meta['product_id']
        page_number = response.meta['page_number']

        # Get the product name from the response and use it to create the CSV file name
        commodity_name = response.css('tr:nth-child(2) td:nth-child(1)::text').get()
        if commodity_name:
            commodity_name_cleaned = commodity_name.strip().replace(' ', '_').replace('/', '_')
            csv_file_name = f"{commodity_name_cleaned}.csv"  # CSV file name based on the commodity name
        else:
            csv_file_name = f"product_{product_id}.csv"  # Fallback in case the product name is missing

        # Initialize the CSV file and write the headers if it's the first page for the product
        if page_number == 1 and not os.path.exists(csv_file_name):
            headers = ['commodity', 'classification', 'grade', 'market', 'wholesale', 'retail', 'supply_volume', 'county', 'date']
            with open(csv_file_name, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(headers)

        # Write scraped data to the CSV file
        for row in response.css('tr'):
            data = {
                'commodity': row.css('td:nth-child(1)::text').get(),
                'classification': row.css('td:nth-child(2)::text').get(),
                'grade': row.css('td:nth-child(3)::text').get(),
                'market': row.css('td:nth-child(5)::text').get(),
                'wholesale': self.extract_price(row.css('td:nth-child(6)::text').get()),
                'retail': self.extract_price(row.css('td:nth-child(7)::text').get()),
                'supply_volume': row.css('td:nth-child(8)::text').get(default='N/A'),
                'county': row.css('td:nth-child(9)::text').get(),
                'date': row.css('td:nth-child(10)::text').get(),
            }

            if data['commodity']:  # Skip any empty rows
                with open(csv_file_name, 'a', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow(data.values())

        # Handle pagination
        next_page_url = f"https://amis.co.ke/site/market/{self.per_page * page_number}?product={product_id}&per_page={self.per_page}"
        if len(response.css('tr')) > 1:  # Check if there are more rows (pagination needed)
            yield scrapy.Request(next_page_url, callback=self.parse, meta={'product_id': product_id, 'page_number': page_number + 1})
        else:
            # Mark product as completed
            self.completed_products.append(product_id)
            self.log(f"Completed scraping product {product_id} ({commodity_name}).")

    def extract_price(self, price_str):
        """Extract price and handle missing or empty values."""
        if price_str and price_str.strip() != '-' and price_str.strip():
            return price_str.split('/')[0].strip()
        else:
            return 'N/A'

    def close(self, reason):
        """Handle the shutdown and print summary of completed products."""
        self.log(f"Scraping completed for the following products: {self.completed_products}")
