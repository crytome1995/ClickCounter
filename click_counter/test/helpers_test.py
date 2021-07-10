from click_counter import helpers


def _build_payload(country, ip):
    return {helpers.COUNTRY_KEY: country, helpers.IP_KEY: ip}


def test_invalid_country():
    payload = _build_payload("BLAH", "123.123.123.123")
    valid = helpers.validate_request(payload=payload)
    assert valid == False


def test_valid_country():
    payload = _build_payload("US", "123.123.123.123")
    valid = helpers.validate_request(payload=payload)
    assert valid == True


def test_invalid_ip():
    payload = _build_payload("US", "abc.123.123.123")
    valid = helpers.validate_request(payload=payload)
    assert valid == False


def test_invalid_ip2():
    payload = _build_payload("US", "999.123.123.123")
    valid = helpers.validate_request(payload=payload)
    assert valid == False
