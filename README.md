# 🚀 Termux Python Discord Gelişmiş Altyapı

Bu altyapı, Termux üzerinde Python (`discord.py`) kullanılarak stabil ve hafif çalışacak şekilde tasarlanmıştır. Sunucu yönetimi, test ve otomasyon işlemlerini hızlıca yapmanızı sağlar.

---

## 🛠️ Termux Kurulum Adımları

Botu Termux üzerinde çalıştırmak için sırasıyla aşağıdaki komutları terminale yapıştırın:

```bash
# Sistem paketlerini güncelleyin
pkg update && pkg upgrade -y

# Python dilini kurun
pkg install python -y

# Bot için bir klasör oluşturun ve içine girin
mkdir python-bot && cd python-bot

# Gerekli Discord kütüphanesini kurun
pip install discord.py
