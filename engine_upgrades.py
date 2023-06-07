"""A script to get compatible engine upgrades for BMW 330i X-Drive
"""

from typing import List

def engine_upgrades(bmw_specs: dict, budget: str, criteria: str) -> List:
    if budget == 'low':
        if criteria == 'performance':
            return ['A', 'B', 'C']
        elif criteria == 'affordability':
            return ['D', 'E', 'F']
        elif criteria == 'balanced':
            return ['G', 'H', 'I']
    elif budget == 'mid':
        if criteria == 'performance':
            return ['J', 'K', 'L']
        elif criteria == 'affordability':
            return ['M', 'N', 'O']
        elif criteria == 'balanced':
            return ['P', 'Q', 'R']
    elif budget == 'high':
        if criteria == 'performance':
            return ['S', 'T', 'U']
        elif criteria == 'affordability':
            return ['V', 'W', 'X']
        elif criteria == 'balanced':
            return ['Y', 'Z']