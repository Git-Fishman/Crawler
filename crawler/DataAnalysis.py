import logging, re
from lxml import etree

logging.basicConfig(level=20, filename='param.txt')


def re_and_fix_analysis(text, text_name=None):
    while True:

        re_pattern = input('\n正在进行正则匹配，请输入正则表达式：')
        try:
            data_raw = re.findall(re_pattern, text)
        except Exception as e:
            print('表达式错误，请重试\n')
            continue

        print(f'\n元素列表:{data_raw}\n元素个数{len(data_raw)}个\n')

        choose = input('以上是返回的结果，是否正确？1.是，保存并退出   2.否，继续匹配   3、是，但需要进行数据处理   4.退出\n请输入：')
        if choose == '1':
            logging.info(f'{text_name}的正则表达式是：{re_pattern}')
            break
        elif choose == '2':
            continue
        elif choose == '3':
            data_fix_analysis(data_raw, text_name, 're', pattern=re_pattern)
        elif choose == '4':
            break
        else:
            print('\n非法操作')
            continue

        break


def xpath_and_fix_analysis(text, text_name):
    text = etree.HTML(text)

    while True:

        xpath_pattern = input('\n正在进行xpath匹配，请输入xpath表达式：')

        try:
            data_raw = text.xpath(xpath_pattern)
        except Exception as e:
            print('表达式错误，请重试\n')
            continue

        print(f'\n元素列表:{data_raw}\n元素个数{len(data_raw)}个\n')

        choose = input(
            '以上是返回的结果，是否正确？1.是，保存并退出   2.否，继续匹配   3、是，但需要进行数据处理   4.退出\n请输入：')
        if choose == '1':
            logging.info(f'{text_name}的xpath表达式是：{xpath_pattern}')
            break
        elif choose == '2':
            continue
        elif choose == '3':
            data_fix_analysis(data_raw, text_name, 'xpath', pattern=xpath_pattern)
        elif choose == '4':
            break
        else:
            print('\n非法操作')
            continue

        break


def data_fix_analysis(data_raw, text_name, mode, pattern):
    while True:
        print(f'\n正在进行二次数据处理\n\n参考结果：{data_raw[0]}\n')
        prefix = input('请输入元素前缀:')
        suffix = input('请输入元素后缀:')
        data = prefix + data_raw[0] + suffix
        print(f'\n元素:{data}\n')
        choose = input(f'以上是数据二次处理结果，是否正确？1.是，退出并保存   2.否，继续处理   3.退出\n请输入：')
        if choose == '1':
            logging.info(f'{text_name}的{mode}表达式是：{pattern},前缀是：{prefix},后缀是：{suffix}')
            break
        elif choose == '2':
            continue
        elif choose == '3':
            break
        else:
            print('非法操作')
            continue


def data_analysis(text, text_name=None):
    while True:
        print(text, '\n')
        confirm = input('是否为目标内容？1.是   2.否\n请输入：')

        if confirm == '1':
            mode = input('请选择分析模式：1.re分析   2.xpath分析\n请输入：')

            if mode == '1':
                print(text)
                print('{:*^100}'.format('以上是文本内容'))
                re_and_fix_analysis(text, text_name)
            else:
                print(text)
                print('{:*^100}'.format('以上是文本内容'))
                xpath_and_fix_analysis(text, text_name)
            break

        else:
            break

