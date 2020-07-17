# uvicorn run_api_post:app --reload --port 8000 --host 0.0.0.0 --access-log --limit-concurrency 100
from fastapi import FastAPI
from custom_logging import CustomizeLogger
from pathlib import Path
from pydantic import BaseModel
from fastapi import Request
from fastapi import logger as api_logger
import uvicorn
import logging
import traceback

logger = logging.getLogger(__name__)

config_path = Path(__file__).with_name("logging_config.json")

def create_app() -> FastAPI:
    app = FastAPI(title='CustomLogger', debug=False)
    print(config_path)
    logger = CustomizeLogger.make_logger(config_path)
    app.logger = logger
    return app


app = create_app()
class Data(BaseModel):
    id: str

@app.post('/custom-logger')
def customize_logger(data: Data, request: Request):
    logger = request.app.logger
    if not isinstance(data, dict):
        data = data.dict()
    print(data)
    logger.info(data["id"])
    try:
        a = 1 / 0
    except:
        logger.error(traceback.format_exc())
    logger.info("Here Is Your Error Log")
    return {'data': "Successfully Implemented Custom Log"}

os.system("python init.py")