from typing import List, Dict
from .mergeSort import merge, basic_compare
from .CustomExceptions.KeyUnknownError import KeyUnknownError
import os

DB_NAME_KEY = "DB_NAME"
DB_USER_KEY = "DB_USER"
DB_PASSWORD_KEY = "DB_PASSWORD"

KNOW_KEYS = [DB_NAME_KEY, DB_USER_KEY, DB_PASSWORD_KEY]

ENV_PARAM_SEPARATOR = "\n"
ENV_KEY_VALUE_SEPARATOR = "="

PROJECT_PATH = os.path.abspath(os.path.dirname(__name__))


def read_env_file():
    res = dict()
    with open(PROJECT_PATH + "/.env", "r") as file:
        params = file.read().split(ENV_PARAM_SEPARATOR)  # type: List[str]
        params_dict = dict()  # type: Dict[str, str]
        to_order = list()
        for param in params:
            if not param:
                continue
            tmp = param.split(ENV_KEY_VALUE_SEPARATOR)
            if not tmp[0] in KNOW_KEYS:
                raise KeyUnknownError(tmp[0], "The given key is unknown and cannot be processed")
            params_dict[tmp[0]] = tmp[1] if len(tmp) > 1 else ""
            to_order.append(tmp[0])
        ordered_keys = merge(to_order, basic_compare)
        for key in ordered_keys:
            res[key] = params_dict[key]
    return res


def write_env_file(params: Dict):
    with open(PROJECT_PATH + "/.env", "w") as file:
        for key, value in params.items():
            file.write("=".join([key, value]) + "\n")


__ordered_params = dict()
try:
    __ordered_params = read_env_file()
    write_env_file(__ordered_params)
except FileNotFoundError as e:
    print(e)
except PermissionError as e:
    print(e)
except KeyUnknownError as e:
    print("Message: %s" % e.message)
    print("Key: %s" % e.key)
except Exception as e:
    print(e)

ENVIRONMENT_PARAMS = __ordered_params
DB_NAME = ENVIRONMENT_PARAMS[DB_NAME_KEY]
DB_USER = ENVIRONMENT_PARAMS[DB_USER_KEY]
DB_PASSWORD = ENVIRONMENT_PARAMS[DB_PASSWORD_KEY]
