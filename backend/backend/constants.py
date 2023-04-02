from pathlib import Path


EMAIL_VERIFICATION_REQUIRED = "email_verification_required"
PHONE_VERIFICATION_REQUIRED = "phone_verification_required"
FROM_EMAIL = ""
# CREDENTIALS_FILE_PATH="/Users/t2bdev/Downloads/Heena/projects/mycity360-backend/backend/backend/credentials/credentials.json"
CREDENTIALS_FILE_PATH = f"{Path.cwd()}/backend/credentials/credentials.json"
# TOKEN_FILE_PATH="/Users/t2bdev/Downloads/Heena/projects/mycity360-backend/backend/backend/credentials/token.json"
TOKEN_FILE_PATH = f"{Path.cwd()}/backend/credentials/token.json"

ADMIN_ROLE = "Admin"
USER_ROLE = "User"

# Messages
CLIENT_ID_REQUIRED = "Client id is required"
EMAIL_OR_PHONE_REQUIRED = "Email or Phone is required"
AREA_REQUIRED = "Area required"
EMAIL_USER_EXIST = "User already exist with email"
PHONE_USER_EXIST = "User already exist with phone"
OTP_REQUIRED = "Email OTP or Phone OTP required"
PASSWORD_REQUIRED = "Password is required"
EMAIL_OTP_EXPIRED = "Email OTP Expired"
PHONE_OTP_EXPIRED = "Phone OTP Expired"
PASSWORD_VERIFICATION_FAILED = "Password verification failed"

EMAIL_SUBJECT = "MyCity360 Email Verification"
EMAIL_BODY = "Hi {} \n This is your OTP for email verification. \n {} \n Regards\nMyCity360 Team"

AREA_DOES_NOT_EXIST = "Area with this id does not exist"
CATEGORY_DOES_NOT_EXIST = "Category with this id does not exist"
IMAGE_DOES_NOT_EXIST = "Image with this id does not exist"
LOCATION_DOES_NOT_EXIST = "Location with this id does not exist"
SAVED_AD_DOES_NOT_EXIST = "SavedAd with this id does not exist"
SERVICE_DOES_NOT_EXIST = "Service with this id does not exist"
STATE_DOES_NOT_EXIST = "State with this id does not exist"
SYSTEM_CONFIG_DOES_NOT_EXIST = "System Config with this id does not exist"
USER_DOES_NOT_EXIST = "User does not exist"
