# import pytest
# from cases_utils import dict_without_key
# from cases_utils import dict_with_new_key
# from cases_utils import dict_with_edited_value
#
# dict = {
#     "one": 1,
#     "two": "smth",
#     "three": True,
#     "five": {
#         "one": {
#             "two": 2,
#             "test": 3
#         }
#     }
# }
#
# TEST_SETUP = {
#     "delete": [
#         # pytest.param(
#         #     dict_without_key(dict, "text"),
#         #     None,
#         #     id='1'
#         # ),
#         pytest.param(
#             dict_without_key(dict, "five"),
#             {
#                 "one": 1,
#                 "two": "smth",
#                 "three": True
#             },
#             id='2'
#         ),
#         pytest.param(
#             dict_without_key(dict, "five.one"),
#             {
#                 "one": 1,
#                 "two": "smth",
#                 "three": True,
#                 "five": {}
#             },
#             id='3'
#         ),
#         pytest.param(
#             dict_without_key(dict, "five.two"),
#             None,
#             id='4'
#         ),
#         pytest.param(
#             dict_without_key(dict, "five.one.two"),
#             {
#                 "one": 1,
#                 "two": "smth",
#                 "three": True,
#                 "five": {
#                     "one": {
#                         "test": 3
#                     }
#                 }
#             },
#             id='5'
#         ),
#         pytest.param(
#             dict_without_key(dict, ""),
#             None,
#             id='6'
#         ),
#         pytest.param(
#             dict_without_key({}, "text"),
#             None,
#             id='7'
#         ),
#         pytest.param(
#             dict_without_key({}, "five"),
#             None,
#             id='8'
#         ),
#         pytest.param(
#             dict_without_key({}, "five.one"),
#             None,
#             id='9'
#         ),
#         pytest.param(
#             dict_without_key({}, "five.two"),
#             None,
#             id='10'
#         ),
#         pytest.param(
#             dict_without_key({}, "five.one.two"),
#             None,
#             id='11'
#         ),
#         pytest.param(
#             dict_without_key({}, ""),
#             None,
#             id='12'
#         ),
#
#     ],
#     "change": [
#         pytest.param(
#             dict_with_edited_value(dict, "text", "new"),
#             None,
#             id='13'
#         ),
#         pytest.param(
#             dict_with_edited_value(dict, "five", "new"),
#             {
#                 "one": 1,
#                 "two": "smth",
#                 "three": True,
#                 "five": "new"
#             },
#             id='14'
#         ),
#         pytest.param(
#             dict_with_edited_value(dict, "five.one", "new"),
#             {
#                 "one": 1,
#                 "two": "smth",
#                 "three": True,
#                 "five": {
#                     "one": "new"
#                 }
#             },
#             id='15'
#         ),
#         pytest.param(
#             dict_with_edited_value(dict, "five.two", "new"),
#             None,
#             id='16'
#         ),
#         pytest.param(
#             dict_with_edited_value(dict, "five.one.two", "new"),
#             {
#                 "one": 1,
#                 "two": "smth",
#                 "three": True,
#                 "five": {
#                     "one": {
#                         "two": "new",
#                         "test": 3
#                     }
#                 }
#             },
#             id='17'
#         ),
#         pytest.param(
#             dict_with_edited_value(dict, "", "new"),
#             None,
#             id='18'
#         ),
#         pytest.param(
#             dict_with_edited_value({}, "text", "new"),
#             None,
#             id='19'
#         ),
#         pytest.param(
#             dict_with_edited_value({}, "five", "new"),
#             None,
#             id='20'
#         ),
#         pytest.param(
#             dict_with_edited_value({}, "five.one", "new"),
#             None,
#             id='21'
#         ),
#         pytest.param(
#             dict_with_edited_value({}, "five.two", "new"),
#             None,
#             id='22'
#         ),
#         pytest.param(
#             dict_with_edited_value({}, "five.one.two", "new"),
#             None,
#             id='23'
#         ),
#         pytest.param(
#             dict_with_edited_value({}, "", "new"),
#             None,
#             id='24'
#         )
#     ],
#     "add": [
#         pytest.param(
#             dict_with_new_key(dict, "text", "new"),
#             {
#                 "one": 1,
#                 "two": "smth",
#                 "three": True,
#                 "five": {
#                     "one": {
#                         "two": 2,
#                         "test": 3
#                     }
#                 },
#                 "text": "new"
#             },
#             id='25'
#         ),
#         pytest.param(
#             dict_with_new_key(dict, "five", "new"),
#             None,
#             id='26'
#         ),
#         pytest.param(
#             dict_with_new_key(dict, "one", "new"),
#             None,
#             id='27'
#         ),
#         pytest.param(
#             dict_with_new_key(dict, "five.one", "new"),
#             None,
#             id='28'
#         ),
#         pytest.param(
#             dict_with_new_key(dict, "five.two", "new"),
#             {
#                 "one": 1,
#                 "two": "smth",
#                 "three": True,
#                 "five": {
#                     "one": {
#                         "two": 2,
#                         "test": 3
#                     },
#                     "two": "new"
#                 }
#             },
#             id='29'
#         ),
#         pytest.param(
#             dict_with_new_key(dict, "five.one.two", "new"),
#             None,
#             id='30'
#         ),
#         pytest.param(
#             dict_with_new_key(dict, "", "new"),
#             {
#                 "one": 1,
#                 "two": "smth",
#                 "three": True,
#                 "five": {
#                     "one": {
#                         "two": 2,
#                         "test": 3
#                     }
#                 },
#                 "": "new"
#             },
#             id='31'
#         ),
#         pytest.param(
#             dict_with_new_key({}, "text", "new"),
#             {
#                 "text": "new"
#             },
#             id='32'
#         ),
#         pytest.param(
#             dict_with_new_key({}, "five", "new"),
#             {
#                 "five": "new"
#             },
#             id='33'
#         ),
#         pytest.param(
#             dict_with_new_key({}, "five.one", "new"),
#             None,
#             id='34'
#         ),
#         pytest.param(
#             dict_with_new_key({}, "five.two", "new"),
#             None,
#             id='35'
#         ),
#         pytest.param(
#             dict_with_new_key({}, "five.one.two", "new"),
#             None,
#             id='36'
#         ),
#         pytest.param(
#             dict_with_new_key({}, "", "new"),
#             {
#                 "": "new"
#             },
#             id='37'
#         )
#     ]
#
# }
#
#
# @pytest.mark.parametrize("result, mock", TEST_SETUP["delete"])
# def test_utils_delete(result, mock):
#     assert result == mock
#
#
# @pytest.mark.parametrize("result, mock", TEST_SETUP["change"])
# def test_utils_change(result, mock):
#     assert result == mock
#
#
# @pytest.mark.parametrize("result, mock", TEST_SETUP["add"])
# def test_utils_add(result, mock):
#     assert result == mock
