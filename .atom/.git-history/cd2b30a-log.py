import datetime
from flask import request, session, escape
from app import app
import os


def set_logging(warning, error, debug):
    '''
    Sets handlers for Flass logger to file names based on parameters passed in.
    Creates the directory structure for the application.

    :param warning: the file name of warning output, e.g. warning.csv
    :type warning: string
    :param error: the file name of error output, e.g. error.csv
    :type error: string
    :param debug: the file name of debug output, e.g. debug.csv
    :type debug: string
    '''
    if not app.debug:
        import logging
        from logging import FileHandler

        now = datetime.datetime.now()

        if not os.path.exists("../log/"):
            os.mkdir("../log/")
        if not os.path.exists("../log/" + str(now.year)):
            os.mkdir("../log/" + str(now.year))
        if not os.path.exists("../log/" + str(now.year) + "/" +
                              now.strftime("%B")):
            os.mkdir("../log/" + str(now.year) + "/" + now.strftime("%B"))
        if not os.path.exists("../log/" + str(now.year) + "/" +
                              now.strftime("%B") + "/" + str(now.day)):
            os.mkdir("../log/" + str(now.year) + "/" +
                     now.strftime("%B") + "/" + str(now.day))

        file_handler = FileHandler("../log/" + str(now.year) + "/" +
                                   now.strftime("%B") + "/" +
                                   str(now.day) + "/" + warning)
        file_handler.setLevel(logging.WARNING)
        app.logger.addHandler(file_handler)

        file_handler = FileHandler("../log/" + str(now.year) + "/" +
                                   now.strftime("%B") + "/" +
                                   str(now.day) + "/" + error)
        file_handler.setLevel(logging.ERROR)
        app.logger.addHandler(file_handler)

        file_handler = FileHandler("../log/" + str(now.year) + "/" +
                                   now.strftime("%B") + "/" +
                                   str(now.day) + "/" + debug)
        file_handler.setLevel(logging.DEBUG)
        app.logger.addHandler(file_handler)


def log_request():
    app.logger.debug(log_msg(''))


def log_error(msg):
    app.logger.debug(log_msg(msg))
    app.logger.error(log_msg(msg))


def log_msg(msg):
    try:
        user = escape(session['user'])
    except KeyError:
        user = 'None'
    log = str(datetime.datetime.now()) + ", " + request.remote_addr + ", " + \
        str(user) + ", " + request.path + ", " + request.method
    if msg:
        log = log + ", " + msg
    return log
