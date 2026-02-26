import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import MachineMonitor

# Validate Production (produced, defect, runtime)


def test_TC_VP_01():
    m = MachineMonitor("M1", 5)
    assert m.validate_production(-1, 0, 10) == False


def test_TC_VP_02():
    m = MachineMonitor("M1", 5)
    assert m.validate_production(100, 200, 10) == False


def test_TC_VP_03():
    m = MachineMonitor("M1", 5)
    assert m.validate_production(100, 0, 0) == False


def test_TC_VP_04():
    m = MachineMonitor("M1", 5)
    assert m.validate_production(100, 0, 10) == True


# Calculate Efficiency (produced, defect)


def test_TC_CE_01():
    m = MachineMonitor("M1", 5)
    assert m.calculate_efficiency(0, 0) == 0


def test_TC_CE_02():
    m = MachineMonitor("M1", 5)
    assert m.calculate_efficiency(100, 5) == "SANGAT_BAIK"


def test_TC_CE_03():
    m = MachineMonitor("M1", 5)
    assert m.calculate_efficiency(100, 20) == "CUKUP"


def test_TC_CE_04():
    m = MachineMonitor("M1", 5)
    assert m.calculate_efficiency(100, 10) == "BAIK"


def test_TC_CE_05():
    m = MachineMonitor("M1", 5)
    assert m.calculate_efficiency(100, 75) == "BURUK"


# Risk Detection (Age_years(KONSTANTA), temperature, downtime)


def test_TC_RD_01():
    m = MachineMonitor("M1", 11)
    assert m.risk_detection(100, 130) == "HIGH_RISK"


def test_TC_RD_02():
    m = MachineMonitor("M1", 9)
    assert m.risk_detection(100, 130) == "MEDIUM_RISK"


def test_TC_RD_03():
    m = MachineMonitor("M1", 5)
    assert m.risk_detection(75, 65) == "LOW_RISK"
