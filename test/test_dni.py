import pytest
from src.dni import DNI



@pytest.mark.dnis
def test_dni():

    numeroDni = DNI('43187839')
    assert "43187839A" ==  numeroDni.getDniNumber()

    numeroDni = DNI('45348976')
    assert "45348976Z" ==  numeroDni.getDniNumber()
