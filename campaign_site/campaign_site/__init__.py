# these 2 lines are for error django.core.exceptions.ImproperlyConfigured when running project

import pymysql

pymysql.install_as_MySQLdb()
