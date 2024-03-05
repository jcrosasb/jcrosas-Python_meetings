from typing import Dict

def merge_dictionaries(dict_1: Dict, dict_2: Dict) -> Dict:
    return {**dict_1, **dict_2}


def merge_dictionaries_2(dict_1: Dict, dict_2: Dict) -> Dict:
    merged = dict(dict_1)
    merged.update(dict_2)
    return merged


dict_1 = {'a': 1, 'b': 2}
dict_2 = {'c': 3, 'd': 4}


print(merge_dictionaries(dict_1, dict_2))
print(merge_dictionaries_2(dict_1, dict_2))