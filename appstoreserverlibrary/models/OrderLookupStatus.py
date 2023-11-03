# Copyright (c) 2023 Apple Inc. Licensed under MIT License.

from enum import Enum

from .LibraryUtility import AppStoreServerLibraryEnumMeta

class OrderLookupStatus(Enum, metaclass=AppStoreServerLibraryEnumMeta):
    """
    A value that indicates whether the order ID in the request is valid for your app.
    
    https://developer.apple.com/documentation/appstoreserverapi/orderlookupstatus
    """
    VALID = 0
    INVALID = 1
