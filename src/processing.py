from typing import Dict, List


def filter_by_state(tested_list: List[Dict], value_: str = 'EXECUTED') -> List[Dict]:
    """Фунция сбора списка со статусом 'EXECUTED' """
    executed_list = []
    for dict_ in tested_list:
        if dict_['state'] == 'EXECUTED':
            executed_list.append(dict_)
    return executed_list


def sort_by_date(tested_list: List[Dict], sort_: bool = True) -> List[Dict]:
    """Функция сортировки словарей в списке по убыванию даты"""
    sorted_list_by_date = sorted(tested_list, key=lambda x: x.get('date'), reverse=sort_)
    return sorted_list_by_date
