import pytest
from features.steps.belly_steps import parsear_tiempo_en_horas

@pytest.mark.parametrize("input_text, expected_hours", [
    ("una hora", 1.0),
    ("dos horas", 2.0),
    ("media hora", 0.5),
    ("treinta minutos", 0.5),
    ("una hora y treinta minutos", 1.5),
    ("dos horas quince minutos", 2.25),
    ("una hora veinte minutos diez segundos", 1.3361),
    ("dos horas y", 2.0),
    ("y treinta minutos", 0.5),
    ("una hora y veinte minutos", 1.3333),
    ("0 horas 45 minutos", 0.75),
    ("45 minutos", 0.75),
])

def test_parsear_tiempo_en_horas(input_text, expected_hours):
    result = parsear_tiempo_en_horas(input_text)
    assert pytest.approx(result, 0.001) == expected_hours
