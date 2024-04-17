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
    SESSION = os.environ.get("SESSION", "1BVtsOHIBuw0hGHsaIxnHYPPzkohTMxsfXYRdSZ8MwynnDq12-Itd15tEaIMuY-Ug02dH12RoMWCIv39xfliUac1i5qG7CItc46EdrddODlHTVLXH-NekkR-eUFv54P9M0ZxJs9oSXlaj-e3HU8JSEf6Ck5OU25338Niyobuq7-AEllCWaMSfFM3ESJOGw5PTPjJ0-uNRFuzZc_ObmWmFrXJyTYWecFPrPeZ5psBYnTMl9CPJOVgbMzLPi_hql0rciYRawzT7b0-47_Nm_xgVtlT_utiGWgxBfb0BsGggD2SsTMi1BVZGY3VK-ZEPlOHxn31IfIcVPzqY6_WtddcC7aWisOAF684=")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1002140519614"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "coffeebyte_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
