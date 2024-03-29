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
GUEST_ROLE = "Guest"

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
PASSWORD_CHANGED = "Password changed successfully"
OTP_SENT = "OTP sent successfully"
USER_VERIFIED = "User Already Verified"

EMAIL_SUBJECT = "MyCity360 Email Verification"
PHONE_SUBJECT = "MyCity360 Phone Verification"
EMAIL_BODY = "Hi {} \nThis is your OTP for email verification. \n{} \nRegards\nMyCity360 Team"
PHONE_BODY = "Hi {} \nThis is your OTP for phone verification. \n{} \nRegards\nMyCity360 Team"

FORGOT_PASSWORD_SUBJECT = "MyCity360 Password Change"
FORGOT_PASSWORD_BODY = "Hi {} \nThis is your OTP for changing password. \n{} \nRegards\nMyCity360 Team"

AREA_DOES_NOT_EXIST = "Area with this id does not exist"
CATEGORY_DOES_NOT_EXIST = "Category with this id does not exist"
IMAGE_DOES_NOT_EXIST = "Image with this id does not exist"
LOCATION_DOES_NOT_EXIST = "Location with this id does not exist"
SAVED_AD_DOES_NOT_EXIST = "SavedAd with this id does not exist"
SERVICE_DOES_NOT_EXIST = "Service with this id does not exist"
STATE_DOES_NOT_EXIST = "State with this id does not exist"
SYSTEM_CONFIG_DOES_NOT_EXIST = "System Config with this id does not exist"
USER_DOES_NOT_EXIST = "User does not exist"
QUESTION_DOES_NOT_EXIST = "Question does not exist"
ANSWER_DOES_NOT_EXIST = "Answer does not exist"
BANNER_DOES_NOT_EXIST = "Banner does not exist"
NEW_PASSWORD_IS_SAME = "New password can not be the same as old password"
FILE_REQUIRED = "File is required"

CACHE_URL = "redis://127.0.0.1:6379/1"

MEDIA_ROOT = "/var/www/media/"
# MEDIA_ROOT = settings.BASE_DIR
SERVER_BASE_URL = "http://mycity360.in/media/"
CACHE_VALIDITY = 10800

OTP_EXPIRE_MINUTES = 2

SUPPORT_EMAILS = (
    "heena4415@gmail.com, vibh1103@gmail.com, anuragchachan97@gmail.com"
)
DELETE_EMAIL_BODY = "Hi \nThe following user wants to delete their account \n Name: {} \n Phone: {} \n Email: {} \nRegards\nMyCity360 Team"
DELETE_EMAIL_SUBJECT = "MyCity360 Delete Account"
USER_ID_REQUIRED = "User id is required"
USER_BLOCKED = "User blocked successfully"
