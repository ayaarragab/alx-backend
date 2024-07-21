#!/usr/bin/env python3
"""
index_range
takes two integer arguments
page and page_size
"""
import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple:
    """
    index_range
    takes two integer arguments
    page and page_size
    """
    if page == 1:
        return (0, page_size)
    else:
        return ((page - 1) * page_size, page * page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        akes two integer arguments page with default
        value 1 and page_size with default value 10
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        dataset_list = self.dataset()
        ranges = index_range(page, page_size)
        n_rows = len(dataset_list)
        if ranges[0] > n_rows - 1 or ranges[1] > n_rows - 1:
            return []
        l_elements = []
        for i in range(ranges[0], ranges[1]):
            l_elements.append(dataset_list[i])
        return l_elements

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        takes the same arguments (and defaults) as get_page and returns a
        dictionary containing the following key-value pairs:
        page_size: the length of the returned dataset page
        return dict of
        @param page
        @param data
        @param next_page
        @param prev_page
        @param total_pages
        """
        actual_data = self.get_page(page, page_size)
        all_data_len = len(self.dataset())
        return {'page_size': len(actual_data),
                'page': page, 'data': actual_data,
                'next_page': page + 1 if page + 1 < all_data_len else None,
                'prev_page': page - 1 if page + 1 > 0 else None,
                'total_pages': all_data_len}
