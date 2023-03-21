# -*- coding: utf-8 -*-
"""
Oauth Task
"""
# python imports
from __future__ import unicode_literals
from contextlib import suppress
from datetime import timedelta
from typing import Optional

# lib imports
from django.utils import timezone
from oauth2_provider.models import AccessToken, Application, RefreshToken
from oauthlib import common


def generate_access_token(user_id, client_id=None, expires_in=None):
    """
    Takes user_id and create its access token and refresh token.

    Args:
        user_id (int): user id for which token is generated
        client_id (str): client id
        expires_in (integer): expiration time in seconds

    Return:
        access_token instance

    Raise:
        None
    """
    application = None
    with suppress(Application.DoesNotExist):
        application = Application.objects.get(client_id=client_id)
    # if not application:
    #     raise InvalidParameter(messages.CLIENT_NOT_REGISTER)
    expires_in = (
        expires_in
        if expires_in is not None
        else 86400
        # else constants.ACCESS_TOKEN_EXPIRE_SECONDS
    )
    expires = timezone.now() + timedelta(seconds=expires_in)
    access_token = AccessToken(
        user_id=user_id,
        scope="",
        expires=expires,
        token=common.generate_token(),
        application=application,
    )
    access_token.save()
    refresh_token = RefreshToken(
        user_id=user_id,
        token=common.generate_token(),
        application=application,
        access_token=access_token,
    )
    refresh_token.save()
    return access_token


def get_token_json(access_token):
    """
    Takes an AccessToken instance as an argument
    and returns a object from that
    AccessToken
    """
    token = {
        "access_token": access_token.token,
        # "expires_in": constants.ACCESS_TOKEN_EXPIRE_SECONDS,
        "expires_in": 86400,
        "token_type": "Bearer",
        "refresh_token": access_token.refresh_token.token,
        "scope": access_token.scope,
        "user_id": access_token.user_id,
    }
    return token


def revoke_token(token: Optional[str]):
    """
    Revoke an access token.

    Args:
        user_id: User Id
        token: The token string.

    Return:
        bool true
    """
    try:
        AccessToken.objects.get(token=token).revoke()
    except AccessToken.DoesNotExist:
        pass
    return True
