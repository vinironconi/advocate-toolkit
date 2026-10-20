import pytest
from toolkit import pv_remaining, search_products, calculate_pv, calculate_total, to_guaranis

LAVENDER = {"name": "Lavender", "size": "15ml", "category": "Single-Oil", "regular": 197, "membros": 148, "pv": 23}
PRODUCTS = [LAVENDER]

def test_pv_remaining():
    assert pv_remaining(90) == 10
    assert pv_remaining(100) == 0
    assert pv_remaining(120) == 0
    assert pv_remaining(50) == 50
    assert pv_remaining(50, goal=125) == 75

def test_search_products():
    assert search_products(PRODUCTS, "lavender") == [LAVENDER]
    assert search_products(PRODUCTS, "lav") == [LAVENDER]
    assert search_products(PRODUCTS, "LAV") == [LAVENDER]
    assert search_products(PRODUCTS, "") == []
    assert search_products(PRODUCTS, "   ") == []

def test_calculate_pv():
    assert calculate_pv([]) == 0
    assert calculate_pv([(LAVENDER, 2)]) == 46
    assert calculate_pv([(LAVENDER, 1)]) == 23

def test_calculate_total():
    assert calculate_total([]) == 0
    assert calculate_total([(LAVENDER, 2)]) == 296
    assert calculate_total([(LAVENDER, 1)]) == 148
    assert calculate_total([(LAVENDER, 2)], price_type="regular") == 394

def test_to_guaranis():
    assert to_guaranis(100) == 130000
    assert to_guaranis(296, exchange_rate=1300) == 385000

