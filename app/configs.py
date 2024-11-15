from dotenv import load_dotenv
import os
basedir = os.path.abspath(__file__)
load_dotenv(os.path.join(basedir, ".env"))

ConStr = os.environ.get("ConStr")
