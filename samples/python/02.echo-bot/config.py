#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """
os.environ["MicrosoftAIServiceEndpoint"] = "https://t6languageserviceproject.cognitiveservices.azure.com/" 
os.environ["MicrosoftAPIKey"] = "<Key_from_AI_language_Project_in_Azure_Website>"

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    APP_TYPE = os.environ.get("MicrosoftAppType", "MultiTenant")
    APP_TENANTID = os.environ.get("MicrosoftAppTenantId", "")
    #To Support interaction with Azure AI Language API
    ENDPOINT_URI = os.environ.get("MicrosoftAIServiceEndpoint","")
    print(f"ENDPOINT_URI = {ENDPOINT_URI}")
    API_KEY = os.environ.get("MicrosoftAPIKey", "")
