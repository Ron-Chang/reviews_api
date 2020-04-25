#built-in
#submodule
from common.data_cache import DataCache
from scraping_tools.super_print import SuperPrint
#project
from core.const import IFOODIE, GOOGLE
from api.ifoodie import IFoodieApi
from api.google import GoogleApi

class SchemaModel:

    @staticmethod
    def suggest(query):
        response = IFoodieApi.suggest(query=query)
        return response

    @staticmethod
    def search_restaurant(query):
        response = IFoodieApi.search_restaurant(query=query)
        return response

    @staticmethod
    def search_location(query):
        response = IFoodieApi.search_location(query=query)
        return response

    @staticmethod
    def search_parking_info(restaurant_id):
        response = IFoodieApi.get_parking_info(restaurant_id=restaurant_id)
        return response

