import re
from collections import Counter
import matplotlib.pyplot as plt

def extraire_ips_echouees(fichier_log):
    failed_ips = []
    with open(fichier_log, 'r') as f:
        for line in f:
            if "Failed password" in line:
                match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
                if match:
                    failed_ips.append(match.group(1))
    return Counter(failed_ips)

def afficher_graphique(counter, top_n=5):
    top = counter.most_common(top_n)
    ips = [ip for ip, _ in top]
    counts = [count for _, count in top]

    plt.figure(figsize=(10, 6))
    plt.bar(ips, counts, color='tomato')
    plt.title(f"Top {top_n} IPs avec tentatives SSH échouées")
    plt.xlabel("Adresse IP")
    plt.ylabel("Nombre d'échecs")
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    log_path = "auth.log"
    compteur = extraire_ips_echouees(log_path)
    afficher_graphique(compteur)
