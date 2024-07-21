#!/usr/bin/env python3
"""
index_range
takes two integer arguments
page and page_size
"""
from typing import Tuple



def index_range(page: int, page_size: int) -> Tuple:
    """
    index_range
    takes two integer arguments
    page and page_size
    """
    if page == 1:
        return (0, page_size)
    else:
        return ((page - 1) * page_size , page * page_size)
