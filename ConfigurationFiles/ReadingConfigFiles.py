from configparser import ConfigParser

parser=ConfigParser()
parser.read('EnvironmentDeatails.cnf')
print(parser.get('Dev_DB_DETAILS','serverName'))