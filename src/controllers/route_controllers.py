import ast
import json
from datetime import datetime
from flask import request, jsonify, url_for, redirect
from common.response_handler import ResponseHandler
from app import app, db
from core.schema_model import SchemaModel


###########################################################
# 清單資訊 #################################################
###########################################################

## TEST ##
## testing ##
@app.route('/test', methods=['GET'])
def test():
    results = SchemaModel.test()
    return ResponseHandler.jsonify(results=results)

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
