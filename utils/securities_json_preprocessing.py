from utils.parse_securities import parse_securities


def securities_preprocessing(url: str) -> list:
    securities_data = []
    securities = parse_securities(url)['securities']['data']
    for security in securities:
        data = {
            'id': str(security[0]),
            'secid': security[1],
            'regnumber': security[3],
            'name': security[4],
            'emitent_title': security[8]
        }
        securities_data.append(data)
    return securities_data
