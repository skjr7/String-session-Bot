import os

ENVIRONMENT = os.environ.get('ENVIRONMENT', False)

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 0))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', None)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
    DATABASE_URL = os.environ.get('DATABASE_URL', None)
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")  # Sqlalchemy dropped support for "postgres" name.
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
    MUST_JOIN = os.environ.get('MUST_JOIN', None)
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "")
else:
    # Fill the Values
    API_ID = 6439635
    API_HASH = "cff5ae354fffc28e97739586d10c70a7"
    BOT_TOKEN = "5461950370:AAG28HoafqcIM7z4oGiDHdQJ3nvptt0Aj-U"
    DATABASE_URL = "mongodb+srv://suryaakumar:suryaa737@cluster0.ltkky.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
    MUST_JOIN = "@Friendstamilchatting"
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN[1:]
