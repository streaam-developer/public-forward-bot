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
    SESSION = os.environ.get("SESSION", "BQGjERMABOMRjYWA1Do9p5tRKvKPxDTQCt10DXtaFto78n3B5pvk_nJGGJ_Q-ih8xXwG8KroA8NMp30l4XZV1rdHRVSaHiC7N-1Mol7t-D2Pyu6TxKeiqKG3ozkL-_XpdDjScKr0DTaZQ1Hnpn9rMG3Vst8ii-x69zF8uVqgRJ2cTe8h7USDLsi0oxFr84WnXfnHp4FYZ2dLzfcWU-7I2gvHZhjGIyGEKQF0BCNV6xz5DiA2E2aR6l7bUmdmpizlXvnPxvxcadGWKUGPzi4pRhk7E8kWLuychBKAg9GNHYlo3qJwd_i1SyCPJtvHYeRzS0MYIHa-FoZbG9HneCbj_UBBDwrwpAAAAAGQM_vWAA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1002140519614"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "coffeebyte_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
