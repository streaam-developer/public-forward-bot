import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "24010108"))
    API_HASH = os.environ.get("API_HASH", "8d89700b2fc09a3aa6c906cbed65b040")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7034883166:AAEy2SExdx2HMQAohgKZjsbTLcEQvuU25fY")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "6924888856")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://lajihi2115:lgAEiuZHs917nZgy@cluster0.lx88eg8.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "xcbzvcb")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1002140519614"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "coffeebyte_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
