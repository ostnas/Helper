import pytest
from cases_utils import dict_without_key
from cases_utils import dict_with_new_key
from cases_utils import dict_with_edited_value


URL = '/travel-passes/social'
CHECK_RESULT = 'etc/responses/travel_passes/add_travel_pass/check_result/social'
POSITIVE_RESPONSE_PATH = 'etc/responses/travel_passes/add_travel_pass'
NEGATIVE_RESPONSE_PATH = 'etc/responses/errors/travel_passes/add_travel_pass/social'
JSON_PARSING_ERROR = 'etc/responses/errors/common/parsing_error.json'

data = {
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
}

TEST_SETUP = {
    "negative": [
        pytest.param(
            # category: кириллица
            dict_with_edited_value(data, "category", "06.Б5"),
            f'{NEGATIVE_RESPONSE_PATH}/category_cyrillic.json',
            id='category_cyrillic'
          ),
        pytest.param(
            # category: латиница
            dict_with_edited_value(data, "category", "F3.05"),
            f'{NEGATIVE_RESPONSE_PATH}/category_latin.json',
            id='category_latin'
          ),
        pytest.param(
            # category: длина категории больше 2-х символов
            dict_with_edited_value(data, "category", "123.05"),
            f'{NEGATIVE_RESPONSE_PATH}/category_category_over_max_value.json',
            id='category_category_over_max_value'
          ),
        pytest.param(
            # category: длина подкатегории больше 2-х символов
            dict_with_edited_value(data, "category", "06.155"),
            f'{NEGATIVE_RESPONSE_PATH}/category_subcategory_over_max_value.json',
            id='category_subcategory_over_max_value'
        ),
        pytest.param(
            # category: пустая строка
            dict_with_edited_value(data, "category", ""),
            f'{NEGATIVE_RESPONSE_PATH}/category_empty_string.json',
            id='category_empty_string'
          ),
        pytest.param(
            # category: пробел
            dict_with_edited_value(data, "category", " "),
            f'{NEGATIVE_RESPONSE_PATH}/category_space.json',
            id='category_space'
        ),
        pytest.param(
            # category: None
            dict_with_edited_value(data, "category", None),
            f'{NEGATIVE_RESPONSE_PATH}/category_null.json',
            id='category_unsent_mandatory_param'
        ),
        pytest.param(
            # category: неполностью заполненная категория
            dict_with_edited_value(data, "category", "0.02"),
            f'{NEGATIVE_RESPONSE_PATH}/category_not_a_complete_category.json',
            id='category_not_a_complete_category'
          ),
        pytest.param(
            # category: неполностью заполненная подкатегория
            dict_with_edited_value(data, "category", "06.2"),
            f'{NEGATIVE_RESPONSE_PATH}/category_not_a_complete_subcategory.json',
            id='category_not_a_complete_subcategory'
        ),
        pytest.param(
            # создание проездного с уже существующей категорией
            dict_with_edited_value(data, "category", "06.99"),
            f'{NEGATIVE_RESPONSE_PATH}/category_exists.json',
            id='category_exists'
         ),
        pytest.param(
            # operatorId: передан несуществующий оператор
            dict_with_edited_value(data, "operatorId", 134),
            f'{NEGATIVE_RESPONSE_PATH}/operatorId_nonexistent_operator.json',
            id='operatorId_nonexistent_operator'
        ),
        pytest.param(
            # operatorId: кириллица
            dict_with_edited_value(data, "operatorId", "абв"),
            JSON_PARSING_ERROR,
            id='operatorId_cyrillic'
        ),
        pytest.param(
            # operatorId: латиница
            dict_with_edited_value(data, "operatorId", "abc"),
            JSON_PARSING_ERROR,
            id='operatorId_latin'
        ),
        pytest.param(
            # operatorId: спецсимволы
            dict_with_edited_value(data, "operatorId", "!@#"),
            JSON_PARSING_ERROR,
            id='operatorId_special_symbol'
        ),
        pytest.param(
            # operatorId: пустая строка
            dict_with_edited_value(data, "operatorId", ""),
            f'{NEGATIVE_RESPONSE_PATH}/operatorId_null.json',
            id='operatorId_empty_string'
        ),
        pytest.param(
            # operatorId: с пробелом
            dict_with_edited_value(data, "operatorId", " "),
            f'{NEGATIVE_RESPONSE_PATH}/operatorId_null.json',
            id='operatorId_space'
        ),
        pytest.param(
            # operatorId: None
            dict_with_edited_value(data, "operatorId", None),
            f'{NEGATIVE_RESPONSE_PATH}/operatorId_null.json',
            id='operatorId_unsent_mandatory_param'
        ),
        pytest.param(
            # operatorId: > 16 символов
            dict_with_edited_value(data, "operatorId", 100000000000000000),
            f'{NEGATIVE_RESPONSE_PATH}/operatorId_over_max_value.json',
            id='operatorId_over_max_value'
        ),
        pytest.param(
            # description: > 512 символов
            dict_with_edited_value(data, "description", "а"*513),
            f'{NEGATIVE_RESPONSE_PATH}/description_over_max_value.json',
            id='description_over_max_value'
          ),
        pytest.param(
            # description: пустая строка
            dict_with_edited_value(data, "description", ""),
            f'{NEGATIVE_RESPONSE_PATH}/description_empty_string.json',
            id='description_empty_string'
        ),
        pytest.param(
            # description: пробел
            dict_with_edited_value(data, "description", " "),
            f'{NEGATIVE_RESPONSE_PATH}/description_space.json',
            id='description_space'
        ),
        pytest.param(
            # description: None
            dict_with_edited_value(data, "description", None),
            f'{NEGATIVE_RESPONSE_PATH}/description_null.json',
            id='description_unsent_mandatory_param'
        ),
        pytest.param(
            # blocked: латиница (кроме True/False)
            dict_with_edited_value(data, "blocked", "abc"),
            JSON_PARSING_ERROR,
            id='blocked_latin'
        ),
        pytest.param(
            # blocked: кириллица
            dict_with_edited_value(data, "blocked", "абв"),
            JSON_PARSING_ERROR,
            id='blocked_cyrillic'
        ),
        pytest.param(
            # blocked: спецсимволы
            dict_with_edited_value(data, "blocked", "!@#"),
            JSON_PARSING_ERROR,
            id='blocked_special_symbols'
        ),
        pytest.param(
            # blocked: пробел
            dict_with_edited_value(data, "blocked", " "),
            f'{NEGATIVE_RESPONSE_PATH}/blocked_null.json',
            id='blocked_space'
        ),
        pytest.param(
            # blocked: пустая строка
            dict_with_edited_value(data, "blocked", ""),
            f'{NEGATIVE_RESPONSE_PATH}/blocked_null.json',
            id='blocked_empty_string'
        ),
        pytest.param(
            # blocked: None
            dict_with_edited_value(data, "blocked", None),
            f'{NEGATIVE_RESPONSE_PATH}/blocked_null.json',
            id='blocked_unsent_mandatory_param'
        ),
        pytest.param(
            # prepaymentSum: латиница
            dict_with_edited_value(data, "prepaymentSum", "abc"),
            JSON_PARSING_ERROR,
            id='prepaymentSum_latin'
        ),
        pytest.param(
            # prepaymentSum: кириллица
            dict_with_edited_value(data, "prepaymentSum", "абв"),
            JSON_PARSING_ERROR,
            id='prepaymentSum_cyrillic'
        ),
        pytest.param(
            # prepaymentSum: спецсимволы
            dict_with_edited_value(data, "prepaymentSum", "!@#"),
            JSON_PARSING_ERROR,
            id='prepaymentSum_special_symbols'
        ),
        pytest.param(
            # prepaymentSum: > int(64)
            dict_with_edited_value(data, "prepaymentSum", 9223372036854775808),
            JSON_PARSING_ERROR,
            id='prepaymentSum_over_max_value'
        ),
        pytest.param(
            #  prepaymentSum: переданное значение 0
            dict_with_edited_value(data, "prepaymentSum", 0),
            f'{NEGATIVE_RESPONSE_PATH}/prepaymentSum_zero.json',
            id='prepaymentSum_zero'
        ),
        pytest.param(
            #  prepaymentSum: переданное отрицательное значение
            dict_with_edited_value(data, "prepaymentSum", -1),
            f'{NEGATIVE_RESPONSE_PATH}/prepaymentSum_negative_value.json',
            id='prepaymentSum_negative_value'
        ),
        pytest.param(
            # algorithm: латиница
            dict_with_edited_value(data, "algorithm", "abc"),
            JSON_PARSING_ERROR,
            id='algorithm_latin'
        ),
        pytest.param(
            # algorithm: кириллица
            dict_with_edited_value(data, "prepaymentSum", "абв"),
            JSON_PARSING_ERROR,
            id='algorithm_cyrillic'
        ),
        pytest.param(
            # algorithm: спецсимволы
            dict_with_edited_value(data, "algorithm", "!@#"),
            JSON_PARSING_ERROR,
            id='algorithm_special_symbols'
        ),
        pytest.param(
            # несуществующий algorithm: 6
            dict_with_edited_value(data, "algorithm", 6),
            f'{NEGATIVE_RESPONSE_PATH}/algorithm_nonexistent_algorithm.json',
            id='algorithm_nonexistent_algorithm'
        ),
        pytest.param(
            # algorithm: с пробелом
            dict_with_edited_value(data, "algorithm", " "),
            f'{NEGATIVE_RESPONSE_PATH}/algorithm_null.json',
            id='algorithm_empty_space'
        ),
        pytest.param(
            # algorithm: пустая строка
            dict_with_edited_value(data, "algorithm", ""),
            f'{NEGATIVE_RESPONSE_PATH}/algorithm_null.json',
            id='algorithm_empty_string'
        ),
        pytest.param(
            # algorithm: None
            dict_with_edited_value(data, "algorithm", None),
            f'{NEGATIVE_RESPONSE_PATH}/algorithm_null.json',
            id='algorithm_unsent_mandatory_param'
        ),
        pytest.param(
            # algorithm: отрицательное значение
            dict_with_edited_value(data, "algorithm", -1),
            f'{NEGATIVE_RESPONSE_PATH}/algorithm_negative_value.json',
            id='algorithm_negative_value'
        ),
        pytest.param(
            # dateRestriction.period : кириллица
            dict_with_edited_value(data, "dateRestriction.period", "абв"),
            JSON_PARSING_ERROR,
            id='dateRestriction_period_cyrillic'
        ),
        pytest.param(
            # dateRestriction.period : латиница
            dict_with_edited_value(data, "dateRestriction.period", "abc"),
            JSON_PARSING_ERROR,
            id='dateRestriction_period_latin'
        ),
        pytest.param(
            # dateRestriction.period : спецсимволы
            dict_with_edited_value(data, "dateRestriction.period", "!@#"),
            JSON_PARSING_ERROR,
            id='dateRestriction_period_special_symbols'
        ),
        pytest.param(
            #  dateRestriction.period : > int(32)
            dict_with_edited_value(data, "dateRestriction.period", 2147483648),
            JSON_PARSING_ERROR,
            id='dateRestriction_period_over_max_value'
        ),
        pytest.param(
            #  dateRestriction.period : несуществующий период
            dict_with_edited_value(data, "dateRestriction.period", 8),
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_period_nonexistent.json',
            id='dateRestriction_period_nonexistent'
        ),
        pytest.param(
            #  dateRestriction.period : с пробелом
            dict_with_edited_value(data, "dateRestriction.period", " "),
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_period_null.json',
            id='dateRestriction_period_space'
        ),
        pytest.param(
            #  dateRestriction.period : пустая строка
            dict_with_edited_value(data, "dateRestriction.period", ""),
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_period_null.json',
            id='dateRestriction_period_empty_string'
        ),
        pytest.param(
            #  dateRestriction.period : None
            dict_with_edited_value(data, "dateRestriction.period", None),
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_period_null.json',
            id='dateRestriction_period_unsent_mandatory_param'
        ),
        pytest.param(
            #  dateRestriction.startHours : кириллица
            dict_with_edited_value(data, "dateRestriction.startHours", "абв"),
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_startHours_cyrillic.json',
            id='dateRestriction_startHours_cyrillic'
        ),
        pytest.param(
            #  dateRestriction.startHours : латиница
            dict_with_edited_value(data, "dateRestriction.startHours", "abc"),
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_startHours_latin.json',
            id='dateRestriction_startHours_latin'
        ),
        pytest.param(
            #  dateRestriction.startHours : спецсимволы
            dict_with_edited_value(data, "dateRestriction.startHours", "!@#"),
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_startHours_special_symbols.json',
            id='dateRestriction_startHours_special_symbols'
        ),
        pytest.param(
            # dateRestriction.startHours : None
            dict_with_edited_value(data, "dateRestriction.startHours", None),
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_startHours_null.json',
            id='dateRestriction_startHours_unsent_mandatory_param'
        ),
        pytest.param(
            #  dateRestriction.startHours : пустая строка
            dict_with_edited_value(data, "dateRestriction.startHours", ""),
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_startHours_empty_string.json',
            id='dateRestriction_startHours_empty_string'
        ),
        pytest.param(
            #  dateRestriction.startHours : с пробелом
            dict_with_edited_value(data, "dateRestriction.startHours", " "),
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_startHours_space.json',
            id='dateRestriction_startHours_space'
        ),
        pytest.param(
            #  dateRestriction.endHours : кириллица
            dict_with_edited_value(data, "dateRestriction.endHours", "абв"),
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_endHours_cyrillic.json',
            id='endHours_cyrillic'
        ),
        pytest.param(
            #  dateRestriction.endHours : латиница
            dict_with_edited_value(data, "dateRestriction.endHours", "abc"),
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_endHours_latin.json',
            id='endHours_latin'
        ),
        pytest.param(
            #  dateRestriction.endHours : спецсимволы
            dict_with_edited_value(data, "dateRestriction.endHours", "!@#"),
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_endHours_special_symbols.json',
            id='endHours_special_symbols'
        ),
        pytest.param(
            #  dateRestriction.endHours : None
            dict_with_edited_value(data, "dateRestriction.endHours", None),
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_endHours_null.json',
            id='dateRestriction_endHours_unsent_mandatory_param'
        ),
        pytest.param(
            #  dateRestriction.endHours : с пробелом
            dict_with_edited_value(data, "dateRestriction.endHours", " "),
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_endHours_space.json',
            id='dateRestriction_endHours_space'
        ),
        pytest.param(
            #  dateRestriction.endHours : пустая строка
            dict_with_edited_value(data, "dateRestriction.endHours", ""),
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_endHours_empty_string.json',
            id='dateRestriction_endHours_empty_string'
        ),
        pytest.param(
            #  dateRestriction : значение startHours больше значения endHours
            dict_with_edited_value(dict_with_edited_value(data, "dateRestriction.startHours", "12:00"), "dateRestriction.endHours", "11:00"),
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_startHours_more_endHours.json',
            id='dateRestriction_startHours_more_endHours'
        ),
        pytest.param(
            #  dateRestriction : передан только period
            dict_without_key(dict_without_key(data, "dateRestriction.startHours"), "dateRestriction.endHours"),
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_only_period.json',
            id='dateRestriction_only_period'
        ),
        pytest.param(
            #  dateRestriction : передан только startHours
            dict_without_key(dict_without_key(data, "dateRestriction.endHours"), "dateRestriction.period"),
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_only_startHours.json',
            id='dateRestriction_only_startHours'
        ),
        pytest.param(
            #  dateRestriction : передан только endHours
            dict_without_key(dict_without_key(data, "dateRestriction.startHours"), "dateRestriction.period"),
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_only_endHours.json',
            id='dateRestriction_only_endHours'
        ),
        pytest.param(
            #  dateRestriction : в параметре startHours указан некорректный формат времени
            dict_with_edited_value(data, "dateRestriction.startHours", "130:00"),
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_startHours_incorrect_time_format.json',
            id='dateRestriction_startHours_incorrect_time_format'
        ),
        pytest.param(
            #  dateRestriction : в параметре endHours указан некорректный формат времени
            dict_with_edited_value(data, "dateRestriction.endHours", "110:00"),
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_endHours_incorrect_time_format.json',
            id='dateRestriction_endHours_incorrect_time_format'
        ),
        pytest.param(
            #  dateRestriction : в параметре startHours число минут не кратно 10
            dict_with_edited_value(data, "dateRestriction.startHours", "10:13"),
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_startHours_incorrect_format_minutes.json',
            id='dateRestriction_startHours_incorrect_format_minutes'
        ),
        pytest.param(
            #  dateRestriction : в параметре endHours число минут не кратно 10
            dict_with_edited_value(data, "dateRestriction.endHours", "12:13"),
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_endHours_incorrect_format_minutes.json',
            id='dateRestriction_endHours_incorrect_format_minutes'
        ),
        pytest.param(
            #  dateRestriction : в параметре startHours передано число, как данные хранятся в БД
            dict_with_edited_value(data, "dateRestriction.startHours", "70"),
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_startHours_number.json',
            id='dateRestriction_startHours_number'
        ),
        pytest.param(
            #  dateRestriction : в параметре endHours передано число, как данные хранятся в БД
            dict_with_edited_value(data, "dateRestriction.endHours", "86"),
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_endHours_number.json',
            id='dateRestriction_endHours_number'
        ),
        pytest.param(
            #  dateRestriction : отравлен пустой объект
            dict_with_edited_value(data, "dateRestriction", {}),
            f'{NEGATIVE_RESPONSE_PATH}/dateRestriction_empty_object.json',
            id='dateRestriction_empty_object'
        ),
        pytest.param(
            #  transportRestriction : передан несуществующий транспорт
            dict_with_edited_value(data, "transportRestriction", [12]),
            f'{NEGATIVE_RESPONSE_PATH}/transportRestriction_existent_and_nonexistent_id_transport.json',
            id='transportRestriction_nonexistent_id_transport'
        ),
        pytest.param(
            #  transportRestriction : кириллица
            dict_with_edited_value(data, "transportRestriction", ["абв"]),
            JSON_PARSING_ERROR,
            id='transportRestriction_cyrillic'
        ),
        pytest.param(
            #  transportRestriction : латиница
            dict_with_edited_value(data, "transportRestriction", ["abc"]),
            JSON_PARSING_ERROR,
            id='transportRestriction_latin'
        ),
        pytest.param(
            #  transportRestriction : спецсимволы
            dict_with_edited_value(data, "transportRestriction", ["!@#"]),
            JSON_PARSING_ERROR,
            id='transportRestriction_special_symbols'
        ),
        pytest.param(
            #  transportRestriction : > int(32)
            dict_with_edited_value(data, "transportRestriction", 2147483648),
            JSON_PARSING_ERROR,
            id='transportRestriction_over_max_value'
        ),
        pytest.param(
            #  transportRestriction : передан существующий и несуществующий транспорт
            dict_with_edited_value(data, "transportRestriction", [1, 12]),
            f'{NEGATIVE_RESPONSE_PATH}/transportRestriction_existent_and_nonexistent_id_transport.json',
            id='transportRestriction_existent_and_nonexistent_id_transport'
        ),
        pytest.param(
            #  sellFeeSum : латиница
            dict_with_edited_value(data, "sellFeeSum", "abc"),
            JSON_PARSING_ERROR,
            id='sellFeeSum_latin'
        ),
        pytest.param(
            #  sellFeeSum : кириллица
            dict_with_edited_value(data, "sellFeeSum", "абв"),
            JSON_PARSING_ERROR,
            id='sellFeeSum_cyrillic'
        ),
        pytest.param(
            #  sellFeeSum : спецсимволы
            dict_with_edited_value(data, "sellFeeSum", "!@#"),
            JSON_PARSING_ERROR,
            id='sellFeeSum_special_symbols'
        ),
        pytest.param(
            #  sellFeeSum: > 6 символов
            dict_with_edited_value(data, "sellFeeSum", 1234567),
            f'{NEGATIVE_RESPONSE_PATH}/sellFeeSum_over_max_value.json',
            id='sellFeeSum_over_max_value'
        ),
        pytest.param(
            #  sellFeeSum: отрицательное значение
            dict_with_edited_value(data, "sellFeeSum", -1),
            f'{NEGATIVE_RESPONSE_PATH}/sellFeeSum_negative_value.json',
            id='sellFeeSum_negative_value'
        ),
        pytest.param(
            #  sellFeeSum: пустая строка
            dict_with_edited_value(data, "sellFeeSum", ""),
            f'{NEGATIVE_RESPONSE_PATH}/sellFeeSum_null.json',
            id='sellFeeSum_empty_string'
        ),
        pytest.param(
            #  sellFeeSum: пробел
            dict_with_edited_value(data, "sellFeeSum", " "),
            f'{NEGATIVE_RESPONSE_PATH}/sellFeeSum_null.json',
            id='sellFeeSum_space'
        ),
        pytest.param(
            #  sellFeeSum: None
            dict_with_edited_value(data, "sellFeeSum", None),
            f'{NEGATIVE_RESPONSE_PATH}/sellFeeSum_null.json',
            id='sellFeeSum_null'
        ),
        pytest.param(
            #  minPayment: кириллица
            dict_with_edited_value(data, "minPayment", "абв"),
            JSON_PARSING_ERROR,
            id='in_minPayment_cyrillic'
        ),
        pytest.param(
            #  minPayment: латиница
            dict_with_edited_value(data, "minPayment", "abc"),
            JSON_PARSING_ERROR,
            id='minPayment_latin'
        ),
        pytest.param(
            #  minPayment: спецсимволы
            dict_with_edited_value(data, "minPayment", "!@#"),
            JSON_PARSING_ERROR,
            id='in_minPayment_special_symbols'
        ),
        pytest.param(
            #  minPayment: > int(64)
            dict_with_edited_value(data, "minPayment", 9223372036854775808),
            JSON_PARSING_ERROR,
            id='minPayment_over_max_value'
        ),
        pytest.param(
            # minPayment: пустая строка
            dict_with_edited_value(data, "minPayment", ""),
            f'{NEGATIVE_RESPONSE_PATH}/minPayment_null.json',
            id='minPayment_empty_string'
        ),
        pytest.param(
            # minPayment: с пробелом
            dict_with_edited_value(data, "minPayment", " "),
            f'{NEGATIVE_RESPONSE_PATH}/minPayment_null.json',
            id='minPayment_space'
        ),
        pytest.param(
            # minPayment: None
            dict_with_edited_value(data, "minPayment", None),
            f'{NEGATIVE_RESPONSE_PATH}/minPayment_null.json',
            id='minPayment_unsent_mandatory_param'
        ),
        pytest.param(
            # minPayment: передано отрицательное значение
            dict_with_edited_value(data, "minPayment", -1),
            f'{NEGATIVE_RESPONSE_PATH}/minPayment_negative_value.json',
            id='minPayment_negative_value'
        ),
        pytest.param(
            # maxPayment: кириллица
            dict_with_edited_value(data, "minPayment", "абв"),
            JSON_PARSING_ERROR,
            id='maxPayment_cyrillic'
        ),
        pytest.param(
            # maxPayment: латиница
            dict_with_edited_value(data, "maxPayment", "abc"),
            JSON_PARSING_ERROR,
            id='maxPayment_latin'
        ),
        pytest.param(
            # maxPayment: спецсимволы
            dict_with_edited_value(data, "maxPayment", "!@#"),
            JSON_PARSING_ERROR,
            id='maxPayment_special_symbols'
        ),
        pytest.param(
            #  maxPayment: > int(64)
            dict_with_edited_value(data, "maxPayment", 9223372036854775808),
            JSON_PARSING_ERROR,
            id='maxPayment_over_max_value'
        ),
        pytest.param(
            # maxPayment: пустая строка
            dict_with_edited_value(data, "maxPayment", ""),
            f'{NEGATIVE_RESPONSE_PATH}/maxPayment_null.json',
            id='maxPayment_empty_string'
        ),
        pytest.param(
            # maxPayment: пробел
            dict_with_edited_value(data, "maxPayment", " "),
            f'{NEGATIVE_RESPONSE_PATH}/maxPayment_null.json',
            id='maxPayment_space'
        ),
        pytest.param(
            # maxPayment: None
            dict_with_edited_value(data, "maxPayment", None),
            f'{NEGATIVE_RESPONSE_PATH}/maxPayment_null.json',
            id='maxPayment_unsent_mandatory_param'
        ),
        pytest.param(
            #  maxPayment: переданное отрицательное значение
            dict_with_edited_value(data, "maxPayment", -1),
            f'{NEGATIVE_RESPONSE_PATH}/maxPayment_negative_value.json',
            id='maxPayment_negative_value'
        ),
        pytest.param(
            #  maxPayment: передан 0
            dict_with_edited_value(data, "maxPayment", 0),
            f'{NEGATIVE_RESPONSE_PATH}/maxPayment_zero.json',
            id='maxPayment_zero'
        ),
        pytest.param(
            #  saleCost: кириллица
            dict_with_edited_value(data, "saleCost", "абв"),
            JSON_PARSING_ERROR,
            id='saleCost_cyrillic'
        ),
        pytest.param(
            #  saleCost: латиница
            dict_with_edited_value(data, "saleCost", "abc"),
            JSON_PARSING_ERROR,
            id='saleCost_latin'
        ),
        pytest.param(
            #  saleCost: спецсимволы
            dict_with_edited_value(data, "saleCost", "!@#"),
            JSON_PARSING_ERROR,
            id='saleCost_special_symbols'
        ),
        pytest.param(
            #  saleCost: > int(64)
            dict_with_edited_value(data, "saleCost", 9223372036854775808),
            JSON_PARSING_ERROR,
            id='saleCost_over_max_value'
        ),
        pytest.param(
            #  saleCost: пустая строка
            dict_with_edited_value(data, "saleCost", ""),
            f'{NEGATIVE_RESPONSE_PATH}/saleCost_null.json',
            id='saleCost_empty_string'
        ),
        pytest.param(
            #  saleCost: с пробелом
            dict_with_edited_value(data, "saleCost", " "),
            f'{NEGATIVE_RESPONSE_PATH}/saleCost_null.json',
            id='saleCost_space'
        ),
        pytest.param(
            #  saleCost: None
            dict_with_edited_value(data, "saleCost", None),
            f'{NEGATIVE_RESPONSE_PATH}/saleCost_null.json',
            id='saleCost_unsent_mandatory_param'
        ),
        pytest.param(
            #  saleCost: передано отрицательное значение
            dict_with_edited_value(data, "saleCost", -1),
            f'{NEGATIVE_RESPONSE_PATH}/saleCost_negative_value.json',
            id='saleCost_negative_value'
        ),
        pytest.param(
            #  thresholdCounter: кириллица
            dict_with_edited_value(data, "thresholdCounter", "абв"),
            JSON_PARSING_ERROR,
            id='thresholdCounter_cyrillic'
        ),
        pytest.param(
            #  thresholdCounter: латница
            dict_with_edited_value(data, "thresholdCounter", "abc"),
            JSON_PARSING_ERROR,
            id='thresholdCounter_latin'
        ),
        pytest.param(
            #  thresholdCounter: спецсимволы
            dict_with_edited_value(data, "thresholdCounter", "!@#"),
            JSON_PARSING_ERROR,
            id='thresholdCounter_special_symbols'
        ),
        pytest.param(
            #  thresholdCounter: > 1500000
            dict_with_edited_value(data, "thresholdCounter", 1500001),
            f'{NEGATIVE_RESPONSE_PATH}/thresholdCounter_over_max_value.json',
            id='thresholdCounter_over_max_value'
        ),
        pytest.param(
            #  thresholdCounter: пустая строка
            dict_with_edited_value(data, "thresholdCounter", ""),
            f'{NEGATIVE_RESPONSE_PATH}/thresholdCounter_null.json',
            id='thresholdCounter_empty_string'
        ),
        pytest.param(
            #  thresholdCounter: с пробелом
            dict_with_edited_value(data, "thresholdCounter", " "),
            f'{NEGATIVE_RESPONSE_PATH}/thresholdCounter_null.json',
            id='thresholdCounter_space'
        ),
        pytest.param(
            #  thresholdCounter: None
            dict_with_edited_value(data, "thresholdCounter", None),
            f'{NEGATIVE_RESPONSE_PATH}/thresholdCounter_null.json',
            id='thresholdCounter_unsent_mandatory_param'
        ),
        pytest.param(
            #  thresholdCounter: передано отрицательное значение
            dict_with_edited_value(data, "thresholdCounter", -1),
            f'{NEGATIVE_RESPONSE_PATH}/thresholdCounter_negative_value.json',
            id='thresholdCounter_negative_value'
        ),
        pytest.param(
            #  maxCounter: кириллица
            dict_with_edited_value(data, "maxCounter", "абв"),
            JSON_PARSING_ERROR,
            id='maxCounter_cyrillic'
        ),
        pytest.param(
            #  maxCounter: латиница
            dict_with_edited_value(data, "maxCounter", "abc"),
            JSON_PARSING_ERROR,
            id='maxCounter_latin'
        ),
        pytest.param(
            #  maxCounter: спецсимволы
            dict_with_edited_value(data, "maxCounter", "!@#"),
            JSON_PARSING_ERROR,
            id='maxCounter_special_symbols'
        ),
        pytest.param(
            #  maxCounter: пустая строка
            dict_with_edited_value(data, "maxCounter", ""),
            f'{NEGATIVE_RESPONSE_PATH}/maxCounter_null.json',
            id='maxCounter_empty_string'
        ),
        pytest.param(
            #  maxCounter: пробел
            dict_with_edited_value(data, "maxCounter", " "),
            f'{NEGATIVE_RESPONSE_PATH}/maxCounter_null.json',
            id='maxCounter_space'
        ),
        pytest.param(
            #  maxCounter: None
            dict_with_edited_value(data, "maxCounter", None),
            f'{NEGATIVE_RESPONSE_PATH}/maxCounter_null.json',
            id='maxCounter_null'
        ),
        pytest.param(
            #  maxCounter: > 1500000
            dict_with_edited_value(data, "maxCounter", 1500001),
            f'{NEGATIVE_RESPONSE_PATH}/maxCounter_over_max_value.json',
            id='maxCounter_over_max_value'
        ),
        pytest.param(
            #  maxCounter: передано отрицательное значение
            dict_with_edited_value(data, "maxCounter", -1),
            f'{NEGATIVE_RESPONSE_PATH}/maxCounter_negative_value.json',
            id='maxCounter_negative_value'
        ),
        pytest.param(
            #  maxCounter: передан 0
            dict_with_edited_value(data, "maxCounter", 0),
            f'{NEGATIVE_RESPONSE_PATH}/maxCounter_zero.json',
            id='maxCounter_zero'
        ),
        pytest.param(
            #  shortDescription: > 1000 символов
            dict_with_edited_value(data, "shortDescription", "a"*1001),
            f'{NEGATIVE_RESPONSE_PATH}/shortDescription_over_max_value.json',
            id='shortDescription_over_max_value'
        ),
        pytest.param(
            #  shortDescription: пустая строка
            dict_with_edited_value(data, "shortDescription", ""),
            f'{NEGATIVE_RESPONSE_PATH}/shortDescription_empty_string.json',
            id='shortDescription_empty_string'
        ),
        pytest.param(
            #  shortDescription: с пробелом
            dict_with_edited_value(data, "shortDescription", " "),
            f'{NEGATIVE_RESPONSE_PATH}/shortDescription_space.json',
            id='shortDescription_space'
        ),
        pytest.param(
            #  shortDescription: None
            dict_with_edited_value(data, "shortDescription", None),
            f'{NEGATIVE_RESPONSE_PATH}/shortDescription_null.json',
            id='shortDescription_unsent_mandatory_param'
        ),
        pytest.param(
            #  longDescription: > 1000 символов
            dict_with_edited_value(data, "longDescription", "a"*1001),
            f'{NEGATIVE_RESPONSE_PATH}/longDescription_over_max_value.json',
            id='longDescription_over_max_value'
        ),
        pytest.param(
            # longDescription: пустая строка
            dict_with_edited_value(data, "longDescription", ""),
            f'{NEGATIVE_RESPONSE_PATH}/longDescription_empty_string.json',
            id='longDescription_empty_string'
        ),
        pytest.param(
            # longDescription: с пробелом
            dict_with_edited_value(data, "longDescription", " "),
            f'{NEGATIVE_RESPONSE_PATH}/longDescription_space.json',
            id='longDescription_space'
        ),
        pytest.param(
            # longDescription: None
            dict_with_edited_value(data, "longDescription", None),
            f'{NEGATIVE_RESPONSE_PATH}/longDescription_null.json',
            id='longDescription_unsent_mandatory_param'
        ),
        pytest.param(
            # paymentDescription: > 1000
            dict_with_edited_value(data, "longDescription", "a"*1001),
            f'{NEGATIVE_RESPONSE_PATH}/paymentDescription_over_max_value.json',
            id='paymentDescription_over_max_value'
        ),
        pytest.param(
            # paymentDescription: пустая строка
            dict_with_edited_value(data, "paymentDescription", ""),
            f'{NEGATIVE_RESPONSE_PATH}/paymentDescription_empty_string.json',
            id='paymentDescription_empty_string'
        ),
        pytest.param(
            # paymentDescription: с пробелом
            dict_with_edited_value(data, "paymentDescription", " "),
            f'{NEGATIVE_RESPONSE_PATH}/paymentDescription_space.json',
            id='paymentDescription_space'
        ),
        pytest.param(
            # paymentDescription: None
            dict_with_edited_value(data, "paymentDescription", None),
            f'{NEGATIVE_RESPONSE_PATH}/paymentDescription_null.json',
            id='paymentDescription_unsent_mandatory_param'
        ),
        pytest.param(
            # не отправлен обязательный параметр category
            dict_without_key(data, "category"),
            f'{NEGATIVE_RESPONSE_PATH}/category_null.json',
            id='without_category'
        ),
        pytest.param(
            # не отправлен обязательный параметр description
            dict_without_key(data, "description"),
            f'{NEGATIVE_RESPONSE_PATH}/description_null.json',
            id='without_description'
        ),
        pytest.param(
            # не отправлен обязательный параметр blocked
            dict_without_key(data, "blocked"),
            f'{NEGATIVE_RESPONSE_PATH}/blocked_null.json',
            id='without_blocked'
        ),
        pytest.param(
            # не отправлен обязательный параметр algorithm
            dict_without_key(data, "algorithm"),
            f'{NEGATIVE_RESPONSE_PATH}/algorithm_null.json',
            id='without_algorithm'
        ),
        pytest.param(
            # не отправлен обязательный параметр minPayment
            dict_without_key(data, "minPayment"),
            f'{NEGATIVE_RESPONSE_PATH}/minPayment_null.json',
            id='without_minPayment'
        ),
        pytest.param(
            # не отправлен обяззательный параметр maxPayment
            dict_without_key(data, "maxPayment"),
            f'{NEGATIVE_RESPONSE_PATH}/maxPayment_null.json',
            id='without_maxPayment'
        ),
        pytest.param(
            # не отправлен обяззательный параметр saleCost
            dict_without_key(data, "saleCost"),
            f'{NEGATIVE_RESPONSE_PATH}/saleCost_null.json',
            id='without_saleCost'
        ),
        pytest.param(
            # не отправлен обяззательный параметр thresholdCounter
            dict_without_key(data, "thresholdCounter"),
            f'{NEGATIVE_RESPONSE_PATH}/thresholdCounter_null.json',
            id='without_thresholdCounter'
        ),
        pytest.param(
            # не отправлен обяззательный параметр maxCounter
            dict_without_key(data, "maxCounter"),
            f'{NEGATIVE_RESPONSE_PATH}/maxCounter_null.json',
            id='without_maxCounter'
        ),
        pytest.param(
            # не отправлен обяззательный параметр shortDescription
            dict_without_key(data, "shortDescription"),
            f'{NEGATIVE_RESPONSE_PATH}/shortDescription_null.json',
            id='without_shortDescription'
        ),
        pytest.param(
            # не отправлен обяззательный параметр longDescription
            dict_without_key(data, "longDescription"),
            f'{NEGATIVE_RESPONSE_PATH}/longDescription_null.json',
            id='without_longDescription'
        ),
        pytest.param(
            # не отправлен обязательный параметр paymentDescription
            dict_without_key(data, "paymentDescription"),
            f'{NEGATIVE_RESPONSE_PATH}/paymentDescription_null.json',
            id='without_paymentDescription'
        ),
        pytest.param(
            # не отправлен обязательный параметр operatorId
            dict_without_key(data, "operatorId"),
            f'{NEGATIVE_RESPONSE_PATH}/operatorId_null.json',
            id='without_operatorId'
        ),
        pytest.param(
            # не отправлен обязательный параметр sellFeeSum
            dict_without_key(data, "sellFeeSum"),
            f'{NEGATIVE_RESPONSE_PATH}/sellFeeSum_null.json',
            id='without_sellFeeSum'
        ),
        pytest.param(
            # передан недоступный параметр sellMonthSum
            dict_with_new_key(data, "sellMonthSum", 1234),
            JSON_PARSING_ERROR,
            id='unavailable_parameter_sellMonthSum'
        ),
        pytest.param(
            # передан недоступный параметр tripSum
            dict_with_new_key(data, "tripSum", 1234),
            JSON_PARSING_ERROR,
            id='unavailable_parameter_tripSum'
        ),
        ]
}