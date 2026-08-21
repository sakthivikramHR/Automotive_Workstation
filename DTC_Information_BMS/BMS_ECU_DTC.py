class BatteryManagementSystem:
    def __init__(self):
        self.state = "NORMAL"
        self.contactors_closed = True
        self.dtc_memory = []
        
        self.DTC_TABLE = {
            "SENSOR_ERROR": "B0001-13", 
            "SENSOR_FROZEN_FAULT": "B0001-11", 
            "COMM_CORRUPTION_FAULT": "U0100-00",
            "SHUTDOWN": "P0A0D-00"
        }

    def process_telemetry(self, temperature, voltage, checksum):
        
        expected_checksum = int(temperature + voltage) if temperature and voltage else 0
        
        if checksum != expected_checksum:
            self.state = "CRC_COMMUNICATION_ERROR"
            self.contactors_closed = False
            return
        
        if self.state != "NORMAL" and self.state not in self.dtc_memory:
            dtc_code = self.DTC_TABLE.get(self.state, "P0000-00")
            self.dtc_memory.append(dtc_code)
            print(f"DTC LOGGED: {dtc_code}")