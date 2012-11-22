from scrapy.item import Item, Field

def strip_and_join(values):
    value = values[0].strip()
    joined = u' '.join(value.split('\n'))
    return joined.replace('\r', '')

class Pybr8TalksItem(Item):
    title = Field()
    description = Field(serializer=strip_and_join)
    author_name = Field(serializer=strip_and_join)
    author_profile = Field(serializer=strip_and_join)
