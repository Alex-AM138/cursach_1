import requests, datetime, json, logging, os, csv, re, collections
import pandas as pd
from pathlib import Path
from typing import Any
from dotenv import load_dotenv
from urllib import request


load_dotenv(".env")

CURRENCY_RATE_API_KEY = os.getenv("CURRENCY_RATE_API_KEY")
STOCK_PRICES_API_KEY = os.getenv("STOCK_PRICES_API_KEY")
