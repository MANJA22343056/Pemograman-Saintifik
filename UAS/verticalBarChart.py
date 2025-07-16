import pandas as pd
import matplotlib.pyplot as plt

# membaca DataFrame dari file CSV dengan delimiter ;
# skip baris pertama (header) dan set kolom yang sesuai
df = pd.read_csv(
    "medal.csv",
    sep=";",
    header=None,
    skiprows=1,
    names=["Country", "Code", "Gold", "Silver", "Bronze", "Total"],
)

# filter data untuk hanya negara-negara (bukan total)
df_countries = df[df["Country"] != "Total"]

# ambil kode negara dan kategori medali
codes = df_countries["Code"]
gold = df_countries["Gold"].astype(int)  # Mengonversi ke tipe data integer
silver = df_countries["Silver"].astype(int)
bronze = df_countries["Bronze"].astype(int)

# jumlah negara
num_countries = len(df_countries)

# warna yang akan digunakan untuk kategori medali
colors = ["#FFD700", "#C0C0C0", "#CD7F32"]  # Gold, Silver, Bronze

# plotting
fig, ax = plt.subplots(figsize=(12, 8))

# plot bar untuk setiap negara dan kategori medali
bar_width = 0.2
index = range(num_countries)
for i in index:
    ax.bar(
        i - bar_width,
        gold[i],
        width=bar_width,
        color=colors[0],
        label="Gold" if i == 0 else None,
    )
    ax.bar(
        i,
        silver[i],
        width=bar_width,
        color=colors[1],
        label="Silver" if i == 0 else None,
    )
    ax.bar(
        i + bar_width,
        bronze[i],
        width=bar_width,
        color=colors[2],
        label="Bronze" if i == 0 else None,
    )

# label dan judul
ax.set_xlabel("Country")
ax.set_ylabel("Number of Medals")
ax.set_title("Medals by Country")
ax.set_xticks(index)
ax.set_xticklabels(codes, rotation=45)
ax.legend(["Gold", "Silver", "Bronze"])

plt.tight_layout()
plt.show()
