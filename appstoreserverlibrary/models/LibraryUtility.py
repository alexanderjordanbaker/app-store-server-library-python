# Copyright (c) 2023 Apple Inc. Licensed under MIT License.

from enum import EnumMeta
from typing import Any, List

from attr import Attribute, ib, fields

metadata_key = 'correspondingFieldName'
metadata_type_key = 'typeOfField'

class AppStoreServerLibraryEnumMeta(EnumMeta):
    def __contains__(c, val):
        try:
            c(val)
        except ValueError:
            return False
        return True  
    
    def create_main_attr(c, raw_field_name: str) -> Any:
        def value_set(self, _: Attribute, value: c):
            newValue = value.value if value is not None else None
            if newValue != getattr(self, raw_field_name):
                object.__setattr__(self, raw_field_name, newValue)
            return value
        return ib(default=None, on_setattr=value_set, metadata={metadata_key: raw_field_name, metadata_type_key: 'main'})
    
    def create_raw_attr(c, field_name: str) -> Any:
        def value_set(self, _: Attribute, value: str):
            newValue = c(value) if value in c else None
            if newValue != getattr(self, field_name):
                object.__setattr__(self, field_name, newValue)
            return value
        return ib(default=None, kw_only=True, on_setattr=value_set, metadata={metadata_key: field_name, metadata_type_key: 'raw'})
    
class AttrsRawValueAware:
    def __attrs_post_init__(self):
        attr_fields: List[Attribute] = fields(type(self))
        for attribute in attr_fields:
            if metadata_type_key not in attribute.metadata or attribute.metadata[metadata_type_key] != 'raw':
                continue
            field: str = attribute.metadata.get(metadata_key)
            rawField = 'raw' + field[0].upper() + field[1:]
            rawValue = getattr(self, rawField)
            value = getattr(self, field)
            if rawValue is not None:
                setattr(self, rawField, rawValue)
            elif value is not None:
                setattr(self, field, value)