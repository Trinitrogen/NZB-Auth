from flask import Flask

app = Flask(__name__)

from nzb_auth import routes