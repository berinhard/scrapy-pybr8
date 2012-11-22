from scrapy.item import Item, Field

class Pybr8TalksItem(Item):
    title = Field()
    description = Field()
    author_name = Field()
    author_profile = Field()
