import re
import csv
from collections import Counter
import matplotlib.pyplot as plt


def extraire_ips(fichier_log):
    no_ips = []
    yes_ips = []

    with open(fichier_log, 'r') as f:
        for line in f:
            if "Failed password" in line:
                match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
                if match:
                    no_ips.append(match.group(1))
            elif "Accepted password" in line:
                match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
                if match:
                    yes_ips.append(match.group(1))
    
    return Counter(no_ips), Counter(yes_ips)

def afficher_comparaison(no_counter, yes_counter, top_n=5):
    top_failed = no_counter.most_common(top_n)
    ips = [ip for ip, _ in top_failed]
    
    no_counts = [no_counter.get(ip, 0) for ip in ips]
    yes_counts = [yes_counter.get(ip, 0) for ip in ips]

    bar_width = 0.35
    x = range(len(ips))

    plt.figure(figsize=(10, 6))
    plt.bar(x, no_counts, width=bar_width, color='red', label='Échecs')
    plt.bar([i + bar_width for i in x], yes_counts, width=bar_width, color='green', label='Réussites')

    plt.xlabel('Adresse IP')
    plt.ylabel('Nombre de connexions')
    plt.title('Echecs vs Reussites')
    plt.xticks([i + bar_width / 2 for i in x], ips, rotation=30)
    plt.legend()
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

def exporter_csv(no_counter, yes_counter, nom_fichier="result.csv"):
    all_ips = set(no_counter.keys()).union(yes_counter.keys())

    with open(nom_fichier, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["IP", "Echecs", "Reussites"])
        for ip in all_ips:
            writer.writerow([ip, no_counter.get(ip, 0), yes_counter.get(ip, 0)])

if __name__ == "__main__":
    log_path = "auth.log"
    failed, accepted = extraire_ips(log_path)
    afficher_comparaison(failed, accepted)
    exporter_csv(failed, accepted, nom_fichier="result.csv")
