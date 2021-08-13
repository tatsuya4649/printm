import pytest
from printm import printm

def test_doc():
    result = printm.__doc__
    assert isinstance(result, str)
    print(f"document: \n{result}")

@pytest.mark.parametrize(
    "no_placeholder",[
    False,
    True,
])
def test_print_no_placeholder(no_placeholder):
    printm(
        output="output",
        placeholder="placeholder",
        before_blanks=1,
        after_blanks=0,
        no_placeholder=no_placeholder,
    )

@pytest.mark.parametrize(
    "placeholder",[
    None,
    "placeholder"
])
def test_print_placeholder(placeholder):
    printm(
        output="output",
        placeholder=placeholder,
        before_blanks=1,
        after_blanks=0,
        no_placeholder=False,
    )

@pytest.mark.parametrize(
    "before_blanks",[
    0,
    10,
])
def test_print_before_blanks(before_blanks):
    printm(
        output="output",
        placeholder="placeholder",
        before_blanks=before_blanks,
        after_blanks=0,
        no_placeholder=False,
    )

@pytest.mark.parametrize(
    "after_blanks",[
    0,
    10,
])
def test_print_after_blanks(after_blanks):
    printm(
        output="output",
        placeholder="placeholder",
        before_blanks=0,
        after_blanks=after_blanks,
        no_placeholder=False,
    )
