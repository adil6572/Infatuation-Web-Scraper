import scrapy


class ReviewItem(scrapy.Item):
    review_url = scrapy.Field()
    restaurant_name = scrapy.Field()
    restaurant_cuisine = scrapy.Field()
    restaurant_location = scrapy.Field()
    restaurant_cost = scrapy.Field()
    review_date = scrapy.Field()
    review_rating = scrapy.Field()
    food_runddown = scrapy.Field()
    review_text = scrapy.Field()
