import pytest
import json
from Aufgabe2_BMS_ECU import BatteryManagementSystem

# Load requirements for reporting
with open("Aufgabe2_requirements.json") as f:
    REQS = json.load(f)

@pytest.fixture

def bms():
    """Provides a fresh BMS instance for every test."""
    return BatteryManagementSystem()

def test_thermal_shutdown_requirement(bms):
    """Verify REQ_BMS_001: Shutdown on high temp."""
    # Test Step: Inject 65 degrees
    bms.process_telemetry(temp=65, voltage=3.7)
    
    status = bms.get_status()
    
    assert status["state"] == "SHUTDOWN"
    assert status["contactors"] is False
    print(f"\nVerified {REQS['REQ_BMS_001']}")

def test_overvoltage_fault_requirement(bms):
    """Verify REQ_BMS_002: Fault on high voltage."""
    # Test Step: Inject 4.5V
    bms.process_telemetry(temp=25, voltage=4.5)
    
    status = bms.get_status()
    
    assert status["state"] == "OVERVOLTAGE_FAULT"
    assert status["contactors"] is False
    print(f"\nVerified {REQS['REQ_BMS_002']}")

def test_normal_fault_requirement(bms):
    """Verify REQ_BMS_003: Normal"""
    # Test Step: Have both temperature and voltage under limits
    bms.process_telemetry(temp=25, voltage=4.1)
    
    status = bms.get_status()
    
    assert status["state"] == "COMPLETELY NORMAL"
    assert status["contactors"] is False
    print(f"\nVerified {REQS['REQ_BMS_003']}")


def test_undervoltage_fault_requirement(bms):
    """Verify REQ_BMS_004: Undervoltage"""
    # Test Step: Have both temperature and voltage under limits
    bms.process_telemetry(temp=45, voltage=2.3)
    
    status = bms.get_status()
    
    assert status["state"] == "COMPLETELY NORMAL"
    assert status["contactors"] is False
    print(f"\nVerified {REQS['REQ_BMS_004']}")