import pytest
from src.belly import Belly

def test_pepinos_fraccionarios():
    belly = Belly()
    belly.comer(1.666)
    assert belly.pepinos_comidos == 1.666

def test_pepinos_negativo():
    belly = Belly()
    with pytest.raises(ValueError, match="No se puede comer una cantidad negativa de pepinos"): 
        belly.comer(-3)

def test_pepinos_inmensos():
    belly = Belly()
    with pytest.raises(ValueError, match="No se puede comer mucha cantidad de pepinos"): 
        belly.comer(200)

def test_gruñir_si_comido_muchos_pepinos():
    belly = Belly()
    belly.comer(15)
    belly.esperar(2)
    assert belly.esta_gruñendo() == True

def test_pepinos_restantes():
    belly = Belly()
    belly.comer(15)
    assert belly.pepinos_comidos == 15

def test_estomago_gruñendo():
    belly = Belly()
    belly.comer(20)
    belly.esperar(2)
    assert belly.esta_gruñendo() == True

def test_estomago_predecir_gruñido():
    belly = Belly()
    belly.comer(12)
    belly.esperar(1.5)
    assert belly.esta_gruñendo() == True

def test_pepinos_restante():
    belly = Belly()
    belly.comer(8)
    assert belly.pepinos_restantes() == 2