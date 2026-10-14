import os
import sys
import hashlib
import tkinter as tk
from pathlib import Path
from tkinter import messagebox, simpledialog

from lli import InputVaultApp

BG = "#0B1424"
PANEL = "#172940"
BLUE = "#72CFFF"
WHITE = "#FFFFFF"
MUTED = "#B7C8DC"


def desktop_path():
    if sys.platform == "win32":
        import ctypes
        from ctypes import wintypes

        path = ctypes.create_unicode_buffer(wintypes.MAX_PATH)
        result = ctypes.windll.shell32.SHGetFolderPathW(
            None, 0x10, None, 0, path
        )
        if result == 0:
            return Path(path.value)

    return Path.home() / "Desktop"


def open_input_proof():
    try:
        window = tk.Toplevel(root)
        InputVaultApp(window)
    except Exception as exc:
        messagebox.showerror("LLI - Input Proof", str(exc), parent=root)


def open_hash_checker():
    folder = desktop_path() / "input_proof"

    if not folder.is_dir():
        messagebox.showerror(
            "SHA-256 Checker",
            f"Input proof folder not found:\n{folder}",
            parent=root
        )
        return

    try:
        files = sorted(
            folder.glob("*.txt"),
            key=lambda item: item.stat().st_mtime,
            reverse=True
        )
        if not files:
            messagebox.showerror(
                "SHA-256 Checker",
                f"No .txt proof files found in:\n{folder}",
                parent=root
            )
            return

        file = files[0]
        text = file.read_text(encoding="utf-8-sig")
        text = text.replace("\r\n", "\n").replace("\r", "\n")

        marker = "-" * 68 + "\n"
        index = text.rfind(marker)
        if index < 0:
            raise ValueError("Proof footer not found in " + file.name)

        payload = text[:index]
        actual = hashlib.sha256(payload.encode("utf-8")).hexdigest()

        expected = simpledialog.askstring(
            "SHA-256 Checker",
            f"Checking newest proof file:\n{file.name}\n\n"
            "Enter the expected SHA-256 hash:",
            parent=root
        )

        if expected is None:
            return

        expected = expected.strip().lower()

        if len(expected) != 64 or any(
            char not in "0123456789abcdef" for char in expected
        ):
            messagebox.showwarning(
                "SHA-256 Checker",
                "Enter exactly 64 hexadecimal characters.",
                parent=root
            )
        elif actual == expected:
            messagebox.showinfo(
                "SHA-256 Checker",
                f"CORRECT: SHA-256 matches.\n\nFile: {file.name}",
                parent=root
            )
        else:
            messagebox.showerror(
                "SHA-256 Checker",
                f"INCORRECT: SHA-256 does not match.\n\n"
                f"File: {file.name}\n\nCalculated hash:\n{actual}",
                parent=root
            )

    except Exception as exc:
        messagebox.showerror(
            "SHA-256 Checker",
            str(exc),
            parent=root
        )


root = tk.Tk()
root.title("LLI - Locked Legit Inputs")
root.geometry("520x480")
root.resizable(False, False)
root.configure(bg=BG)

try:
    icon = Path(getattr(sys, "_MEIPASS", Path(__file__).parent))
    root.iconbitmap(str(icon / "LLI_logo.ico"))
except Exception:
    pass

header = tk.Frame(root, bg=BG)
header.pack(pady=(28, 8))

tk.Label(
    header, text="LLI", font=("Segoe UI", 30, "bold"),
    fg=BLUE, bg=BG
).pack()

tk.Label(
    root, text="LOCKED LEGIT INPUTS",
    font=("Segoe UI", 10, "bold"), fg=BLUE, bg=BG
).pack(pady=(0, 8))

tk.Label(
    root, text="Your gameplay input verification toolkit.",
    font=("Segoe UI", 10), fg=MUTED, bg=BG
).pack(pady=(0, 24))


def make_button(title, subtitle, command):
    button = tk.Button(
        root, text=f"{title}\n{subtitle}",
        command=command,
        font=("Segoe UI", 12, "bold"),
        fg=WHITE, bg=PANEL,
        activebackground="#244565",
        activeforeground=WHITE,
        relief="flat", bd=0,
        cursor="hand2",
        justify="left", anchor="w",
        padx=22, pady=15
    )
    button.pack(fill="x", padx=42, pady=7)


make_button(
    "Input Proof",
    "Record and export keyboard and mouse logs",
    open_input_proof
)

make_button(
    "SHA-256 Checker",
    "Check proof-file hashes",
    open_hash_checker
)

tk.Label(
    root, text="LLI  -  INPUT VERIFICATION TOOLKIT",
    font=("Segoe UI", 8), fg="#8295AD", bg=BG
).pack(side="bottom", pady=18)

root.mainloop()
