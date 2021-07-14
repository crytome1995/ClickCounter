from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from dynamo import Dynamo
from config import config
from helpers import COUNTRY_KEY, IP_KEY, validate_request
from loggers import logger

db = Dynamo(config.default_region, config.click_bags_table, config.click_users_table)

app = Flask(__name__)
CORS(app)

bad_request = {"message": "bad_request"}
ok = {"message": "ok"}
internal_error = {"message": "internal_error"}


@app.route("/click", methods=["POST"])
def click():
    payload = request.get_json()
    logger.info("Payload: {}".format(str(payload)))
    if not validate_request(payload):
        return make_response(jsonify(bad_request)), 400
    country = payload[COUNTRY_KEY]
    ip = payload[IP_KEY]
    if db.update_country_click_count(country):
        db.insert_country_ip(country, ip)
        return make_response(jsonify(ok)), 200
    else:
        return make_response(jsonify(bad_request)), 500


@app.route("/healthcheck", methods=["GET"])
def healthcheck():
    if db:
        return make_response(jsonify(ok)), 200
    else:
        return make_response(jsonify(bad_request)), 500
