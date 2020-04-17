#built-in
#submodule
from common.data_cache import DataCache
from scraping_tools.super_print import SuperPrint
#project
from core.const import REVIEWS
# from core.sport_api import SportApi

class SchemaModel:

    @staticmethod
    def test():
        return f'Hello! my name is Ron! Rating: {DataCache.get_google_rating(restaurant_id=100)}'
