import ast
import json
from scraping_tools.log_stash import LogStash
from datetime import datetime
from flask import request, jsonify, url_for, redirect
from common.response_handler import ResponseHandler
from app import app, db
from core.schema_model import SchemaModel


@app.route('/probe', methods=['GET'])
def probe():
    return 'ok', 200

###########################################################
# IFOODIE #################################################
###########################################################

## 建議搜尋 ##
@app.route('/suggest/<string:query>', methods=['GET'])
def get_ifoodie_suggest(query):
    results = SchemaModel.suggest(query=query)
    return ResponseHandler.jsonify(results=results)

## 搜尋餐廳 ##
@app.route('/restaurant/<string:query>', methods=['GET'])
def get_ifoodie_results_by_restaurant(query):
    results = SchemaModel.search_restaurant(query=query)
    return ResponseHandler.jsonify(results=results)

## 搜尋地點 ##
@app.route('/location/<string:query>', methods=['GET'])
def get_ifoodie_results_by_location(query):
    results = SchemaModel.search_location(query=query)
    return ResponseHandler.jsonify(results=results)

## 探索目標 ##
@app.route('/explore/<string:query>', methods=['GET'])
def get_ifoodie_explore(query):
    results = SchemaModel.explore(query=query)
    return ResponseHandler.jsonify(results=results)

###########################################################
# GOOGLE ##################################################
###########################################################

# # 全文檢索
# @app.route('/search/<string:sub_string>', methods=['GET'])
# @CommonUtils.language_gate()
# def search(language, sub_string):
#     if not RouteUtils.validate_search_string(_string=sub_string):
#         raise ValidationError(error_code=ErrorCodeDefine.INVALID_OPERATION)
#     response = SportApi.search(sub_string=sub_string)
#     results = ResponseHandler.unpack_response(response=response)
#     return ResponseHandler.jsonify(results=results)

# ## FIFA ##
# ## 排名清單 ##
# @app.route('/info/fifa/ranks/<string:gender>', methods=['GET'])
# @CommonUtils.language_gate()
# def fifa_ranks(language, gender):
#     sort_by = request.args.get('sort_by', None)
#     date = request.args.get('date', None)
#     results = SchemaModel.fifa_ranks(gender=gender, date=date, sort_by=sort_by)
#     return ResponseHandler.jsonify(results=results)
