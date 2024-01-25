import os

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6926818113:AAGvY8BgAxXJCQA68U90pQ0Tn9WkoU7dQ9o")
API_ID = int(os.environ.get("API_ID", "20145727"))
PASS_DB = int(os.environ.get("PASS_DB", "721"))
FR_TOKEN = os.environ.get("FR_TOKEN", "f0907b55-922e-414a-8d21-47c1887bb90d")
API_KEY = os.environ.get("API_KEY", "d9bb45ffcd4b965c515a714f2680f4a7")
API_HASH = os.environ.get("API_HASH", "d9bb45ffcd4b965c515a714f2680f4a7")
ADMINS = int(os.environ.get("ADMINS", "5454197638"))
LOG = [int(chat) for chat in os.getenv("LOG", "2032609744").split(",") if chat != ""]
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
