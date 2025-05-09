import pytest
from features.steps.belly_steps import parsear_tiempo_en_horas
from features.steps.belly_steps import elegir_numero_aleatorio

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
    ("1 hora, 30 minutos y 45 segundos", 1.5125),
])

def test_parsear_tiempo_en_horas(input_text, expected_hours):
    result = parsear_tiempo_en_horas(input_text)
    assert pytest.approx(result, 0.001) == expected_hours

def test_elegir_numero_aleatorio_en_rango():
    resultado = elegir_numero_aleatorio(1, 3)
    assert 1 <= resultado <= 3, "El número aleatorio no está dentro del rango esperado"
