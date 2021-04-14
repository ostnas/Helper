import pytest
from cases_utils import dict_without_key
from cases_utils import add_key_to_dict
from cases_utils import change_value_by_key

dict = {
    "one": 1,
    "two": "smth",
    "three": True,
    "five": {
        "one": {
            "two": 2,
            "test": 3
        }
    }
}

TEST_SETUP = {
    "delete": [
        (
            dict_without_key(dict, "text"),
            None
        ),
        (
            dict_without_key(dict, "five"),
            {
                "one": 1,
                "two": "smth",
                "three": True
            }
        ),
        (
            dict_without_key(dict, "five.one"),
            {
                "one": 1,
                "two": "smth",
                "three": True,
                "five": {}
            }
        ),
        (
            dict_without_key(dict, "five.two"),
            None
        ),
        (
            dict_without_key(dict, "five.one.two"),
            {
                "one": 1,
                "two": "smth",
                "three": True,
                "five": {
                    "one": {
                        "test": 3
                    }
                }
            }
        ),
        (
            dict_without_key(dict, ""),
            None
        ),
        (
            dict_without_key({}, "text"),
            None
        ),
        (
            dict_without_key({}, "five"),
            None
        ),
        (
            dict_without_key({}, "five.one"),
            None
        ),
        (
            dict_without_key({}, "five.two"),
            None
        ),
        (
            dict_without_key({}, "five.one.two"),
            None
        ),
        (
            dict_without_key({}, ""),
            None
        ),

    ],
    "change": [
        (
            change_value_by_key(dict, "text", "new"),
            None
        ),
        (
            change_value_by_key(dict, "five", "new"),
            {
                "one": 1,
                "two": "smth",
                "three": True,
                "five": "new"
            }
        ),
        (
            change_value_by_key(dict, "five.one", "new"),
            {
                "one": 1,
                "two": "smth",
                "three": True,
                "five": {
                    "one": "new"
                }
            }
        ),
        (
            change_value_by_key(dict, "five.two", "new"),
            None
        ),
        (
            change_value_by_key(dict, "five.one.two", "new"),
            {
                "one": 1,
                "two": "smth",
                "three": True,
                "five": {
                    "one": {
                        "two": "new",
                        "test": 3
                    }
                }
            }
        ),
        (
            change_value_by_key(dict, "", "new"),
            None
        ),
        (
            change_value_by_key({}, "text", "new"),
            None
        ),
        (
            change_value_by_key({}, "five", "new"),
            None
        ),
        (
            change_value_by_key({}, "five.one", "new"),
            None
        ),
        (
            change_value_by_key({}, "five.two", "new"),
            None
        ),
        (
            change_value_by_key({}, "five.one.two", "new"),
            None
        ),
        (
            change_value_by_key({}, "", "new"),
            None
        )
    ],
    "add": [
        (
            add_key_to_dict(dict, "text", "new"),
            {
                "one": 1,
                "two": "smth",
                "three": True,
                "five": {
                    "one": {
                        "two": 2,
                        "test": 3
                    }
                },
                "text": "new"
            }
        ),
        (
            add_key_to_dict(dict, "five", "new"),
            None
        ),
        (
            add_key_to_dict(dict, "five.one", "new"),
            None
        ),
        (
            add_key_to_dict(dict, "five.two", "new"),
            {
                "one": 1,
                "two": "smth",
                "three": True,
                "five": {
                    "one": {
                        "two": 2,
                        "test": 3
                    },
                    "two": "new"
                }
            }
        ),
        (
            add_key_to_dict(dict, "five.one.two", "new"),
            None
        ),
        (
            add_key_to_dict(dict, "", "new"),
            {
                "one": 1,
                "two": "smth",
                "three": True,
                "five": {
                    "one": {
                        "two": 2,
                        "test": 3
                    }
                },
                "": "new"
            }
        ),
        (
            add_key_to_dict({}, "text", "new"),
            {
                "text": "new"
            }
        ),
        (
            add_key_to_dict({}, "five", "new"),
            {
                "five": "new"
            }
        ),
        (
            add_key_to_dict({}, "five.one", "new"),
            None
        ),
        (
            add_key_to_dict({}, "five.two", "new"),
            None
        ),
        (
            add_key_to_dict({}, "five.one.two", "new"),
            None
        ),
        (
            add_key_to_dict({}, "", "new"),
            {
                "": "new"
            }
        )
    ]

}


@pytest.mark.parametrize("result, mock", TEST_SETUP["delete"]+TEST_SETUP["change"]+TEST_SETUP["add"])
def test_utils(result, mock):
    assert result == mock
