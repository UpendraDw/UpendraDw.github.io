# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

class BaseConfig(object):

    # Can be set to 'MasterUser' or 'ServicePrincipal'
    AUTHENTICATION_MODE = 'ServicePrincipal'

    # Workspace Id in which the report is present
    WORKSPACE_ID = '77d7a63e-1c33-45c9-8b79-7dc105409b66'
    
    # Report Id for which Embed token needs to be generated
    REPORT_ID = '8ad574c9-edc0-4879-b83a-0bb0d4322f83'
    
    # Id of the Azure tenant in which AAD app and Power BI report is hosted. Required only for ServicePrincipal authentication mode.
    TENANT_ID = 'ec8b63c9-4b2e-42df-8c37-429d44d0be66'
    
    # Client Id (Application Id) of the AAD app
    CLIENT_ID = 'aef69a68-7bfb-4970-8bea-5a14b5d8da88'
    
    # Client Secret (App Secret) of the AAD app. Required only for ServicePrincipal authentication mode.
    CLIENT_SECRET = '7228Q~R0itpz6-XQGNagi966dCqwzHOi6INjCayz'
    
    # Scope Base of AAD app. Use the below configuration to use all the permissions provided in the AAD app through Azure portal.
    SCOPE_BASE = ['https://analysis.windows.net/powerbi/api/.default']
    
    # URL used for initiating authorization request
    AUTHORITY_URL = 'https://login.microsoftonline.com/organizations'
    
    # Master user email address. Required only for MasterUser authentication mode.
    POWER_BI_USER = 'upendradwivedi01@upendradwivedidegmail.onmicrosoft.com'
    
    # Master user email password. Required only for MasterUser authentication mode.
    POWER_BI_PASS = 'Nithelec@2019'