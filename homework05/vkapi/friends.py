import dataclasses
import math
import time
import typing as tp
import json
import requests
import networkx
from tqdm import tqdm
from vkapi import config, session
from vkapi.exceptions import APIError
import matplotlib.pyplot as plt
QueryParams = tp.Optional[tp.Dict[str, tp.Union[str, int]]]


@dataclasses.dataclass(frozen=True)
class FriendsResponse:
    count: int
    items: tp.Union[tp.List[int], tp.List[tp.Dict[str, tp.Any]]]


def get_friends(
        user_id: int, count: int = 5000, offset: int = 0, fields: tp.Optional[tp.List[str]] = None
) -> FriendsResponse:
    """
    Получить список идентификаторов друзей пользователя или расширенную информацию
    о друзьях пользователя (при использовании параметра fields).

    :param user_id: Идентификатор пользователя, список друзей для которого нужно получить.
    :param count: Количество друзей, которое нужно вернуть.
    :param offset: Смещение, необходимое для выборки определенного подмножества друзей.
    :param fields: Список полей, которые нужно получить для каждого пользователя.
    :return: Список идентификаторов друзей пользователя или список пользователей.
    """
    access_token = config.VK_CONFIG['access_token']
    try:
        req = requests.get('https://api.vk.com/method/friends.get',
                           params={'user_id': user_id, 'order': 'name', 'count': 5000, 'offset': 0,
                                   'fields': 'bdate, nickname', 'access_token': access_token, 'v': 5.131}).json()['response']['items']
    except KeyError:
        return None
    else:
        return req
# print(get_friends(242649276))


class MutualFriends(tp.TypedDict):
    id: int
    common_friends: tp.List[int]
    common_count: int


def get_mutual(
        source_uid: tp.Optional[int] = None,
        target_uid: tp.Optional[int] = None,
        target_uids: tp.Optional[tp.List[int]] = None,
        order: str = "",
        count: tp.Optional[int] = None,
        offset: int = 0,
        progress=None,
) -> tp.Union[tp.List[int], tp.List[MutualFriends]]:
    """
    Получить список идентификаторов общих друзей между парой пользователей.

    :param source_uid: Идентификатор пользователя, чьи друзья пересекаются с друзьями пользователя с идентификатором target_uid.
    :param target_uid: Идентификатор пользователя, с которым необходимо искать общих друзей.
    :param target_uids: Cписок идентификаторов пользователей, с которыми необходимо искать общих друзей.
    :param order: Порядок, в котором нужно вернуть список общих друзей.
    :param count: Количество общих друзей, которое нужно вернуть.
    :param offset: Смещение, необходимое для выборки определенного подмножества общих друзей.
    :param progress: Callback для отображения прогресса.
    """
    access_token = config.VK_CONFIG['access_token']
    r = requests.get('https://api.vk.com/method/friends.getMutual',
                     params={'source_uid': source_uid, 'target_uid': target_uid, 'target_uids': target_uids,
                             'order': 'name', 'offset': 0, 'access_token': access_token, 'v': 5.131}).json()
    h = r['response']
    # f = get_friends(source_uid)
    # g = []
    # for i in range(len(f)):
    #     for j in range(len(r)):
    #         if f[i]['id'] == r[j]:
    #             g.append(f[i]['first_name'] + ' ' + f[i]['last_name'] + ',')
    return h
# print(get_mutual(242649276, 52104206))

def get_friends_id(friends):
    a = []
    if friends != None:
        for x in friends:
            a.append(x['id'])
        return a
