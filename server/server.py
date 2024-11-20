import os
from dotenv import load_dotenv
from api import config, create_app

load_dotenv()

app = create_app(config.Config)
app.run(port=os.getenv('PORT', 5000))