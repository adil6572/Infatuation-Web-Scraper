import random
import scrapy
from pathlib import Path
from bs4 import BeautifulSoup
from theinfatuation.items import ReviewItem

from settings import USER_AGENTS


class ReviewSpider(scrapy.Spider):
    name = "Review"
    allowed_domains = ["www.theinfatuation.com"]
    start_urls = ["https://www.theinfatuation.com/new-york/reviews"]

    custom_settings = {
        "FEEDS": {
            "Reviews.json": {"format": "json", "overwrite": True}
        }
    }
    base_url = "https://www.theinfatuation.com/new-york/reviews?page="

# Create a list of URLs by iterating from 1 to 157

    def start_requests(self):
        # urls = [
        #     "https://www.theinfatuation.com/new-york/reviews",
        # ]
        urls = [self.base_url + str(pageNo) for pageNo in range(1, 158)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # print(response.request.url)

        href_values = response.css(
            'a[data-testid="detailedStory-link"]::attr(href)').extract()

        for link in href_values:
            request_link = "http://www.theinfatuation.com" + link
            yield scrapy.Request(request_link, callback=self.parse_review, headers={"user-agent": USER_AGENTS[random.randint(0, len(USER_AGENTS)-1)]})

    def parse_review(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        restaurant_name = response.css("h1 ::text").get()
        restaurant_cuisine = response.css(
            'span.cuisineTag a[data-testid="tag-tagLink"]::text').get()
        restaurant_location = response.css(
            'span.neighborhoodTag a[data-testid="tag-tagLink"]::text').get()
        restaurant_cost = response.css(
            'span.css-utujt7 ::attr(data-price)').extract()
        review_rating = response.css(
            'div[data-testid="ratingBadge-rating"]::text').extract()
        review_date = response.css('time::text').get()

        food_rundown_element = response.xpath("//*[@id='foodRundown']/div")
        food_runddown = {}
        if food_rundown_element is not None:
            for item in food_rundown_element:
                title = item.xpath(".//h2/text()").get()
                paragraph = item.xpath(".//p/text()").get()
                food_runddown[title] = paragraph
        else:
            food_runddown = ""
        review_item = ReviewItem()

        css_selector = ".styles_richText__a6C_c.flatplan_body > p"
        selected_elements = soup.select(css_selector)

        # Extract the text from the selected elements
        review_text = [element.get_text() for element in selected_elements]

        # Now you have the extracted text in the 'extracted_text' list

        review_item["review_url"] = response.request.url
        review_item["restaurant_name"] = restaurant_name
        review_item["restaurant_cuisine"] = restaurant_cuisine
        review_item["restaurant_location"] = restaurant_location
        review_item["restaurant_cost"] = restaurant_cost
        review_item["review_date"] = review_date
        review_item["review_rating"] = review_rating
        review_item["food_runddown"] = food_runddown
        review_item["review_text"] = review_text

        yield review_item
