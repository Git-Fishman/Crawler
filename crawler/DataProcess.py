# -*- coding: UTF-8 -*-
import re
from lxml import etree


def data_process(data, mode, pattern, future, prefix, suffix):

    if mode == 're':
        data_raw = get_data_by_re(data, pattern, future)
        data = get_data_with_fixed(data_raw, prefix, suffix)

    else:
        data_raw = get_data_by_xpath(data, pattern, future)
        data = get_data_with_fixed(data_raw, prefix, suffix)

    return data


def get_data_by_xpath(data, xpath_pattern, result_type):
    if result_type == 'str':
        data = etree.HTML(data)
        data = data.xpath(xpath_pattern)
        data = str(data[0])
        return data
    else:
        data_raw = etree.HTML(data)
        data_raw = data_raw.xpath(xpath_pattern)
        data_list = []
        for i in range(len(data_raw)):
            data = str(data_raw[i])
            data_list.append(data)
        return data_list


def get_data_by_re(text, re_pattern, result_type):
    if result_type == 'str':
        data = re.findall(re_pattern, text)
        data = data[0]
        return data
    else:
        data = re.findall(re_pattern, text)
        return data


def get_data_with_fixed(data, prefix, suffix):
    if isinstance(data, str):
        data = prefix + data + suffix
    else:
        data_list = []
        for data_son in data:
            data_dad = prefix + data_son + suffix
            data_list.append(data_dad)
        return data_list
    return data
