import psutil

def triger_temp():
    temps = psutil.sensors_temperatures()
    if temps:
        for _, entries in temps.items():
            for entry in entries:
                if entry.current > 75:
                    return True
                else: return False
        

def sensor_temp():
    temps = psutil.sensors_temperatures()
    result = ""
    if not temps:
        return "Не могу считать температуру"
    for name, entries in temps.items():
        result += name
        for entry in entries:
            result += "\n    %-20s %s °C (high = %s °C, critical = %s °C)" % (
                entry.label or name, entry.current, entry.high,
                entry.critical)
        result += "\n"
    return result

if __name__ == '__main__':
    print(triger_temp())