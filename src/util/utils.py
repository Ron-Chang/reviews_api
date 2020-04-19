import json
from core.const import IFOODIE


class APIUtils:

    @staticmethod
    def convert_to_price_level(attr):
        if not attr.isdigit():
            return None
        price = ast.literal_eval(attr)
        if price < 0:
            return None
        if price < 150:
            return 1
        if 150 <= price < 600:
            return 2
        if 600 <= price < 1200:
            return 3
        if price >= 1200:
            return 4

    @staticmethod
    def extact_json(soup):
        data = soup.find('script', IFOODIE.LABEL.JSON_DATA_TAG)
        data_text = data.get_text() if data else None
        if not data_text:
            return None
        return json.loads(data_text)
