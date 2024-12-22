from typing import Dict, List


def filter_by_state(tested_list: List[Dict], value_: str = 'EXECUTED') -> List[Dict]:
    """Фунция принимающая на входе список словарей, и выдает спиосок словарей со статусом 'EXECUTED' """
    executed_list = []
    for dict_of_list in tested_list:
        if dict_of_list['state'] == 'EXECUTED':
            executed_list.append(dict_of_list)
    return executed_list


def sort_by_date(tested_list: List[Dict], `revers_date_list`: bool = True) -> List[Dict]:
    """Функция сортировки словарей в списке по убыванию даты"""
    sorted_list_by_date = sorted(tested_list, key=lambda x: x.get('date'), reverse=revers_date_list)
    return sorted_list_by_date


