import pytest
from unittest import mock
import sys
import io
from printm.more import *


@pytest.fixture(scope="function", autouse=False)
def more_init():
    more = More(
        output="hello world",
    )
    yield more
    
def test_init():
    More(
        output="hello world",
    )

def test_init_stdin_error():
    with mock.patch(
        "sys.stdin.isatty",
        return_value=False,
    ):
        with pytest.raises(
            MoreIOError
        ) as raiseinfo:
            More(
                output="Hello World"
            )

def test_init_stdout_error():
    with mock.patch(
        "sys.stdout.isatty",
        return_value=False
    ):
        with pytest.raises(
            MoreIOError
        ) as raiseinfo:
            More(
                output="Hello World"
            )

def test_flush(more_init):
    more_init._flush_screen()

def test_terminal_size(more_init):
    result = more_init._terminal_size()
    assert isinstance(result, tuple)
    assert len(result) == 2

def test_terminal_full_size(more_init):
    result = more_init._terminal_full_size()
    assert isinstance(result, int)

@pytest.mark.parametrize(
    "placeholder",[
    True,
    "placeholder",
    1,
    1.0,
    b"placeholder"
])
def test_placeholder_type_error(more_init, placeholder):
    with pytest.raises(
        TypeError
    ):
        more_init.placeholder = placeholder
        
