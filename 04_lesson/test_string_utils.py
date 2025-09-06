import pytest


from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.positive_test
@pytest.mark.parametrize("string, new_string", [("Good morning", "Good morning"), ("good day", "Good day"),])
def test_positive_capitalize(string, new_string):
    result = string_utils.capitalize(string[0]) + string[1:]
    assert result == new_string


@pytest.mark.negative_test
@pytest.mark.parametrize("string, new_string", [("65 days", "65 days"), ("", ""), ("  ", "  "),])
def test_negative_capitalize(string, new_string):
    result = string_utils.capitalize(string)
    assert result == new_string


@pytest.mark.positive_test
@pytest.mark.parametrize("string, new_string", [("   Hello", "Hello"), ("  159", "159"),])
def test_positive_trim(string, new_string):
    result = string_utils.trim(string)
    assert result == new_string


@pytest.mark.negative_test
@pytest.mark.parametrize("string, new_string", [("Hello", "Hello"), ("  ", ""), ("", ""),])
def test_negative_trim(string, new_string):
    result = string_utils.trim(string)
    assert result == new_string


@pytest.mark.positive_test
@pytest.mark.parametrize("string, symbol, boolean", [("Hello", "l", True), ("Python 3.13.7", "3", True), ("  ", " ", True), ("", "", True),])
def test_positive_contains(string, symbol, boolean):
    result = string_utils.contains(string, symbol)
    assert result == boolean


@pytest.mark.negative_test
@pytest.mark.parametrize("string, symbol, boolean", [("Hello", "d", False), ("", "4", False), ("   ", "Rk", False),])
def test_negative_contains(string, symbol, boolean):
    result = string_utils.contains(string, symbol)
    assert result == boolean


@pytest.mark.positive_test
@pytest.mark.parametrize("string, symbol, new_string", [("Hello", "l", "Heo"), ("Pyt  hon", " ", "Python"), ("Python 3.13.7", "3", "Python .1.7"),])
def test_positive_delete_symbol(string, symbol, new_string):
    result = string_utils.delete_symbol(string, symbol)
    assert result == new_string


@pytest.mark.negative_test
@pytest.mark.parametrize("string, symbol, new_string", [("Hello", "I", "Hello"), ("", "", ""),])
def test_negative_delete_symbol(string, symbol, new_string):
    result = string_utils.delete_symbol(string, symbol)
    assert result == new_string
