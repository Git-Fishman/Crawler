from gevent import monkey; monkey.patch_all()
from gevent.pool import Pool
from concurrent.futures import ThreadPoolExecutor


def threads(task_name, pool_size, *args, **kwargs):

    pool = ThreadPoolExecutor(pool_size)
    outcome_iter = pool.map(task_name, args, kwargs)
    pool.shutdown()

    result_list = []
    for result in outcome_iter:
        result_list.append(result)

    return result_list


def coroutines(task_name, param_list, pool_size):

    pool = Pool(pool_size)

    result_list = pool.map(task_name, param_list)

    return result_list


def multi_task(task_name, param_list, pool_size, mode='coroutines'):

    if mode == 'threads':
        result_list = threads(task_name, param_list, pool_size)

    else:
        result_list = coroutines(task_name,  param_list, pool_size)

    return result_list

