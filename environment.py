from dotenv import load_dotenv
import os

load_dotenv()

supabase_secret = os.environ.get("SUPABASE_JWT_SECRET")
