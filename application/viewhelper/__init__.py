from application.viewhelper.date_helper import datetime_format
from application.viewhelper.string_helper import filter_supress_none


def my_filter(app):
    app.jinja_env.filters['datetime_format'] = datetime_format
    app.jinja_env.filters['filter_supress_none'] = filter_supress_none
