import time
import sys

def print_slow(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    print()

class Game:
    def __init__(self):
        self.day = 1
        self.sanity = 100
        self.caffeine = 50
        self.code_quality = 50
        self.deadline_progress = 0

    def check_status(self):
        print("\n📊 STATUS ANDA:")
        print(f"🧠 Sanity (Kewarasan): {self.sanity}%")
        print(f"☕ Caffeine Level     : {self.caffeine}%")
        print(f"💻 Code Quality      : {self.code_quality}%")
        print(f"🚀 Progress Aplikasi : {self.deadline_progress}/100")
        print("-" * 30)

    def is_game_over(self):
        if self.sanity <= 0:
            print_slow("\n💀 GAME OVER: Anda mengalami Burnout parah dan mengunduh LinkedIn di tengah malam.")
            return True
        if self.code_quality <= 0:
            print_slow("\n💀 GAME OVER: Kode Anda terlalu berantakan. Server production meledak dan Anda dipecat.")
            return True
        if self.day > 5 and self.deadline_progress < 100:
            print_slow("\n⏰ GAME OVER: Hari Jumat tiba dan aplikasi belum selesai. Klien mengamuk!")
            return True
        if self.deadline_progress >= 100:
            print_slow("\n🎉 VICTORY! Aplikasi berhasil rilis tepat waktu tanpa bug fatal. Anda adalah Legend!")
            return True
        return False

    def play_day(self):
        print_slow(f"\n📆 --- HARI KE-{self.day} ---")
        self.check_status()

        if self.day == 1:
            print("Skenario: Klien tiba-tiba meminta fitur baru yang tidak ada di kontrak.")
            print("1. Tolak mentah-mentah demi kesehatan mental. (Sanity +20, Progress +0)")
            print("2. Terima dan lembur semalaman. (Sanity -30, Progress +30, Caffeine -20)")
        elif self.day == 2:
            print("Skenario: Kode Anda mengalami error misterius yang hanya muncul di komputer Anda.")
            print("1. Salin solusi dari StackOverflow tanpa dibaca. (Code Quality -20, Progress +25)")
            print("2. Lakukan debugging pelan-pelan sambil minum kopi. (Caffeine +20, Progress +15, Code Quality +10)")
        elif self.day == 3:
            print("Skenario: Rekan kerja Anda tidak sengaja melakukan 'git push --force' ke branch utama.")
            print("1. Marah-marah di grup Slack kantor. (Sanity -15, Code Quality -10)")
            print("2. Tetap tenang, seduh kopi hitam, dan perbaiki manual. (Caffeine -10, Code Quality +20, Progress +10)")
        elif self.day == 4:
            print("Skenario: Besok deadline, tapi tim QA menemukan 50 bug baru.")
            print("1. Tandai semua bug sebagai 'Bukan bug, tapi fitur'. (Code Quality -30, Progress +30)")
            print("2. Begadang semalaman suntuk memperbaikinya. (Sanity -40, Caffeine -30, Progress +25, Code Quality +25)")
        elif self.day == 5:
            print("Skenario: Hari terakhir! Sisa sedikit lagi untuk deploy ke production.")
            print("1. Lewati proses testing, langsung push ke server! (Progress +20, Code Quality -20)")
            print("2. Lakukan testing terakhir dengan hati-hati. (Progress +10, Sanity -10, Code Quality +15)")

        choice = input("\nPilih tindakan Anda (1 atau 2): ")
        
        # Logika konsekuensi pilihan
        if self.day == 1:
            if choice == "1": self.sanity += 20
            else: self.sanity -= 30; self.deadline_progress += 30; self.caffeine -= 20
        elif self.day == 2:
            if choice == "1": self.code_quality -= 20; self.deadline_progress += 25
            else: self.caffeine += 20; self.deadline_progress += 15; self.code_quality += 10
        elif self.day == 3:
            if choice == "1": self.sanity -= 15; self.code_quality -= 10
            else: self.caffeine -= 10; self.code_quality += 20; self.deadline_progress += 10
        elif self.day == 4:
            if choice == "1": self.code_quality -= 30; self.deadline_progress += 30
            else: self.sanity -= 40; self.caffeine -= 30; self.deadline_progress += 25; self.code_quality += 25
        elif self.day == 5:
            if choice == "1": self.deadline_progress += 20; self.code_quality -= 20
            else: self.deadline_progress += 10; self.sanity -= 10; self.code_quality += 15

        # Batasi nilai maksimal 100 dan minimal 0
        self.sanity = max(0, min(100, self.sanity))
        self.caffeine = max(0, min(100, self.caffeine))
        self.code_quality = max(0, min(100, self.code_quality))

        self.day += 1

    def start(self):
        print_slow("💻 SELAMAT DATANG DI SENIOR DEVELOPER SIMULATOR 💻")
        print_slow("Misi Anda: Selesaikan aplikasi sebelum hari Jumat berakhir!")
        
        while not self.is_game_over():
            self.play_day()

if __name__ == "__main__":
    game = Game()
    game.start()
