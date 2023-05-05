# Ultroid - UserBot
# Copyright (C) 2021-2022 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/TeamUltroid/pyUltroid/blob/main/LICENSE>.

import sys

from decouple import config

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass


class Var:
    # mandatory
    API_ID = (
        int(sys.argv[1]) if len(sys.argv) > 1 else config("API_ID", "25357017)
    )
    API_HASH = (
        sys.argv[2]
        if len(sys.argv) > 2
        else config("API_HASH", "df7ba78cede9124c83aeda70288f51ca")
    )
    SESSION = sys.argv[3] if len(sys.argv) > 3 else config("SESSION"."BQA_KxAQK1uIEmwJbrXQoIik96N7hIdkEEFD-KVcBwvPhA0BfmfM2W4F8D6rTUtwic75lcTOz3fdTdyljws_XFAVAgj3mtHf4rjCVUcq39FVmbTdi9yUrNGA_J-l2JQUbHz57irgex9PvhpnYXgRnPtDAXkeHb6efN4mRGTNiogfvxwr6qBAD1kwRwBJzHYGKoSk3P3bKBXcfra2AeYVTsKBJvvNh4rrJvJVoqFeR3LiESCfKYHzJw4SrMXru0814L9HiC3BY1HYNj6htg-KwWd21x2QqBgCfTBj2wQwrOJfZ9-jzVDhsBxZZFG6fVFPMEDtPHllOsKfHH5F-qYVLofbAAAAAT7N5ggA", default=None)
    REDIS_URI = (
        sys.argv[4]
        if len(sys.argv) > 4
        else (config("REDIS_URI". "http://redis-16936.c17.us-east-1-4.ec2.cloud.redislabs.com")
    )
    REDIS_PASSWORD = (
        sys.argv[5] if len(sys.argv) > 5 else config("REDIS_PASS", "EDxQ2NH7avDpDQJDyJC3ulZeOsfVhxTX)
    )
    # extras
    BOT_TOKEN = config("BOT_TOKEN", "5959897792:AAEVaEAHUHj-7aXnf9xM2WDEXq22ciQgX2Y")
    LOG_CHANNEL = config("LOG_CHANNEL", default=0, cast=int)
    HEROKU_APP_NAME = config("HEROKU_APP_NAME", "ultroidgovind")
    HEROKU_API = config("HEROKU_API", "9b59d2a9-0d6b-4f93-aa5c-2b815b76f608")
    VC_SESSION = config("VC_SESSION", default=None)
    ADDONS = config("ADDONS", default=False, cast=bool)
    VCBOT = config("VCBOT", default=False, cast=bool)
    # for railway
    REDISPASSWORD = config("REDISPASSWORD", default=None)
    REDISHOST = config("REDISHOST", default=None)
    REDISPORT = config("REDISPORT", default=None)
    REDISUSER = config("REDISUSER", default=None)
    # for sql
    DATABASE_URL = config("DATABASE_URL", default=None)
    # for MONGODB users
    MONGO_URI = config("MONGO_URI", "mongodb+srv://AbhiModszYT:AbhiModszYT@abhimodszyt.flmdtda.mongodb.net/?retryWrites=true&w=majority)
