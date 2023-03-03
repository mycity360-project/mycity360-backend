from pathlib import Path


EMAIL_VERIFICATION_REQUIRED = "email_verification_required"
PHONE_VERIFICATION_REQUIRED = "phone_verification_required"
FROM_EMAIL = ""
# CREDENTIALS_FILE_PATH="/Users/t2bdev/Downloads/Heena/projects/mycity360-backend/backend/backend/credentials/credentials.json"
CREDENTIALS_FILE_PATH = f"{Path.cwd()}/backend/credentials/credentials.json"
# TOKEN_FILE_PATH="/Users/t2bdev/Downloads/Heena/projects/mycity360-backend/backend/backend/credentials/token.json"
TOKEN_FILE_PATH = f"{Path.cwd()}/backend/credentials/token.json"
