import pytest
from src.dni import DNI



def test_dni():

    numeroDni = DNI('43187839')
    numeroDni.setDni()
    assert "43187839A" ==  numeroDni.dni

    numeroDni = DNI('45348976')
    numeroDni.setDni()
    assert "45348976Z" ==  numeroDni.dni
