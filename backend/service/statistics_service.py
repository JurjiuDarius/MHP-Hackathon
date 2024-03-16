from ai_component.ai_interactive_logic import ai_controller
from utils.date import mdy_to_dmy


def get_office_occupation(data):
    date = data["date"]
    date = mdy_to_dmy(date)

    ai = ai_controller()
    result = ai.get_presence_prediction(date)
    result = int(result)
    return result, 200
