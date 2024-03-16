#!/usr/bin/env/bash
python manage.py db upgrade
flask run --host=0.0.0.0

RUN chmod u+x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
