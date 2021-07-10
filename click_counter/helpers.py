from loggers import logger

COUNTRY_KEY = "country"
IP_KEY = "ip"
CODES = [
    "ZW",
    "ZM",
    "ZA",
    "YT",
    "YE",
    "WS",
    "WF",
    "VU",
    "VN",
    "VI",
    "VG",
    "VE",
    "VC",
    "VA",
    "UZ",
    "UY",
    "US",
    "UM",
    "UG",
    "UA",
    "TZ",
    "TW",
    "TV",
    "TT",
    "TR",
    "TO",
    "TN",
    "TM",
    "TL",
    "TK",
    "TJ",
    "TH",
    "TG",
    "TF",
    "TD",
    "TC",
    "SZ",
    "SY",
    "SX",
    "SV",
    "ST",
    "SS",
    "SR",
    "SO",
    "SN",
    "SM",
    "SL",
    "SK",
    "SJ",
    "SI",
    "SH",
    "SG",
    "SE",
    "SD",
    "SC",
    "SB",
    "SA",
    "RW",
    "RU",
    "RS",
    "RO",
    "RE",
    "QA",
    "PY",
    "PW",
    "PT",
    "PS",
    "PR",
    "PN",
    "PM",
    "PL",
    "PK",
    "PH",
    "PG",
    "PF",
    "PE",
    "PA",
    "OM",
    "NZ",
    "NU",
    "NR",
    "NP",
    "NO",
    "NL",
    "NI",
    "NG",
    "NF",
    "NE",
    "NC",
    "NA",
    "MZ",
    "MY",
    "MX",
    "MW",
    "MV",
    "MU",
    "MT",
    "MS",
    "MR",
    "MQ",
    "MP",
    "MO",
    "MN",
    "MM",
    "ML",
    "MK",
    "MH",
    "MG",
    "MF",
    "ME",
    "MD",
    "MC",
    "MA",
    "LY",
    "LV",
    "LU",
    "LT",
    "LS",
    "LR",
    "LK",
    "LI",
    "LC",
    "LB",
    "LA",
    "KZ",
    "KY",
    "KW",
    "KR",
    "KP",
    "KN",
    "KM",
    "KI",
    "KH",
    "KG",
    "KE",
    "JP",
    "JO",
    "JM",
    "JE",
    "IT",
    "IS",
    "IR",
    "IQ",
    "IO",
    "IN",
    "IM",
    "IL",
    "IE",
    "ID",
    "HU",
    "HT",
    "HR",
    "HN",
    "HM",
    "HK",
    "GY",
    "GW",
    "GU",
    "GT",
    "GS",
    "GR",
    "GQ",
    "GP",
    "GN",
    "GM",
    "GL",
    "GI",
    "GH",
    "GG",
    "GF",
    "GE",
    "GD",
    "GB",
    "GA",
    "FR",
    "FO",
    "FM",
    "FK",
    "FJ",
    "FI",
    "ET",
    "ES",
    "ER",
    "EH",
    "EG",
    "EE",
    "EC",
    "DZ",
    "DO",
    "DM",
    "DK",
    "DJ",
    "DE",
    "CZ",
    "CY",
    "CX",
    "CW",
    "CV",
    "CU",
    "CR",
    "CO",
    "CN",
    "CM",
    "CL",
    "CK",
    "CI",
    "CH",
    "CG",
    "CF",
    "CD",
    "CC",
    "CA",
    "BZ",
    "BY",
    "BW",
    "BV",
    "BT",
    "BS",
    "BR",
    "BQ",
    "BO",
    "BN",
    "BM",
    "BL",
    "BJ",
    "BI",
    "BH",
    "BG",
    "BF",
    "BE",
    "BD",
    "BB",
    "BA",
    "AZ",
    "AX",
    "AW",
    "AU",
    "AT",
    "AS",
    "AR",
    "AQ",
    "AO",
    "AM",
    "AL",
    "AI",
    "AG",
    "AF",
    "AE",
]


def _valid_ip(ip):
    parts = ip.split(".")
    try:
        return len(parts) == 4 and all(
            0 < len(part) < 4 and 0 <= int(part) < 256 for part in parts
        )
    except ValueError:
        return False


def validate_request(payload):
    if payload and COUNTRY_KEY in payload and IP_KEY in payload:
        country = payload[COUNTRY_KEY]
        if country not in CODES:
            logger.info("Bad request missing country key!")
            return False
        if not _valid_ip(payload[IP_KEY]):
            logger.info("Bad request missing ip key!")
            return False
        return True
    logger.info(
        "Bad request for payload {}".format(str(payload) if payload else "empty")
    )
    return False
