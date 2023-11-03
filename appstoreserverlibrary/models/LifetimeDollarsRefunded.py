# Copyright (c) 2023 Apple Inc. Licensed under MIT License.

from enum import Enum

from .LibraryUtility import AppStoreServerLibraryEnumMeta

class LifetimeDollarsRefunded(Enum, metaclass=AppStoreServerLibraryEnumMeta):
    """
    A value that indicates the dollar amount of refunds the customer has received in your app, since purchasing the app, across all platforms.
    
    https://developer.apple.com/documentation/appstoreserverapi/lifetimedollarsrefunded
    """
    UNDECLARED = 0
    ZERO_DOLLARS = 1
    ONE_CENT_TO_FORTY_NINE_DOLLARS_AND_NINETY_NINE_CENTS = 2
    FIFTY_DOLLARS_TO_NINETY_NINE_DOLLARS_AND_NINETY_NINE_CENTS = 3
    ONE_HUNDRED_DOLLARS_TO_FOUR_HUNDRED_NINETY_NINE_DOLLARS_AND_NINETY_NINE_CENTS = 4
    FIVE_HUNDRED_DOLLARS_TO_NINE_HUNDRED_NINETY_NINE_DOLLARS_AND_NINETY_NINE_CENTS = 5
    ONE_THOUSAND_DOLLARS_TO_ONE_THOUSAND_NINE_HUNDRED_NINETY_NINE_DOLLARS_AND_NINETY_NINE_CENTS = 6
    TWO_THOUSAND_DOLLARS_OR_GREATER = 7
