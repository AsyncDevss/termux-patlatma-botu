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
🚀 Botu Başlatmamain.py dosyasını açın ve TOKEN = "BOT_TOKENINIZI_BURAYA_YAZIN" kısmına Discord Developer Portal'dan aldığınız bot tokenini yapıştırın.Discord Developer Portal üzerinden botunuzun "Message Content Intent" ayarını aktif ettiğinizden emin olun.Termux terminaline şu komutu yazarak botu çalıştırın:Bashpython main.py
📋 Bot KomutlarıBot içerisindeki tüm komutlar varsayılan olarak ! prefixi ile çalışır:KomutKullanımAçıklama!spam!spam <yazı>Belirtilen metni kanala hızlı bir şekilde spamlar.!kanallar!kanallar <isim>Belirtilen isimde ve numaralandırılmış şekilde hızlıca metin kanalları açar.!roller!roller <isim>Belirtilen isimde hızlıca roller oluşturur.
