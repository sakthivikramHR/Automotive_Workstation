from BMS_ECU_DTC import BatteryManagementSystem

def read_dtc(bms):
    print("\n--- Scanning for Diagnostic Trouble Codes (UDS 0x19) ---")
    faults = bms.dtc_memory
    if not faults:
        return "No DTCs Found. System healthy."
    return f"Active DTCs: {faults}"

def clear_dtc(bms):
    print("\n--- Clearing Fault Memory (UDS 0x14) ---")
    bms.dtc_memory = []
    bms.state = "NORMAL"
    bms.contactors_closed = True
    return "DTCs Cleared."