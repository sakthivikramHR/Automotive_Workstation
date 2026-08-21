from BMS_ECU_DTC import BatteryManagementSystem
from UDS_Service import read_dtc, clear_dtc

def test_repair_workflow(bms):
    for x in range(6):
        bms.process_telemetry(30, 3.7, 33)
    
    assert bms.state == "SENSOR_FROZEN_FAULT"
    
    # 2. Mechanic reads DTCs
    active_faults = read_dtc(bms)
    assert "B0001-11" in active_faults
    
    # 3. Mechanic clears DTCs
    clear_dtc(bms)
    assert bms.state == "NORMAL"
    assert not bms.dtc_memory