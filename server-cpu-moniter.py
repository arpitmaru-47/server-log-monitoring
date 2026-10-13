import logging 

logging.basicConfig(
    filename="server.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s"
)

servers = [
    {"name": "web-01", "cpu": 45},
    {"name": "web-02", "cpu": 85},
    {"name": "db-01", "cpu": 95}
]

for server in servers:
    name = server["name"]
    cpu = server["cpu"]

    if cpu >= 90:
        logging.error("%s CPU is critical: %s%%", name, cpu)

    elif cpu >= 80:
        logging.warning("%s CPU is high: %s%%", name, cpu)

    else:
        logging.info("%s CPU is normal: %s%%", name, cpu)

print("Monitoring completed. Check server.log")