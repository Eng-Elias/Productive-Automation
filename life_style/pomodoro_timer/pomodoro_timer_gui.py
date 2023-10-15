import tkinter as tk
from tkinter import messagebox


class PomodoroTimer:
    WORK_TIME = 25 * 60  # 25 minutes
    BREAK_TIME = 5 * 60  # 5 minutes

    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")
        self.working = False
        self.remaining_time = 0

        self.root.geometry("600x400")

        self.bg_color = "#F0F0F0"  # Light grey
        self.button_bg_color = "#00ce07"  # Green
        self.label_fg_color = "#333333"  # Dark grey
        self.font_style = ("Helvetica", 24)

        self.root.configure(bg=self.bg_color)

        self.label = tk.Label(
            root,
            text="",
            font=self.font_style,
            fg=self.label_fg_color,
            bg=self.bg_color,
        )
        self.label.pack(pady=20)

        self.canvas = tk.Canvas(root, width=200, height=200, bg=self.bg_color)
        self.canvas.pack()

        self.start_button = tk.Button(
            root,
            text="Start",
            command=self.start_work_timer,
            font=self.font_style,
            bg=self.button_bg_color,
            fg="white",
        )
        self.start_button.pack(pady=10, side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(
            root,
            text="Reset",
            command=self.reset_timer,
            state="disabled",
            font=self.font_style,
            bg=self.button_bg_color,
            fg="white",
        )
        self.reset_button.pack(pady=10, side=tk.RIGHT, padx=10)

    def start_work_timer(self):
        self.working = True
        self.remaining_time = self.WORK_TIME
        self.start_timer()

    def start_break_timer(self):
        self.working = False
        self.remaining_time = self.BREAK_TIME
        self.start_timer()

    def start_timer(self):
        self.start_button["state"] = "disabled"
        self.reset_button["state"] = "normal"
        if self.working:
            self.run_work_timer()
        else:
            self.run_break_timer()

    def run_work_timer(self):
        if self.working and self.remaining_time >= 0:
            minutes = self.remaining_time // 60
            seconds = self.remaining_time % 60
            self.label.config(text=f"Work Time: {minutes:02d}:{seconds:02d}")
            self.draw_pie_chart(self.remaining_time)
            self.remaining_time -= 1
            self.root.after(1000, self.run_work_timer)
        elif self.remaining_time < 0 and self.working:
            self.working = False
            messagebox.showinfo("Pomodoro Timer", "Time for a break!")
            self.start_break_timer()

    def run_break_timer(self):
        if not self.working and self.remaining_time >= 0:
            minutes = self.remaining_time // 60
            seconds = self.remaining_time % 60
            self.label.config(text=f"Break Time: {minutes:02d}:{seconds:02d}")
            self.draw_pie_chart(self.remaining_time)
            self.remaining_time -= 1
            self.root.after(1000, self.run_break_timer)
        elif self.remaining_time < 0 and not self.working:
            self.reset_timer()

    def draw_pie_chart(self, remaining_time):
        self.canvas.delete("pie_chart")

        radius = 80
        center_x, center_y = 100, 100
        self.canvas.create_oval(
            center_x - radius,
            center_y - radius,
            center_x + radius,
            center_y + radius,
            outline="black",
        )

        total_time = self.WORK_TIME if self.working else self.BREAK_TIME
        progress_angle = (remaining_time / total_time) * 360

        if self.working:
            color = "blue"
        else:
            color = "#00ff00"

        self.canvas.create_arc(
            center_x - radius,
            center_y - radius,
            center_x + radius,
            center_y + radius,
            start=0,
            extent=progress_angle,
            fill=color,
            outline="black",
            tags="pie_chart",
        )

    def reset_timer(self):
        self.working = False
        self.start_button["state"] = "normal"
        self.reset_button["state"] = "disabled"
        self.label.config(text="")
        self.canvas.delete("pie_chart")
        messagebox.showinfo("Pomodoro Timer", "Timer reset.")
        self.remaining_time = 0


if __name__ == "__main__":
    root = tk.Tk()
    timer = PomodoroTimer(root)
    root.mainloop()
