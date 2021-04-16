import pytest


URL = '/travel-passes/social'
CHECK_RESULT = 'etc/responses/travel_passes/add_travel_pass/check_result/social'
POSITIVE_RESPONSE_PATH = 'etc/responses/travel_passes/add_travel_pass'
NEGATIVE_RESPONSE_PATH = 'etc/responses/errors/travel_passes/add_travel_pass/social'
JSON_PARSING_ERROR = 'etc/responses/errors/common/parsing_error.json'


TEST_SETUP = {
    "negative": [
        pytest.param(
            # category: кириллица
            {
                 "category": "06.Б5",
                 "operatorId": 6,
                 "description": "Описание",
                 "blocked": False,
                 "algorithm": 4,
                 "sellFeeSum": 12345,
                 "minPayment": 12345,
                 "maxPayment": 12345,
                 "saleCost": 12345,
                 "thresholdCounter": 12345,
                 "maxCounter": 12345,
                 "shortDescription": "Описание описание",
                 "longDescription": "Описание 123",
                 "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/category_cyrillic.json',
            id='category_cyrillic'
          ),
        pytest.param(
            # category: латиница
            {
                 "category": "F3.05",
                 "operatorId": 6,
                 "description": "Описание",
                 "blocked": False,
                 "algorithm": 4,
                 "sellFeeSum": 12345,
                 "minPayment": 12345,
                 "maxPayment": 12345,
                 "saleCost": 12345,
                 "thresholdCounter": 12345,
                 "maxCounter": 12345,
                 "shortDescription": "Описание описание",
                 "longDescription": "Описание 123",
                 "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/category_latin.json',
            id='category_latin'
          ),
        pytest.param(
            # category: длина категории больше 2-х символов
            {
                 "category": "123.05",
                 "operatorId": 6,
                 "description": "Описание",
                 "blocked": False,
                 "algorithm": 4,
                 "sellFeeSum": 12345,
                 "minPayment": 12345,
                 "maxPayment": 12345,
                 "saleCost": 12345,
                 "thresholdCounter": 12345,
                 "maxCounter": 12345,
                 "shortDescription": "Описание описание",
                 "longDescription": "Описание 123",
                 "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/category_category_over_max_value.json',
            id='category_category_over_max_value'
          ),
        pytest.param(
            # category: длина подкатегории больше 2-х символов
            {
                "category": "06.155",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/category_subcategory_over_max_value.json',
            id='category_subcategory_over_max_value'
        ),
        pytest.param(
            # category: пустая строка
            {
                 "category": "",
                 "operatorId": 6,
                 "description": "Описание",
                 "blocked": False,
                 "algorithm": 4,
                 "sellFeeSum": 12345,
                 "minPayment": 12345,
                 "maxPayment": 12345,
                 "saleCost": 12345,
                 "thresholdCounter": 12345,
                 "maxCounter": 12345,
                 "shortDescription": "Описание описание",
                 "longDescription": "Описание 123",
                 "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/category_empty_string.json',
            id='category_empty_string'
          ),
        pytest.param(
            # category: пробел
            {
                "category": " ",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/category_space.json',
            id='category_space'
        ),
        pytest.param(
            # category: None
            {
                "category": None,
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/category_null.json',
            id='category_unsent_mandatory_param'
        ),
        pytest.param(
            # category: неполностью заполненная категория
            {
                "category": "0.02",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/category_not_a_complete_category.json',
            id='category_not_a_complete_category'
          ),
        pytest.param(
            # category: неполностью заполненная подкатегория
            {
                "category": "06.2",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/category_not_a_complete_subcategory.json',
            id='category_not_a_complete_subcategory'
        ),
        pytest.param(
            # создание проездного с уже существующей категорией
            {
                 "category": "06.99",
                 "operatorId": 6,
                 "description": "Описание",
                 "blocked": False,
                 "algorithm": 4,
                 "sellFeeSum": 12345,
                 "minPayment": 12345,
                 "maxPayment": 12345,
                 "saleCost": 12345,
                 "thresholdCounter": 12345,
                 "maxCounter": 12345,
                 "shortDescription": "Описание описание",
                 "longDescription": "Описание 123",
                 "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/category_exists.json',
            id='category_exists'
         ),
        pytest.param(
            # operatorId: передан несуществующий оператор
            {
                "category": "06.10",
                "operatorId": 134,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/operatorId_nonexistent_operator.json',
            id='operatorId_nonexistent_operator'
        ),
        pytest.param(
            # operatorId: кириллица
            {
                "category": "06.10",
                "operatorId": "абв",
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            JSON_PARSING_ERROR,
            id='operatorId_cyrillic'
        ),
        pytest.param(
            # operatorId: латиница
            {
                "category": "06.10",
                "operatorId": "abc",
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            JSON_PARSING_ERROR,
            id='operatorId_latin'
        ),
        pytest.param(
            # operatorId: спецсимволы
            {
                "category": "06.10",
                "operatorId": "!@#",
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            JSON_PARSING_ERROR,
            id='operatorId_special_symbol'
        ),
        pytest.param(
            # operatorId: пустая строка
            {
                "category": "06.10",
                "operatorId": "",
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/operatorId_null.json',
            id='operatorId_empty_string'
        ),
        pytest.param(
            # operatorId: с пробелом
            {
                "category": "06.10",
                "operatorId": " ",
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/operatorId_null.json',
            id='operatorId_space'
        ),
        pytest.param(
            # operatorId: None
            {
                "category": "06.10",
                "operatorId": None,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/operatorId_null.json',
            id='operatorId_unsent_mandatory_param'
        ),
        pytest.param(
            # operatorId: > 16 символов
            {
                "category": "06.10",
                "operatorId": 100000000000000000,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/operatorId_over_max_value.json',
            id='operatorId_over_max_value'
        ),
        pytest.param(
            # description: > 512 символов
            {
                 "category": "06.01",
                 "operatorId": 6,
                 "description": "а"*513,
                 "blocked": False,
                 "algorithm": 4,
                 "sellFeeSum": 12345,
                 "minPayment": 12345,
                 "maxPayment": 12345,
                 "saleCost": 12345,
                 "thresholdCounter": 12345,
                 "maxCounter": 12345,
                 "shortDescription": "Описание описание",
                 "longDescription": "Описание 123",
                 "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/description_over_max_value.json',
            id='description_over_max_value'
          ),
        pytest.param(
            # description: пустая строка
            {
                "category": "06.22",
                "operatorId": 6,
                "description": "",
                "blocked": False,
                "algorithm": 4,
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/description_empty_string.json',
            id='description_empty_string'
        ),
        pytest.param(
            # description: пробел
            {
                "category": "06.01",
                "operatorId": 6,
                "description": " ",
                "blocked": False,
                "algorithm": 4,
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/description_space.json',
            id='description_space'
        ),
        pytest.param(
            # description: None
            {
                "category": "06.22",
                "operatorId": 6,
                "description": None,
                "blocked": False,
                "algorithm": 4,
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/description_null.json',
            id='description_unsent_mandatory_param'
        ),
        pytest.param(
            # blocked: латиница (кроме True/False)
            {
                "category": "06.22",
                "operatorId": 6,
                "description": "Описание",
                "blocked": "abc",
                "algorithm": 4,
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            JSON_PARSING_ERROR,
            id='blocked_latin'
        ),
        pytest.param(
            # blocked: кириллица
            {
                "category": "06.22",
                "operatorId": 6,
                "description": "Описание",
                "blocked": "абв",
                "algorithm": 4,
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            JSON_PARSING_ERROR,
            id='blocked_cyrillic'
        ),
        pytest.param(
            # blocked: спецсимволы
            {
                "category": "06.22",
                "operatorId": 6,
                "description": "Описание",
                "blocked": "!@#",
                "algorithm": 4,
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            JSON_PARSING_ERROR,
            id='blocked_special_symbols'
        ),
        pytest.param(
            # blocked: пробел
            {
                "category": "06.22",
                "operatorId": 6,
                "description": "Описание",
                "blocked": " ",
                "algorithm": 4,
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/blocked_null.json',
            id='blocked_space'
        ),
        pytest.param(
            # blocked: пустая строка
            {
                "category": "06.22",
                "operatorId": 6,
                "description": "Описание",
                "blocked": "",
                "algorithm": 4,
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/blocked_null.json',
            id='blocked_empty_string'
        ),
        pytest.param(
            # blocked: None
            {
                "category": "06.22",
                "operatorId": 6,
                "description": "Описание",
                "blocked": None,
                "algorithm": 4,
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/blocked_null.json',
            id='blocked_unsent_mandatory_param'
        ),
        pytest.param(
            # prepaymentSum: латиница
            {
                "category": "06.22",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "prepaymentSum": "abc",
                "algorithm": 4,
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            JSON_PARSING_ERROR,
            id='prepaymentSum_latin'
        ),
        pytest.param(
            # prepaymentSum: кириллица
            {
                "category": "06.22",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "prepaymentSum": "абв",
                "algorithm": 4,
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            JSON_PARSING_ERROR,
            id='prepaymentSum_cyrillic'
        ),
        pytest.param(
            # prepaymentSum: спецсимволы
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "prepaymentSum": "!@#",
                "algorithm": 4,
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            JSON_PARSING_ERROR,
            id='prepaymentSum_special_symbols'
        ),
        pytest.param(
            # prepaymentSum: > int(64)
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "prepaymentSum": 9223372036854775808,
                "algorithm": 4,
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            JSON_PARSING_ERROR,
            id='prepaymentSum_over_max_value'
        ),
        pytest.param(
            #  prepaymentSum: переданное значение 0
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "prepaymentSum": 0,
                "algorithm": 4,
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/prepaymentSum_zero.json',
            id='prepaymentSum_zero'
        ),
        pytest.param(
            #  prepaymentSum: переданное отрицательное значение
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "prepaymentSum": -1,
                "algorithm": 4,
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/prepaymentSum_negative_value.json',
            id='prepaymentSum_negative_value'
        ),
        pytest.param(
            # algorithm: латиница
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": "abc",
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            JSON_PARSING_ERROR,
            id='algorithm_latin'
        ),
        pytest.param(
            # algorithm: кириллица
            {
                "category": "06.22",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": "абв",
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            JSON_PARSING_ERROR,
            id='algorithm_cyrillic'
        ),
        pytest.param(
            # algorithm: спецсимволы
            {
                "category": "06.22",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": "!@#",
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            JSON_PARSING_ERROR,
            id='algorithm_special_symbols'
        ),
        pytest.param(
            # несуществующий algorithm: 6
            {
                "category": "06.22",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 6,
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/algorithm_nonexistent_algorithm.json',
            id='algorithm_nonexistent_algorithm'
        ),
        pytest.param(
            # algorithm: с пробелом
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": " ",
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/algorithm_null.json',
            id='algorithm_empty_space'
        ),
        pytest.param(
            # algorithm: пустая строка
            {
                "category": "06.22",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": "",
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/algorithm_null.json',
            id='algorithm_empty_string'
        ),
        pytest.param(
            # algorithm: None
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": None,
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/algorithm_null.json',
            id='algorithm_unsent_mandatory_param'
        ),
        pytest.param(
            # algorithm: отрицательное значение
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": -1,
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/algorithm_negative_value.json',
            id='algorithm_negative_value'
        ),
        pytest.param(
            # dateRestriction.period : кириллица
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "dateRestriction": {
                    "period": "абв",
                    "startHours": "09:50",
                    "endHours": "20:50"
                },
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            JSON_PARSING_ERROR,
            id='dateRestriction_period_cyrillic'
        ),
        pytest.param(
            # dateRestriction.period : латиница
            {
                "category": "06.22",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "dateRestriction": {
                    "period": "abc",
                    "startHours": "09:50",
                    "endHours": "20:50"
                },
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            JSON_PARSING_ERROR,
            id='dateRestriction_period_latin'
        ),
        pytest.param(
            # dateRestriction.period : спецсимволы
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "dateRestriction": {
                    "period": "!@#",
                    "startHours": "09:50",
                    "endHours": "20:50"
                },
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            JSON_PARSING_ERROR,
            id='dateRestriction_period_special_symbols'
        ),
        pytest.param(
            #  dateRestriction.period : > int(32)
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "dateRestriction": {
                    "period": 2147483648,
                    "startHours": "09:50",
                    "endHours": "20:50"
                },
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            JSON_PARSING_ERROR,
            id='dateRestriction_period_over_max_value'
        ),
        pytest.param(
            #  dateRestriction.period : несуществующий период
            {
                "category": "06.22",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "dateRestriction": {
                    "period": 8,
                    "startHours": "09:50",
                    "endHours": "20:50"
                },
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_period_nonexistent.json',
            id='dateRestriction_period_nonexistent'
        ),
        pytest.param(
            #  dateRestriction.period : с пробелом
            {
                "category": "06.22",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "dateRestriction": {
                    "period": " ",
                    "startHours": "09:50",
                    "endHours": "20:50"
                },
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_period_null.json',
            id='dateRestriction_period_space'
        ),
        pytest.param(
            #  dateRestriction.period : пустая строка
            {
                "category": "06.22",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "dateRestriction": {
                    "period": "",
                    "startHours": "09:50",
                    "endHours": "20:50"
                },
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_period_null.json',
            id='dateRestriction_period_empty_string'
        ),
        pytest.param(
            #  dateRestriction.period : None
            {
                "category": "06.22",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "dateRestriction": {
                    "period": None,
                    "startHours": "09:50",
                    "endHours": "20:50"
                },
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_period_null.json',
            id='dateRestriction_period_unsent_mandatory_param'
        ),
        pytest.param(
            #  dateRestriction.startHours : кириллица
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "dateRestriction": {
                    "period": 7,
                    "startHours": "абв",
                    "endHours": "20:50"
                },
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_startHours_cyrillic.json',
            id='dateRestriction_startHours_cyrillic'
        ),
        pytest.param(
            #  dateRestriction.startHours : латиница
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "dateRestriction": {
                    "period": 7,
                    "startHours": "abc",
                    "endHours": "20:50"
                },
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_startHours_latin.json',
            id='dateRestriction_startHours_latin'
        ),
        pytest.param(
            #  dateRestriction.startHours : спецсимволы
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "dateRestriction": {
                    "period": 7,
                    "startHours": "!@#",
                    "endHours": "20:50"
                },
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_startHours_special_symbols.json',
            id='dateRestriction_startHours_special_symbols'
        ),
        pytest.param(
            # dateRestriction.startHours : None
            {
                "category": "06.22",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "dateRestriction": {
                    "period": 7,
                    "startHours": None,
                    "endHours": "20:50"
                },
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_startHours_null.json',
            id='dateRestriction_startHours_unsent_mandatory_param'
        ),
        pytest.param(
            #  dateRestriction.startHours : пустая строка
            {
                "category": "06.75",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "dateRestriction": {
                    "period": 7,
                    "startHours": "",
                    "endHours": "20:50"
                },
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_startHours_empty_string.json',
            id='dateRestriction_startHours_empty_string'
        ),
        pytest.param(
            #  dateRestriction.startHours : с пробелом
            {
                "category": "06.74",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "dateRestriction": {
                    "period": 7,
                    "startHours": " ",
                    "endHours": "20:50"
                },
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_startHours_space.json',
            id='dateRestriction_startHours_space'
        ),
        pytest.param(
            #  dateRestriction.endHours : кириллица
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "dateRestriction": {
                    "period": 7,
                    "startHours": "12:50",
                    "endHours": "абв"
                },
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_endHours_cyrillic.json',
            id='endHours_cyrillic'
        ),
        pytest.param(
            #  dateRestriction.endHours : латиница
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "dateRestriction": {
                    "period": 7,
                    "startHours": "12:50",
                    "endHours": "abc"
                },
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_endHours_latin.json',
            id='endHours_latin'
        ),
        pytest.param(
            #  dateRestriction.endHours : спецсимволы
            {
                "category": "06.22",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "dateRestriction": {
                    "period": 7,
                    "startHours": "12:50",
                    "endHours": "!@#"
                },
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_endHours_special_symbols.json',
            id='endHours_special_symbols'
        ),
        pytest.param(
            #  dateRestriction.endHours : None
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "dateRestriction": {
                    "period": 7,
                    "startHours": "12:50",
                    "endHours": None
                },
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_endHours_null.json',
            id='dateRestriction_endHours_unsent_mandatory_param'
        ),
        pytest.param(
            #  dateRestriction.endHours : с пробелом
            {
                "category": "06.78",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "dateRestriction": {
                    "period": 7,
                    "startHours": "12:50",
                    "endHours": " "
                },
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_endHours_space.json',
            id='dateRestriction_endHours_space'
        ),
        pytest.param(
            #  dateRestriction.endHours : пустая строка
            {
                "category": "06.77",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "dateRestriction": {
                    "period": 7,
                    "startHours": "12:50",
                    "endHours": ""
                },
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_endHours_empty_string.json',
            id='dateRestriction_endHours_empty_string'
        ),
        pytest.param(
            #  dateRestriction : значение startHours больше значения endHours
            {
                "category": "06.76",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "dateRestriction": {
                    "period": 7,
                    "startHours": "12:00",
                    "endHours": "11:00",
                },
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_startHours_more_endHours.json',
            id='dateRestriction_startHours_more_endHours'
        ),
        pytest.param(
            #  dateRestriction : передан только period
            {
                "category": "06.69",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "dateRestriction": {
                    "period": 7,
                },
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_only_period.json',
            id='dateRestriction_only_period'
        ),
        pytest.param(
            #  dateRestriction : передан только startHours
            {
                "category": "06.73",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "dateRestriction": {
                    "startHours": "12:00",
                },
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_only_startHours.json',
            id='dateRestriction_only_startHours'
        ),
        pytest.param(
            #  dateRestriction : передан только endHours
            {
                "category": "06.72",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "dateRestriction": {
                    "endHours": "12:00",
                },
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_only_endHours.json',
            id='dateRestriction_only_endHours'
        ),
        pytest.param(
            #  dateRestriction : в параметре startHours указан некорректный формат времени
            {
                "category": "06.22",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "dateRestriction": {
                        "period": 7,
                        "startHours": "130:00",
                        "endHours": "11:00",
                    },
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_startHours_incorrect_time_format.json',
            id='dateRestriction_startHours_incorrect_time_format'
        ),
        pytest.param(
            #  dateRestriction : в параметре endHours указан некорректный формат времени
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "dateRestriction": {
                    "period": 7,
                    "startHours": "10:00",
                    "endHours": "110:00",
                },
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_endHours_incorrect_time_format.json',
            id='dateRestriction_endHours_incorrect_time_format'
        ),
        pytest.param(
            #  dateRestriction : в параметре startHours число минут не кратно 10
            {
                "category": "06.22",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "dateRestriction": {
                    "period": 7,
                    "startHours": "10:13",
                    "endHours": "12:00",
                },
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_startHours_incorrect_format_minutes.json',
            id='dateRestriction_startHours_incorrect_format_minutes'
        ),
        pytest.param(
            #  dateRestriction : в параметре endHours число минут не кратно 10
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "dateRestriction": {
                    "period": 7,
                    "startHours": "10:10",
                    "endHours": "12:13",
                },
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_endHours_incorrect_format_minutes.json',
            id='dateRestriction_endHours_incorrect_format_minutes'
        ),
        pytest.param(
            #  dateRestriction : в параметре startHours передано число, как данные хранятся в БД
            {
                "category": "06.71",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "dateRestriction": {
                    "period": 7,
                    "startHours": "70",
                    "endHours": "12:13",
                },
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_startHours_number.json',
            id='dateRestriction_startHours_number'
        ),
        pytest.param(
            #  dateRestriction : в параметре endHours передано число, как данные хранятся в БД
            {
                "category": "06.22",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "dateRestriction": {
                    "period": 7,
                    "startHours": "10:00",
                    "endHours": "86",
                },
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_endHours_number.json',
            id='dateRestriction_endHours_number'
        ),
        pytest.param(
            #  dateRestriction : отравлен пустой объект
            {
                "category": "06.70",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "dateRestriction": {},
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_empty_object.json',
            id='dateRestriction_empty_object'
        ),
        pytest.param(
            #  transportRestriction : передан несуществующий транспорт
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "transportRestriction": [12],
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/transportRestriction_existent_and_nonexistent_id_transport.json',
            id='transportRestriction_nonexistent_id_transport'
        ),
        pytest.param(
            #  transportRestriction : кириллица
            {
                "category": "06.22",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "transportRestriction": ["абв"],
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            JSON_PARSING_ERROR,
            id='transportRestriction_cyrillic'
        ),
        pytest.param(
            #  transportRestriction : латиница
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "transportRestriction": ["abc"],
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            JSON_PARSING_ERROR,
            id='transportRestriction_latin'
        ),
        pytest.param(
            #  transportRestriction : спецсимволы
            {
                "category": "06.22",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "transportRestriction": ["!@#"],
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            JSON_PARSING_ERROR,
            id='transportRestriction_special_symbols'
        ),
        pytest.param(
            #  transportRestriction : > int(32)
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "transportRestriction": [2147483648],
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            JSON_PARSING_ERROR,
            id='transportRestriction_over_max_value'
        ),
        pytest.param(
            #  transportRestriction : передан существующий и несуществующий транспорт
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "transportRestriction": [1, 12],
                "sellFeeSum": 12345,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/transportRestriction_existent_and_nonexistent_id_transport.json',
            id='transportRestriction_existent_and_nonexistent_id_transport'
        ),
        pytest.param(
            #  sellFeeSum : латиница
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "sellFeeSum": "abc",
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            JSON_PARSING_ERROR,
            id='sellFeeSum_latin'
        ),
        pytest.param(
            #  sellFeeSum : кириллица
            {
                "category": "06.22",
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "sellFeeSum": "абв",
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            JSON_PARSING_ERROR,
            id='sellFeeSum_cyrillic'
        ),
        pytest.param(
            #  sellFeeSum : спецсимволы
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "sellFeeSum": "!@#",
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            JSON_PARSING_ERROR,
            id='sellFeeSum_special_symbols'
        ),
        pytest.param(
            #  sellFeeSum: > 6 символов
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "sellFeeSum": 1234567,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/sellFeeSum_over_max_value.json',
            id='sellFeeSum_over_max_value'
        ),
        pytest.param(
            #  sellFeeSum: отрицательное значение
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "sellFeeSum": -1,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/sellFeeSum_negative_value.json',
            id='sellFeeSum_negative_value'
        ),
        pytest.param(
            #  sellFeeSum: пустая строка
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "sellFeeSum": "",
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/sellFeeSum_null.json',
            id='sellFeeSum_empty_string'
        ),
        pytest.param(
            #  sellFeeSum: пробел
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "sellFeeSum": " ",
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/sellFeeSum_null.json',
            id='sellFeeSum_space'
        ),
        pytest.param(
            #  sellFeeSum: None
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "sellFeeSum": None,
                "minPayment": 12345,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/sellFeeSum_null.json',
            id='sellFeeSum_null'
        ),
        pytest.param(
            #  minPayment: кириллица
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "sellFeeSum": 12345,
                "algorithm": 4,
                "minPayment": "абв",
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            JSON_PARSING_ERROR,
            id='in_minPayment_cyrillic'
        ),
        pytest.param(
            #  minPayment: латиница
            {
                "category": "06.22",
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "sellFeeSum": 12345,
                "minPayment": "abc",
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            JSON_PARSING_ERROR,
            id='minPayment_latin'
        ),
        pytest.param(
            #  minPayment: спецсимволы
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "sellFeeSum": 1234,
                "algorithm": 4,
                "minPayment": "!@#",
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            JSON_PARSING_ERROR,
            id='in_minPayment_special_symbols'
        ),
        pytest.param(
            #  minPayment: > int(64)
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "sellFeeSum": 1234,
                "algorithm": 4,
                "minPayment": 92233720368547758078,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            JSON_PARSING_ERROR,
            id='minPayment_over_max_value'
        ),
        pytest.param(
            # minPayment: пустая строка
            {
                    "category": "06.01",
                    "operatorId": 6,
                    "description": "Описание",
                    "blocked": False,
                    "sellFeeSum": 1234,
                    "algorithm": 4,
                    "minPayment": "",
                    "maxPayment": 12345,
                    "saleCost": 12345,
                    "thresholdCounter": 12345,
                    "maxCounter": 12345,
                    "shortDescription": "Описание описание",
                    "longDescription": "Описание 123",
                    "paymentDescription": "Описание 111"
                },
            f'{NEGATIVE_RESPONSE_PATH}/minPayment_null.json',
            id='minPayment_empty_string'
        ),
        pytest.param(
            # minPayment: с пробелом
            {
                "category": "06.22",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "sellFeeSum": 1234,
                "minPayment": " ",
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/minPayment_null.json',
            id='minPayment_space'
        ),
        pytest.param(
            # minPayment: None
            {
                "category": "06.22",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "minPayment": None,
                "sellFeeSum": 1234,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/minPayment_null.json',
            id='minPayment_unsent_mandatory_param'
        ),
        pytest.param(
            # minPayment: передано отрицательное значение
            {
                "category": "06.22",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "sellFeeSum": 1234,
                "minPayment": -1,
                "maxPayment": 12345,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/minPayment_negative_value.json',
            id='minPayment_negative_value'
        ),
        pytest.param(
            # maxPayment: кириллица
            {
                "category": "06.22",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "minPayment": 1234,
                "sellFeeSum": 1234,
                "maxPayment": "абв",
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            JSON_PARSING_ERROR,
            id='maxPayment_cyrillic'
        ),
        pytest.param(
            # maxPayment: латиница
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "minPayment": 1234,
                "sellFeeSum": 1234,
                "maxPayment": "abc",
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            JSON_PARSING_ERROR,
            id='maxPayment_latin'
        ),
        pytest.param(
            # maxPayment: спецсимволы
            {
                "category": "06.22",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "sellFeeSum": 1234,
                "minPayment": 1234,
                "maxPayment": "!@#",
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            JSON_PARSING_ERROR,
            id='maxPayment_special_symbols'
        ),
        pytest.param(
            #  maxPayment: > int(64)
            {
                "category": "06.22",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "sellFeeSum": 1234,
                "algorithm": 4,
                "minPayment": 1234,
                "maxPayment": 92233720368547758078,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            JSON_PARSING_ERROR,
            id='maxPayment_over_max_value'
        ),
        pytest.param(
            # maxPayment: пустая строка
            {
                "category": "06.22",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "sellFeeSum": 1234,
                "algorithm": 4,
                "minPayment": 1234,
                "maxPayment": "",
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/maxPayment_null.json',
            id='maxPayment_empty_string'
        ),
        pytest.param(
            # maxPayment: пробел
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "sellFeeSum": 1234,
                "minPayment": 1234,
                "maxPayment": " ",
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/maxPayment_null.json',
            id='maxPayment_space'
        ),
        pytest.param(
            # maxPayment: None
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "minPayment": 1234,
                "sellFeeSum": 1234,
                "maxPayment": None,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/maxPayment_null.json',
            id='maxPayment_unsent_mandatory_param'
        ),
        pytest.param(
            #  maxPayment: переданное отрицательное значение
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "minPayment": 1234,
                "sellFeeSum": 1234,
                "maxPayment": -1,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/maxPayment_negative_value.json',
            id='maxPayment_negative_value'
        ),
        pytest.param(
            #  maxPayment: передан 0
            {
                "category": "04.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "minPayment": 1234,
                "sellFeeSum": 1234,
                "maxPayment": 0,
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/maxPayment_zero.json',
            id='maxPayment_zero'
        ),
        pytest.param(
            #  saleCost: кириллица
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "minPayment": 1234,
                "sellFeeSum": 1234,
                "maxPayment": 1234,
                "saleCost": "абв",
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            JSON_PARSING_ERROR,
            id='saleCost_cyrillic'
        ),
        pytest.param(
            #  saleCost: латиница
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "sellFeeSum": 1234,
                "minPayment": 1234,
                "maxPayment": 1234,
                "saleCost": "abc",
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            JSON_PARSING_ERROR,
            id='saleCost_latin'
        ),
        pytest.param(
            #  saleCost: спецсимволы
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "sellFeeSum": 1234,
                "minPayment": 1234,
                "maxPayment": 1234,
                "saleCost": "!@#",
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            JSON_PARSING_ERROR,
            id='saleCost_special_symbols'
        ),
        pytest.param(
            #  saleCost: > int(64)
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "sellFeeSum": 1234,
                "blocked": False,
                "algorithm": 4,
                "minPayment": 1234,
                "maxPayment": 1234,
                "saleCost": 92233720368547758078,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            JSON_PARSING_ERROR,
            id='saleCost_over_max_value'
        ),
        pytest.param(
            #  saleCost: пустая строка
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "sellFeeSum": 1234,
                "algorithm": 4,
                "minPayment": 1234,
                "maxPayment": 1234,
                "saleCost": "",
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/saleCost_null.json',
            id='saleCost_empty_string'
        ),
        pytest.param(
            #  saleCost: с пробелом
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "sellFeeSum": 1234,
                "algorithm": 4,
                "minPayment": 1234,
                "maxPayment": 1234,
                "saleCost": " ",
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/saleCost_null.json',
            id='saleCost_space'
        ),
        pytest.param(
            #  saleCost: None
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "sellFeeSum": 1234,
                "algorithm": 4,
                "minPayment": 1234,
                "maxPayment": 1234,
                "saleCost": None,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/saleCost_null.json',
            id='saleCost_unsent_mandatory_param'
        ),
        pytest.param(
            #  saleCost: передано отрицательное значение
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "sellFeeSum": 1234,
                "algorithm": 4,
                "minPayment": 1234,
                "maxPayment": 1234,
                "saleCost": -1,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/saleCost_negative_value.json',
            id='saleCost_negative_value'
        ),
        pytest.param(
            #  thresholdCounter: кириллица
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "sellFeeSum": 1234,
                "algorithm": 4,
                "minPayment": 1234,
                "maxPayment": 1234,
                "saleCost": 1234,
                "thresholdCounter": "абв",
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            JSON_PARSING_ERROR,
            id='thresholdCounter_cyrillic'
        ),
        pytest.param(
            #  thresholdCounter: латница
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "sellFeeSum": 1234,
                "algorithm": 4,
                "minPayment": 1234,
                "maxPayment": 1234,
                "saleCost": 1234,
                "thresholdCounter": "abc",
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            JSON_PARSING_ERROR,
            id='thresholdCounter_latin'
        ),
        pytest.param(
            #  thresholdCounter: спецсимволы
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "sellFeeSum": 1234,
                "algorithm": 4,
                "minPayment": 1234,
                "maxPayment": 1234,
                "saleCost": 1234,
                "thresholdCounter": "!@#",
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            JSON_PARSING_ERROR,
            id='thresholdCounter_special_symbols'
        ),
        pytest.param(
            #  thresholdCounter: > 1500000
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "sellFeeSum": 1234,
                "algorithm": 4,
                "minPayment": 1234,
                "maxPayment": 1234,
                "saleCost": 1234,
                "thresholdCounter": 1500001,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/thresholdCounter_over_max_value.json',
            id='thresholdCounter_over_max_value'
        ),
        pytest.param(
            #  thresholdCounter: пустая строка
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "sellFeeSum": 1234,
                "algorithm": 4,
                "minPayment": 1234,
                "maxPayment": 1234,
                "saleCost": 1234,
                "thresholdCounter": "",
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/thresholdCounter_null.json',
            id='thresholdCounter_empty_string'
        ),
        pytest.param(
            #  thresholdCounter: с пробелом
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "sellFeeSum": 1234,
                "algorithm": 4,
                "minPayment": 1234,
                "maxPayment": 1234,
                "saleCost": 1234,
                "thresholdCounter": " ",
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/thresholdCounter_null.json',
            id='thresholdCounter_space'
        ),
        pytest.param(
            #  thresholdCounter: None
            {
                "category": "06.22",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "sellFeeSum": 1234,
                "algorithm": 4,
                "minPayment": 1234,
                "maxPayment": 1234,
                "saleCost": 1234,
                "thresholdCounter": None,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/thresholdCounter_null.json',
            id='thresholdCounter_unsent_mandatory_param'
        ),
        pytest.param(
            #  thresholdCounter: передано отрицательное значение
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "sellFeeSum": 1234,
                "minPayment": 1234,
                "maxPayment": 1234,
                "saleCost": 1234,
                "thresholdCounter": -1,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/thresholdCounter_negative_value.json',
            id='thresholdCounter_negative_value'
        ),
        pytest.param(
            #  maxCounter: кириллица
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "sellFeeSum": 1234,
                "algorithm": 4,
                "minPayment": 1234,
                "maxPayment": 1234,
                "saleCost": 1234,
                "thresholdCounter": 1234,
                "maxCounter": "абв",
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            JSON_PARSING_ERROR,
            id='maxCounter_cyrillic'
        ),
        pytest.param(
            #  maxCounter: латиница
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "sellFeeSum": 1234,
                "blocked": False,
                "algorithm": 4,
                "minPayment": 1234,
                "maxPayment": 1234,
                "saleCost": 1234,
                "thresholdCounter": 1234,
                "maxCounter": "abc",
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            JSON_PARSING_ERROR,
            id='maxCounter_latin'
        ),
        pytest.param(
            #  maxCounter: спецсимволы
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "sellFeeSum": 1234,
                "algorithm": 4,
                "minPayment": 1234,
                "maxPayment": 1234,
                "saleCost": 1234,
                "thresholdCounter": 1234,
                "maxCounter": "!@#",
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            JSON_PARSING_ERROR,
            id='maxCounter_special_symbols'
        ),
        pytest.param(
            #  maxCounter: пустая строка
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "sellFeeSum": 1234,
                "algorithm": 4,
                "minPayment": 1234,
                "maxPayment": 1234,
                "saleCost": 1234,
                "thresholdCounter": 1234,
                "maxCounter": "",
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/maxCounter_null.json',
            id='maxCounter_empty_string'
        ),
        pytest.param(
            #  maxCounter: пробел
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "sellFeeSum": 1234,
                "algorithm": 4,
                "minPayment": 1234,
                "maxPayment": 1234,
                "saleCost": 1234,
                "thresholdCounter": 1234,
                "maxCounter": " ",
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/maxCounter_null.json',
            id='maxCounter_space'
        ),
        pytest.param(
            #  maxCounter: None
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "sellFeeSum": 1234,
                "algorithm": 4,
                "minPayment": 1234,
                "maxPayment": 1234,
                "saleCost": 1234,
                "thresholdCounter": 1234,
                "maxCounter": None,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/maxCounter_null.json',
            id='maxCounter_null'
        ),
        pytest.param(
            #  maxCounter: > 1500000
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "sellFeeSum": 1234,
                "algorithm": 4,
                "minPayment": 1234,
                "maxPayment": 1234,
                "saleCost": 1234,
                "thresholdCounter": 1234,
                "maxCounter": 1500001,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/maxCounter_over_max_value.json',
            id='maxCounter_over_max_value'
        ),
        pytest.param(
            #  maxCounter: передано отрицательное значение
            {
                "category": "03.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "sellFeeSum": 1234,
                "algorithm": 4,
                "minPayment": 1234,
                "maxPayment": 1234,
                "saleCost": 1234,
                "thresholdCounter": 1234,
                "maxCounter": -1,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/maxCounter_negative_value.json',
            id='maxCounter_negative_value'
        ),
        pytest.param(
            #  maxCounter: передан 0
            {
                "category": "03.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "sellFeeSum": 1234,
                "algorithm": 4,
                "minPayment": 1234,
                "maxPayment": 1234,
                "saleCost": 1234,
                "thresholdCounter": 1234,
                "maxCounter": 0,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/maxCounter_zero.json',
            id='maxCounter_zero'
        ),
        pytest.param(
            #  shortDescription: > 1000 символов
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "sellFeeSum": 1234,
                "algorithm": 4,
                "minPayment": 1234,
                "maxPayment": 1234,
                "saleCost": 1234,
                "thresholdCounter": 1234,
                "maxCounter": 1234,
                "shortDescription": "a"*1001,
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/shortDescription_over_max_value.json',
            id='shortDescription_over_max_value'
        ),
        pytest.param(
            #  shortDescription: пустая строка
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "sellFeeSum": 1234,
                "algorithm": 4,
                "minPayment": 1234,
                "maxPayment": 1234,
                "saleCost": 1234,
                "thresholdCounter": 1234,
                "maxCounter": 1234,
                "shortDescription": "",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/shortDescription_empty_string.json',
            id='shortDescription_empty_string'
        ),
        pytest.param(
            #  shortDescription: с пробелом
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "sellFeeSum": 1234,
                "algorithm": 4,
                "minPayment": 1234,
                "maxPayment": 1234,
                "saleCost": 1234,
                "thresholdCounter": 1234,
                "maxCounter": 1234,
                "shortDescription": " ",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/shortDescription_space.json',
            id='shortDescription_space'
        ),
        pytest.param(
            #  shortDescription: None
            {
                "category": "06.22",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "sellFeeSum": 1234,
                "algorithm": 4,
                "minPayment": 1234,
                "maxPayment": 1234,
                "saleCost": 1234,
                "thresholdCounter": 1234,
                "maxCounter": 1234,
                "shortDescription": None,
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/shortDescription_null.json',
            id='shortDescription_unsent_mandatory_param'
        ),
        pytest.param(
            #  longDescription: > 1000 символов
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "sellFeeSum": 1234,
                "algorithm": 4,
                "minPayment": 1234,
                "maxPayment": 1234,
                "saleCost": 1234,
                "thresholdCounter": 1234,
                "maxCounter": 1234,
                "shortDescription": "Описание 123",
                "longDescription": "a"*1001,
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/longDescription_over_max_value.json',
            id='longDescription_over_max_value'
        ),
        pytest.param(
            # longDescription: пустая строка
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "sellFeeSum": 1234,
                "algorithm": 4,
                "minPayment": 1234,
                "maxPayment": 1234,
                "saleCost": 1234,
                "thresholdCounter": 1234,
                "maxCounter": 1234,
                "shortDescription": "Описание 123",
                "longDescription": "",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/longDescription_empty_string.json',
            id='longDescription_empty_string'
        ),
        pytest.param(
            # longDescription: с пробелом
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "sellFeeSum": 1234,
                "blocked": False,
                "algorithm": 4,
                "minPayment": 1234,
                "maxPayment": 1234,
                "saleCost": 1234,
                "thresholdCounter": 1234,
                "maxCounter": 1234,
                "shortDescription": "Описание 123",
                "longDescription": " ",
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/longDescription_space.json',
            id='longDescription_space'
        ),
        pytest.param(
            # longDescription: None
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "sellFeeSum": 1234,
                "algorithm": 4,
                "minPayment": 1234,
                "maxPayment": 1234,
                "saleCost": 1234,
                "thresholdCounter": 1234,
                "maxCounter": 1234,
                "shortDescription": "Описание 123",
                "longDescription": None,
                "paymentDescription": "Описание 111"
            },
            f'{NEGATIVE_RESPONSE_PATH}/longDescription_null.json',
            id='longDescription_unsent_mandatory_param'
        ),
        pytest.param(
            # paymentDescription: > 1000
            {
                "category": "06.01",
                "operatorId": 6,
                "description": "Описание",
                "sellFeeSum": 1234,
                "blocked": False,
                "algorithm": 4,
                "minPayment": 1234,
                "maxPayment": 1234,
                "saleCost": 1234,
                "thresholdCounter": 1234,
                "maxCounter": 1234,
                "shortDescription": "Описание 123",
                "longDescription": "Описание",
                "paymentDescription": "a"*1001
            },
            f'{NEGATIVE_RESPONSE_PATH}/paymentDescription_over_max_value.json',
            id='paymentDescription_over_max_value'
        ),
        pytest.param(
            # paymentDescription: пустая строка
            {
                "category": "06.68",
                "operatorId": 6,
                "description": "Описание",
                "sellFeeSum": 1234,
                "blocked": False,
                "algorithm": 4,
                "minPayment": 1234,
                "maxPayment": 1234,
                "saleCost": 1234,
                "thresholdCounter": 1234,
                "maxCounter": 1234,
                "shortDescription": "Описание 123",
                "longDescription": "Описание",
                "paymentDescription": ""
            },
            f'{NEGATIVE_RESPONSE_PATH}/paymentDescription_empty_string.json',
            id='paymentDescription_empty_string'
        ),
        pytest.param(
            # paymentDescription: с пробелом
            {
                "category": "06.67",
                "operatorId": 6,
                "sellFeeSum": 1234,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "minPayment": 1234,
                "maxPayment": 1234,
                "saleCost": 1234,
                "thresholdCounter": 1234,
                "maxCounter": 1234,
                "shortDescription": "Описание 123",
                "longDescription": "Описание",
                "paymentDescription": " "
            },
            f'{NEGATIVE_RESPONSE_PATH}/paymentDescription_space.json',
            id='paymentDescription_space'
        ),
        pytest.param(
            # paymentDescription: None
            {
                "category": "06.66",
                "operatorId": 6,
                "sellFeeSum": 1234,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "minPayment": 1234,
                "maxPayment": 1234,
                "saleCost": 1234,
                "thresholdCounter": 1234,
                "maxCounter": 1234,
                "shortDescription": "Описание 123",
                "longDescription": "Описание",
                "paymentDescription": None
            },
            f'{NEGATIVE_RESPONSE_PATH}/paymentDescription_null.json',
            id='paymentDescription_unsent_mandatory_param'
        ),
        pytest.param(
            # не отправлен обязательный параметр category
            {
                "category": None,
                "description": "Описание",
                "operatorId": 6,
                "blocked": False,
                "sellFeeSum": 1234,
                "algorithm": 4,
                "minPayment": 1234,
                "maxPayment": 1234,
                "saleCost": 1234,
                "thresholdCounter": 1234,
                "maxCounter": 1234,
                "shortDescription": "Описание 123",
                "longDescription": "Описание",
                "paymentDescription": "Описание"
            },
            f'{NEGATIVE_RESPONSE_PATH}/category_null.json',
            id='without_category'
        ),
        pytest.param(
            # не отправлен обязательный параметр description
            {
                "category": "06.65",
                "operatorId": 6,
                "blocked": False,
                "algorithm": 4,
                "minPayment": 1234,
                "sellFeeSum": 1234,
                "maxPayment": 1234,
                "saleCost": 1234,
                "thresholdCounter": 1234,
                "maxCounter": 1234,
                "shortDescription": "Описание 123",
                "longDescription": "Описание",
                "paymentDescription": "Описание"
            },
            f'{NEGATIVE_RESPONSE_PATH}/description_null.json',
            id='without_description'
        ),
        pytest.param(
            # не отправлен обязательный параметр blocked
            {
                "category": "06.22",
                "operatorId": 6,
                "description": "Описание",
                "algorithm": 4,
                "minPayment": 1234,
                "sellFeeSum": 1234,
                "maxPayment": 1234,
                "saleCost": 1234,
                "thresholdCounter": 1234,
                "maxCounter": 1234,
                "shortDescription": "Описание 123",
                "longDescription": "Описание",
                "paymentDescription": "Описание"
            },
            f'{NEGATIVE_RESPONSE_PATH}/blocked_null.json',
            id='without_blocked'
        ),
        pytest.param(
            # не отправлен обязательный параметр algorithm
            {
                "category": "06.64",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "minPayment": 1234,
                "sellFeeSum": 1234,
                "maxPayment": 1234,
                "saleCost": 1234,
                "thresholdCounter": 1234,
                "maxCounter": 1234,
                "shortDescription": "Описание 123",
                "longDescription": "Описание",
                "paymentDescription": "Описание"
            },
            f'{NEGATIVE_RESPONSE_PATH}/algorithm_null.json',
            id='without_algorithm'
        ),
        pytest.param(
            # не отправлен обязательный параметр minPayment
            {
                "category": "06.63",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "sellFeeSum": 1234,
                "algorithm": 4,
                "maxPayment": 1234,
                "saleCost": 1234,
                "thresholdCounter": 1234,
                "maxCounter": 1234,
                "shortDescription": "Описание 123",
                "longDescription": "Описание",
                "paymentDescription": "Описание"
            },
            f'{NEGATIVE_RESPONSE_PATH}/minPayment_null.json',
            id='without_minPayment'
        ),
        pytest.param(
            # не отправлен обяззательный параметр maxPayment
            {
                "category": "06.62",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "sellFeeSum": 1234,
                "minPayment": 1234,
                "saleCost": 1234,
                "thresholdCounter": 1234,
                "maxCounter": 1234,
                "shortDescription": "Описание 123",
                "longDescription": "Описание",
                "paymentDescription": "Описание"
            },
            f'{NEGATIVE_RESPONSE_PATH}/maxPayment_null.json',
            id='without_maxPayment'
        ),
        pytest.param(
            # не отправлен обяззательный параметр saleCost
            {
                "category": "06.61",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "sellFeeSum": 1234,
                "minPayment": 1234,
                "maxPayment": 1234,
                "thresholdCounter": 1234,
                "maxCounter": 1234,
                "shortDescription": "Описание 123",
                "longDescription": "Описание",
                "paymentDescription": "Описание"
            },
            f'{NEGATIVE_RESPONSE_PATH}/saleCost_null.json',
            id='without_saleCost'
        ),
        pytest.param(
            # не отправлен обяззательный параметр thresholdCounter
            {
                "category": "06.60",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "minPayment": 1234,
                "sellFeeSum": 1234,
                "maxPayment": 1234,
                "saleCost": 1234,
                "maxCounter": 1234,
                "shortDescription": "Описание 123",
                "longDescription": "Описание",
                "paymentDescription": "Описание"
            },
            f'{NEGATIVE_RESPONSE_PATH}/thresholdCounter_null.json',
            id='without_thresholdCounter'
        ),
        pytest.param(
            # не отправлен обяззательный параметр maxCounter
            {
                "category": "06.59",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "sellFeeSum": 1234,
                "algorithm": 4,
                "minPayment": 1234,
                "maxPayment": 1234,
                "saleCost": 1234,
                "thresholdCounter": 1234,
                "shortDescription": "Описание 123",
                "longDescription": "Описание",
                "paymentDescription": "Описание"
            },
            f'{NEGATIVE_RESPONSE_PATH}/maxCounter_null.json',
            id='without_maxCounter'
        ),
        pytest.param(
            # не отправлен обяззательный параметр shortDescription
            {
                "category": "06.58",
                "operatorId": 6,
                "description": "Описание",
                "sellFeeSum": 1234,
                "blocked": False,
                "algorithm": 4,
                "minPayment": 1234,
                "maxPayment": 1234,
                "saleCost": 1234,
                "thresholdCounter": 1234,
                "maxCounter": 1234,
                "longDescription": "Описание",
                "paymentDescription": "Описание"
            },
            f'{NEGATIVE_RESPONSE_PATH}/shortDescription_null.json',
            id='without_shortDescription'
        ),
        pytest.param(
            # не отправлен обяззательный параметр longDescription
            {
                "category": "06.57",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "sellFeeSum": 1234,
                "algorithm": 4,
                "minPayment": 1234,
                "maxPayment": 1234,
                "saleCost": 1234,
                "thresholdCounter": 1234,
                "maxCounter": 1234,
                "shortDescription": "Описание 123",
                "paymentDescription": "Описание"
            },
            f'{NEGATIVE_RESPONSE_PATH}/longDescription_null.json',
            id='without_longDescription'
        ),
        pytest.param(
            # не отправлен обязательный параметр paymentDescription
            {
                "category": "06.56",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "sellFeeSum": 1234,
                "algorithm": 4,
                "minPayment": 1234,
                "maxPayment": 1234,
                "saleCost": 1234,
                "thresholdCounter": 1234,
                "maxCounter": 1234,
                "shortDescription": "Описание 123",
                "longDescription": "Описание",
            },
            f'{NEGATIVE_RESPONSE_PATH}/paymentDescription_null.json',
            id='without_paymentDescription'
        ),
        pytest.param(
            # не отправлен обязательный параметр operatorId
            {
                "category": "06.55",
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "sellFeeSum": 1234,
                "minPayment": 1234,
                "maxPayment": 1234,
                "saleCost": 1234,
                "thresholdCounter": 1234,
                "maxCounter": 1234,
                "shortDescription": "Описание 123",
                "longDescription": "Описание",
                "paymentDescription": "Описание"
            },
            f'{NEGATIVE_RESPONSE_PATH}/operatorId_null.json',
            id='without_operatorId'
        ),
        pytest.param(
            # не отправлен обязательный параметр sellFeeSum
            {
                "category": "06.55",
                "description": "Описание",
                "operatorId": 6,
                "blocked": False,
                "algorithm": 4,
                "minPayment": 1234,
                "maxPayment": 1234,
                "saleCost": 1234,
                "thresholdCounter": 1234,
                "maxCounter": 1234,
                "shortDescription": "Описание 123",
                "longDescription": "Описание",
                "paymentDescription": "Описание"
            },
            f'{NEGATIVE_RESPONSE_PATH}/sellFeeSum_null.json',
            id='without_sellFeeSum'
        ),
        pytest.param(
            # передан недоступный параметр sellMonthSum
            {
                "category": "06.22",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "sellFeeSum": 1234,
                "sellMonthSum": 1234,
                "minPayment": 1234,
                "maxPayment": "!@#",
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            JSON_PARSING_ERROR,
            id='unavailable_parameter_sellMonthSum'
        ),
        pytest.param(
            # передан недоступный параметр tripSum
            {
                "category": "06.22",
                "operatorId": 6,
                "description": "Описание",
                "blocked": False,
                "algorithm": 4,
                "sellFeeSum": 1234,
                "tripSum": 1234,
                "minPayment": 1234,
                "maxPayment": "!@#",
                "saleCost": 12345,
                "thresholdCounter": 12345,
                "maxCounter": 12345,
                "shortDescription": "Описание описание",
                "longDescription": "Описание 123",
                "paymentDescription": "Описание 111"
            },
            JSON_PARSING_ERROR,
            id='unavailable_parameter_tripSum'
        ),
        ]
}
