import pytest
from unittest import mock
from printm.placeholder import *

@pytest.fixture(scope="function", autouse=False)
def p_init():
    place = PlaceHolder(
        placeholder="Hello World",
        before_blanks=1,
        after_blanks=1,
    )
    yield place
    
def test_init():
    place = PlaceHolder(
        placeholder="Hello World",
        before_blanks=1,
        after_blanks=1,
    ) 
@pytest.mark.parametrize(
    "placeholder",[
    10,
    10.0,
    b"placeholder",
    ["placeholder"],
    {"placeholder": "hello world"},
    True,
])
def test_init_placeholder_type_error(placeholder):
    with pytest.raises(
        TypeError
    ):
        place = PlaceHolder(
            placeholder=placeholder,
            before_blanks=1,
            after_blanks=1,
        )

@pytest.mark.parametrize(
    "before_blanks",[
    "10",
    10.0,
    b"placeholder",
    [10],
    {"before_blanks": 10},
])
def test_init_before_blanks_type_error(before_blanks):
    with pytest.raises(
        TypeError
    ):
        place = PlaceHolder(
            placeholder="placeholder",
            before_blanks=before_blanks,
            after_blanks=1,
        )

@pytest.mark.parametrize(
    "after_blanks",[
    "10",
    10.0,
    b"placeholder",
    [10],
    {"after_blanks": 10},
])
def test_init_after_blanks_type_error(after_blanks):
    with pytest.raises(
        TypeError
    ):
        place = PlaceHolder(
            placeholder="placeholder",
            before_blanks=1,
            after_blanks=after_blanks,
        )

def test_placelines(p_init):
    result = p_init.placelines(
        lines=100,
    )
    assert isinstance(result, int)

@pytest.mark.parametrize(
    "lines",[
    "100",
    b"100",
    [100],
    {"lines": 100},
])
def test_placelines(p_init, lines):
    with pytest.raises(
        TypeError
    ):
        result = p_init.above_placelines(
            lines=lines,
        )

def test_before_blank(p_init):
    result = p_init.before_blank
    assert isinstance(result, str)

def test_after_blank(p_init):
    result = p_init.after_blank
    assert isinstance(result, str)
