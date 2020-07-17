# uvicorn run_api_get:app --reload --port 8000 --host 0.0.0.0 --access-log --limit-concurrency 100
from fastapi import FastAPI
from custom_logging import CustomizeLogger
from pathlib import Path
from fastapi import Request
import uvicorn
import logging

logger = logging.getLogger(__name__)

config_path = Path(__file__).with_name("logging_config.json")

def create_app() -> FastAPI:
    app = FastAPI(title='CustomLogger', debug=False)
    print(config_path)
    logger = CustomizeLogger.make_logger(config_path)
    app.logger = logger
    return app


app = create_app()

@app.get('/custom-logger')
def customize_logger(request: Request):
    request.app.logger.info("Here Is Your Info Log")
    a = 1 / 0
    request.app.logger.error("Here Is Your Error Log")
    return {'data': "Successfully Implemented Custom Log"}

# import requests
# url = "http://ip:8000/custom-logger"
# r = requests.get(url)