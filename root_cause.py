import psutil

def find_root_cause():

    processes = []

    for proc in psutil.process_iter(['pid','name','cpu_percent','memory_percent']):
        try:
            processes.append(proc.info)
        except:
            pass

    # sort processes by highest CPU usage
    processes = sorted(processes, key=lambda x: x['cpu_percent'], reverse=True)

    if processes:
        top = processes[0]

        cause = {
            "process": top['name'],
            "pid": top['pid'],
            "cpu": top['cpu_percent'],
            "memory": top['memory_percent']
        }

        return cause

    return None