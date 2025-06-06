import psutil
import time
import os
import sys
import platform
from inputimeout import inputimeout


class Logger:
    def __init__(self, fichier_log_txt):
        self.terminal = sys.stdout
        self.log = open(fichier_log_txt, "w", encoding="utf-8")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        self.terminal.flush()
        self.log.flush()

sys.stdout = Logger("resultat.txt")


def afficher_barre(valeur, longueur=50):
    barre_pleine = int(valeur / 100 * longueur)
    barre = '█' * barre_pleine + '-' * (longueur - barre_pleine)
    return f"[{barre}] {valeur:5.1f}%"


def clear_screen():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def display_dashboard():
    while True:
        clear_screen()

        print("-------------")
        print("Infos système")
        print("-------------")

        print("\nUtilisation CPU\n")
        print(f"Total CPU : {psutil.cpu_percent()} %")
        for i, pourcentage in enumerate(psutil.cpu_percent(percpu=True)):
            print(f"CPU {i:>2}: {afficher_barre(pourcentage)}")
            print(f"CPU coeur {i} : {pourcentage} %\n")


        print("\nTempérature CPU\n")

        """
        print("Utilisation du CPU (ASCII) :\n")
        cpu_par_coeur = psutil.cpu_percent(percpu=True)
        for i, pourcentage in enumerate(cpu_par_coeur):
            print(f"CPU {i:>2}: {afficher_barre(pourcentage)} \n\n")
        """
        #temperature = psutil.sensors_temperatures() 
        #print(temperature)
        """
        psutil.sensors_temperatures() est unique à Linux et ne contionne donc pas pour moi
        solution avec hwmonitor (librairie wmi) et openhardwaremonitor (https://openhardwaremonitor.org/downloads/)
        """

        import wmi
        w = wmi.WMI(namespace="root\OpenHardwareMonitor")
        temperature_infos = w.Sensor()
        for sensor in temperature_infos:
            if sensor.SensorType==u'Temperature':
                print(sensor.Name)
                print(sensor.Value)


        print("\nMémoire RAM\n")
        mem = psutil.virtual_memory()
        print(f"Totale : {round(mem.total / (1024**3), 2)} GB")
        print(f"Utilisée : {round(mem.used / (1024**3), 2)} GB")
        print(f"Libre : {round(mem.available / (1024**3), 2)} GB")

        print("\nUtilisation Disque\n")
        for part in psutil.disk_partitions():
            try:
                usage = psutil.disk_usage(part.mountpoint)
                print(f"{part.mountpoint} : {usage.percent}% utilisé")
            except PermissionError:
                continue

        print("\nActivité Réseau\n")
        net = psutil.net_io_counters()
        print(f"Envoyés: {net.bytes_sent / (1024**2):.2f} MB")
        print(f"Reçus: {net.bytes_recv / (1024**2):.2f} MB")

        print("\nStatistiques Réseau par interface\n")
        net_if = psutil.net_io_counters(pernic=True)
        for interface, stats in net_if.items():
            print(f"{interface} : Envoyés: {stats.bytes_sent / (1024**2):.2f} MB | Reçus: {stats.bytes_recv / (1024**2):.2f} MB")


        print("\nTapez 'quit' pour quitter.")
        try:
            user_input = inputimeout(timeout=5).strip().lower()
            if user_input == "quit":
                break
            else:
                time.sleep(1)
        except:
            pass

with open("result.txt", "w") as f:
    try:
        display_dashboard()
    except KeyboardInterrupt:
        print("\nArrêt manuel par l'utilisateur.")
