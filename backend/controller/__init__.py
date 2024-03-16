from controller.home import home
from controller.login import login_blueprint
from controller.booking import booking_blueprint
from controller.user import user_blueprint
from controller.bookable import bookable_blueprint

blueprints = [
    home,
    login_blueprint,
    booking_blueprint,
    user_blueprint,
    bookable_blueprint,
]
