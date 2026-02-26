import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import MachineMonitor


def test_validate_production():
    """Test validasi data produksi"""
    monitor = MachineMonitor("M1", 5)
    assert monitor.validate_production(100, 5, 8) == True
    assert monitor.validate_production(0, 0, 0) == True
    assert monitor.validate_production(-10, 5, 8) == False
    assert monitor.validate_production(50, 60, 8) == False
    assert monitor.validate_production(50, 5, 0) == False


def test_calculate_efficiency():
    monitor = MachineMonitor("M1", 5)

    assert monitor.calculate_efficiency(100, 0) == "SANGAT_BAIK"  # 100%
    assert monitor.calculate_efficiency(100, 5) == "SANGAT_BAIK"  # 95%
    assert monitor.calculate_efficiency(100, 10) == "BAIK"  # 90%
    assert monitor.calculate_efficiency(100, 25) == "CUKUP"  # 75%
    assert monitor.calculate_efficiency(100, 50) == "BURUK"  # 50%
    assert monitor.calculate_efficiency(0, 0) == 0  # tidak ada produksi


def test_risk_detection():
    mesin_baru = MachineMonitor("M3", 5)
    mesin_lama = MachineMonitor("M4", 15)

    # Test low risk
    assert mesin_baru.risk_detection(70, 30) == "LOW_RISK"
    assert mesin_lama.risk_detection(70, 30) == "LOW_RISK"

    # Test medium risk
    assert mesin_baru.risk_detection(85, 70) == "MEDIUM_RISK"
    assert mesin_lama.risk_detection(85, 70) == "MEDIUM_RISK"

    # Test high risk
    assert mesin_lama.risk_detection(95, 130) == "HIGH_RISK"


def test_gabungan():
    # Mesin baru dengan kualitas bagus
    new_machine = MachineMonitor("NEW_001", 3)
    assert new_machine.validate_production(1000, 50, 8) == True
    assert new_machine.calculate_efficiency(1000, 50) == "SANGAT_BAIK"  # 95%
    assert new_machine.machine_status(15) == "NORMAL"
    assert new_machine.risk_detection(75, 15) == "LOW_RISK"

    # Mesin tua dengan masalah
    old_machine = MachineMonitor("OLD_001", 12)
    assert old_machine.validate_production(800, 400, 8) == True
    assert old_machine.calculate_efficiency(800, 400) == "BURUK"  # 50%
    assert old_machine.machine_status(200) == "KRITIS"
    assert old_machine.risk_detection(95, 200) == "HIGH_RISK"
