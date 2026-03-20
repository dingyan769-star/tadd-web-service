from app.service import mask_profanity

def test_no_profanity():
    assert mask_profanity("hello world") == "hello world"

def test_single_profanity():
    assert mask_profanity("you are stupid") == "you are ******"

def test_multiple_profanity():
    assert mask_profanity("stupid idiot") == "****** *****"

def test_case_insensitive():
    assert mask_profanity("Stupid") == "******"

def test_empty_string():
    assert mask_profanity("") == ""