import os
from app import create_app
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create app instance
app = create_app(os.getenv('FLASK_ENV', 'development'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
