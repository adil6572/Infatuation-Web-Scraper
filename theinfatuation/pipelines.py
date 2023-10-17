
from itemadapter import ItemAdapter
from datetime import datetime


class ReviewItemPipeline:
    def process_item(self, item, spider):
        item_adapter = ItemAdapter(item)

        # Convert review_rating to a float (if not empty)
        review_rating = item_adapter.get("review_rating", "")
        if review_rating:
            item_adapter["review_rating"] = float(review_rating[0])
        else:
            item_adapter["review_rating"] = ""

        # Convert restaurant_cost to string (if not empty)
        restaurant_cost = item_adapter.get("restaurant_cost")
        if restaurant_cost:
            item_adapter["restaurant_cost"] = int(restaurant_cost[0])*"$"
        else:
            item_adapter["restaurant_cost"] = ''

        # Convert review_date to "YYYY-MM-DD" format (if not empty)
        review_date = item_adapter.get("review_date", "")
        if review_date:
            date_object = datetime.strptime(review_date, "%B %d, %Y")
            formatted_date = date_object.strftime("%Y-%m-%d")
            item_adapter["review_date"] = formatted_date

        # Returning Clean item
        return item
