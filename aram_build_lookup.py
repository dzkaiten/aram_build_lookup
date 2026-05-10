import tkinter as tk
from tkinter import ttk
import subprocess
import os

current_theme = "league"

def open_builds():
    champion = entry.get().strip().lower()
    
    if not champion or champion == "enter champion name...":
        status_label.config(text="⚠️ Please enter a champion name!")
        apply_theme_colors()
        return
    
    # Format champion name with hyphens for multi-word champions
    champion_formatted = champion.replace(" ", "-")
    
    ugg_url = f"https://u.gg/lol/champions/aram/{champion_formatted}-aram"
    
    # Toggle between mayhem and aram modes
    if mayhem_mode.get():
        metasrc_url = f"https://www.metasrc.com/lol/mayhem/build/{champion_formatted}?ranks=diamond,master,grandmaster,challenger"
    else:
        metasrc_url = f"https://www.metasrc.com/lol/aram/build/{champion_formatted}?ranks=diamond,master,grandmaster,challenger"
    
    chrome_paths = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        os.path.expanduser(r"~\AppData\Local\Google\Chrome\Application\chrome.exe")
    ]
    
    chrome_path = None
    for path in chrome_paths:
        if os.path.exists(path):
            chrome_path = path
            break
    
    if chrome_path:
        # Open tabs in current window (no --new-window flag)
        subprocess.Popen([chrome_path, ugg_url])
        subprocess.Popen([chrome_path, metasrc_url])
        mode_text = "Mayhem" if mayhem_mode.get() else "ARAM"
        status_label.config(text=f"✓ Opening {mode_text} builds for {champion.title()}...")
        apply_theme_colors()
    else:
        status_label.config(text="❌ Chrome not found!")
        apply_theme_colors()
    
    entry.delete(0, tk.END)
    entry.insert(0, "Enter champion name...")
    entry.config(foreground=themes[current_theme]["placeholder"])

def on_enter(event):
    open_builds()

def on_focus_in(event):
    if entry.get() == "Enter champion name...":
        entry.delete(0, tk.END)
        entry.config(foreground=themes[current_theme]["entry_fg"])

def on_focus_out(event):
    if entry.get() == "":
        entry.insert(0, "Enter champion name...")
        entry.config(foreground=themes[current_theme]["placeholder"])

def change_theme(theme_name):
    global current_theme
    current_theme = theme_name
    apply_theme()

def apply_theme():
    theme = themes[current_theme]
    
    root.configure(bg=theme["bg"])
    main_frame.config(bg=theme["bg"])
    
    title_label.config(
        text=theme["title"],
        font=theme["title_font"],
        bg=theme["bg"],
        fg=theme["title_fg"]
    )
    
    subtitle_label.config(
        text=theme["subtitle"],
        font=theme["subtitle_font"],
        bg=theme["bg"],
        fg=theme["subtitle_fg"]
    )
    
    entry.config(
        font=theme["entry_font"],
        bg=theme["entry_bg"],
        fg=theme["entry_fg"] if entry.get() != "Enter champion name..." else theme["placeholder"],
        insertbackground=theme["cursor"],
        relief="flat",
        borderwidth=0
    )
    
    style.configure("Custom.TButton",
                    font=theme["button_font"],
                    background=theme["button_bg"],
                    foreground=theme["button_fg"],
                    borderwidth=0,
                    focuscolor="none")
    
    search_button.config(style="Custom.TButton")
    
    status_label.config(
        bg=theme["bg"],
        fg=theme["status_fg"],
        font=theme["status_font"]
    )
    
    # Mayhem checkbox styling
    mayhem_check.config(
        bg=theme["bg"],
        fg=theme["subtitle_fg"],
        selectcolor=theme["entry_bg"],
        activebackground=theme["bg"],
        activeforeground=theme["title_fg"]
    )
    
    theme_menu_frame.config(bg=theme["bg"])
    theme_label.config(bg=theme["bg"], fg=theme["subtitle_fg"])
    
    # Update theme buttons
    for btn_name, btn in theme_buttons.items():
        if btn_name == current_theme:
            btn.config(
                bg=theme["button_bg"],
                fg=theme["button_fg"],
                font=("Segoe UI", 8, "bold")
            )
        else:
            btn.config(
                bg=theme["entry_bg"],
                fg=theme["subtitle_fg"],
                font=("Segoe UI", 8)
            )

def apply_theme_colors():
    # Re-apply colors for status messages
    theme = themes[current_theme]
    if "⚠️" in status_label.cget("text") or "❌" in status_label.cget("text"):
        status_label.config(fg="#ff6b6b")
    elif "✓" in status_label.cget("text"):
        status_label.config(fg="#51cf66")
    else:
        status_label.config(fg=theme["status_fg"])

# Theme definitions
themes = {
    "dark_modern": {
        "title": "⚔️ ARAM BUILD LOOKUP",
        "title_font": ("Segoe UI", 20, "bold"),
        "title_fg": "#7aa2f7",
        "subtitle": "Find the best builds for your champion",
        "subtitle_font": ("Segoe UI", 9),
        "subtitle_fg": "#9aa5ce",
        "bg": "#1a1b26",
        "entry_bg": "#24283b",
        "entry_fg": "#f8f9fa",
        "entry_font": ("Segoe UI", 14),
        "placeholder": "#868e96",
        "cursor": "#7aa2f7",
        "button_bg": "#7aa2f7",
        "button_fg": "white",
        "button_font": ("Segoe UI", 11, "bold"),
        "status_fg": "#9aa5ce",
        "status_font": ("Segoe UI", 9)
    },
    "league": {
        "title": "ARAM BUILD LOOKUP",
        "title_font": ("Arial", 22, "bold"),
        "title_fg": "#c8aa6e",
        "subtitle": "Dominate the Howling Abyss",
        "subtitle_font": ("Arial", 9, "italic"),
        "subtitle_fg": "#785a28",
        "bg": "#010a13",
        "entry_bg": "#0a1428",
        "entry_fg": "#c8aa6e",
        "entry_font": ("Arial", 14),
        "placeholder": "#5a4a28",
        "cursor": "#c8aa6e",
        "button_bg": "#c8aa6e",
        "button_fg": "#010a13",
        "button_font": ("Arial", 11, "bold"),
        "status_fg": "#785a28",
        "status_font": ("Arial", 9)
    },
    "minimal": {
        "title": "ARAM Build Lookup",
        "title_font": ("Segoe UI", 20, "bold"),
        "title_fg": "#2c3e50",
        "subtitle": "Quick champion build search",
        "subtitle_font": ("Segoe UI", 9),
        "subtitle_fg": "#7f8c8d",
        "bg": "#ffffff",
        "entry_bg": "#f8f9fa",
        "entry_fg": "#2c3e50",
        "entry_font": ("Segoe UI", 14),
        "placeholder": "#95a5a6",
        "cursor": "#3498db",
        "button_bg": "#3498db",
        "button_fg": "white",
        "button_font": ("Segoe UI", 11),
        "status_fg": "#7f8c8d",
        "status_font": ("Segoe UI", 9)
    },
    "cyberpunk": {
        "title": "⚡ ARAM BUILD LOOKUP ⚡",
        "title_font": ("Consolas", 18, "bold"),
        "title_fg": "#00ff9f",
        "subtitle": ">> JACK INTO THE RIFT <<",
        "subtitle_font": ("Consolas", 9),
        "subtitle_fg": "#ff006e",
        "bg": "#0f0f23",
        "entry_bg": "#1a1a3e",
        "entry_fg": "#00ff9f",
        "entry_font": ("Consolas", 14),
        "placeholder": "#4a4a6e",
        "cursor": "#ff006e",
        "button_bg": "#ff006e",
        "button_fg": "#0f0f23",
        "button_font": ("Consolas", 11, "bold"),
        "status_fg": "#00d9ff",
        "status_font": ("Consolas", 9)
    }
}

# Create main window
root = tk.Tk()
root.title("ARAM Build Lookup")
root.geometry("500x420")
root.resizable(False, False)

# Create mayhem_mode variable AFTER root window
mayhem_mode = tk.BooleanVar(value=True)

style = ttk.Style()
style.theme_use('clam')

# Create widgets
main_frame = tk.Frame(root)
main_frame.pack(expand=True, fill="both", padx=30, pady=20)

title_label = tk.Label(main_frame)
title_label.pack(pady=(0, 5))

subtitle_label = tk.Label(main_frame)
subtitle_label.pack(pady=(0, 20))

entry_frame = tk.Frame(main_frame)
entry_frame.pack(pady=10)

entry = tk.Entry(entry_frame, width=25)
entry.insert(0, "Enter champion name...")
entry.bind('<Return>', on_enter)
entry.bind('<FocusIn>', on_focus_in)
entry.bind('<FocusOut>', on_focus_out)
entry.pack(ipady=10, pady=5)

# Mayhem mode checkbox
mayhem_check = tk.Checkbutton(
    main_frame,
    text="🔥 Mayhem Mode",
    variable=mayhem_mode,
    font=("Segoe UI", 10),
    cursor="hand2"
)
mayhem_check.pack(pady=5)

search_button = ttk.Button(main_frame, text="Search Builds", command=open_builds)
search_button.pack(pady=15, ipadx=20, ipady=5)

status_label = tk.Label(main_frame, text="")
status_label.pack(pady=5)

# Theme selector
theme_menu_frame = tk.Frame(main_frame)
theme_menu_frame.pack(pady=15)

theme_label = tk.Label(theme_menu_frame, text="Theme:", font=("Segoe UI", 9))
theme_label.pack(side=tk.LEFT, padx=5)

theme_buttons = {}
theme_names = {
    "dark_modern": "Dark",
    "league": "LoL",
    "minimal": "Light",
    "cyberpunk": "Cyber"
}

for theme_key, theme_display in theme_names.items():
    btn = tk.Button(
        theme_menu_frame,
        text=theme_display,
        command=lambda t=theme_key: change_theme(t),
        relief="flat",
        padx=10,
        pady=5,
        cursor="hand2"
    )
    btn.pack(side=tk.LEFT, padx=2)
    theme_buttons[theme_key] = btn

# Apply initial theme
apply_theme()
entry.focus()
root.mainloop()