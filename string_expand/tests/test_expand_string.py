# tests
import pytest

from string_expand.expand_string import expand_string


def test_basic_expansion():
    assert expand_string("2[rt]") == "rtrt"
    assert expand_string("q4[t]") == "qtttt"
    assert expand_string("r2[r3[t]w]r3[rt]q") == "rrtttwrtttwrrtrtrtq"


def test_empty_case():
    assert expand_string("") == ""


def test_number_without_brackets():
    assert expand_string("a2b") == "a2b"


def test_nested_case():
    assert expand_string("3[a2[b]]") == "abbabbabb"


def test_zero_multiplier():
    assert expand_string("a0[b]c") == "ac"


def test_invalid_input_opening_bracket_without_number():
    with pytest.raises(ValueError) as exc_info:
        expand_string("a[b]")
    assert str(exc_info.value) == "Opening bracket '[' without preceding number"


def test_invalid_input_unmatched_closing_bracket():
    with pytest.raises(ValueError) as exc_info:
        expand_string("a]b")
    assert str(exc_info.value) == "Unmatched closing bracket ']'"


def test_invalid_input_unmatched_opening_bracket():
    with pytest.raises(ValueError) as exc_info:
        expand_string("2[a")
    assert str(exc_info.value) == "Unmatched opening bracket '['"


def test_multiple_consecutive_brackets():
    assert expand_string("2[ab]3[cd]") == "ababcdcdcd"
    assert expand_string("2[ab]3[cd]4[ef]") == "ababcdcdcdefefefef"


def test_brackets_with_no_content():
    assert expand_string("2[]") == ""
    assert expand_string("a2[]b") == "ab"


def test_only_brackets():
    with pytest.raises(ValueError) as exc_info:
        expand_string("[abc]")
    assert str(exc_info.value) == "Opening bracket '[' without preceding number"


def test_only_numbers():
    assert expand_string("123") == "123"


def test_special_characters():
    assert expand_string("2[a!@]") == "a!@a!@"
    assert expand_string("2[ a ]") == " a  a "


def test_long_input():
    long_input = "1000[a]"
    expected_output = "a" * 1000
    assert expand_string(long_input) == expected_output
