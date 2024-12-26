import uuid
from utils.parse_history import parse_history


def history_preprocessing(url: str) -> list:
    history_data = []
    histories = parse_history(url)['history']['data']
    for history in histories:
        data = {
            'id': str(uuid.uuid4()),
            'secid': history[3],
            'numtrades': history[4],
            'tradedate': history[1],
            'open': history[6],
            'close': history[11]
        }
        history_data.append(data)
    return history_data
