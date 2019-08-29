from typing import NewType


s3_service_name_type = NewType('s3_service_name', str)
s3_service_name: s3_service_name_type = s3_service_name_type('s3')

config_service_name_type = NewType('config_service_name', str)
config_service_name: config_service_name_type = config_service_name_type('config')
