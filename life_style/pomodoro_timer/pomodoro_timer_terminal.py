from enum import Enum
import time
import sys
import os
import keyboard


class TimerType(Enum):
    WORK = "Work"
    BREAK = "Break"


class Option(Enum):
    START_BREAK = "Start Break"
    RESET = "Reset"
    EXIT = "Exit"


class Key(Enum):
    UP = "up"
    DOWN = "down"
    ENTER = "enter"


class PomodoroTimer:
    WORK_TIME = 25 * 60  # 25 minutes
    BREAK_TIME = 5 * 60  # 5 minutes

    def __init__(self):
        self.working = False
        self.remaining_time = 0

    def start_timer(self, timer_type):
        if timer_type == TimerType.WORK:
            self.remaining_time = self.WORK_TIME
        else:
            self.remaining_time = self.BREAK_TIME

        print(f"{timer_type.value} timer started.")
        while self.remaining_time >= 0:
            self.clear_terminal()
            minutes = self.remaining_time // 60
            seconds = self.remaining_time % 60
            print(f"Time: {minutes:02d}:{seconds:02d}")
            sys.stdout.flush()
            self.remaining_time -= 1
            time.sleep(1)
        if timer_type == TimerType.WORK:
            print(f"\nTime for a {timer_type.value.lower()}!")
            self.ask_user_for_option_after_work()
        else:
            self.ask_user_for_option_after_break()

    def ask_user_for_option_after_work(self):
        options = {Option.START_BREAK: TimerType.BREAK, Option.RESET: TimerType.WORK}

        self.ask_user_for_option(options)

    def ask_user_for_option_after_break(self):
        options = {Option.RESET: TimerType.WORK, Option.EXIT: None}

        self.ask_user_for_option(options)

    def ask_user_for_option(self, options):
        option_idx = 0
        option_keys = list(options.keys())

        while True:
            self.clear_terminal()
            print("Choose an option:")
            for i, key in enumerate(option_keys):
                option = options[key]
                if i == option_idx:
                    print(f"> {key.value}")
                else:
                    print(f"  {key.value}")

            key_event = keyboard.read_event(suppress=True)

            if key_event.event_type == keyboard.KEY_DOWN:
                if (
                    key_event.name == Key.DOWN.value
                    and option_idx < len(option_keys) - 1
                ):
                    option_idx += 1
                elif key_event.name == Key.UP.value and option_idx > 0:
                    option_idx -= 1
                elif key_event.name == Key.ENTER.value:
                    break

        selected_option = option_keys[option_idx]
        if selected_option in options:
            next_timer_type = options[selected_option]
            if next_timer_type:
                self.start_timer(next_timer_type)
            else:
                sys.exit()

    def reset_timer(self):
        self.working = False
        print("Timer reset.")
        self.remaining_time = 0

    def clear_terminal(self):
        if os.name == "posix":
            os.system("clear")  # For UNIX/Linux/MacOS
        elif os.name == "nt":
            os.system("cls")  # For Windows


if __name__ == "__main__":
    timer = PomodoroTimer()
    timer.start_timer(TimerType.WORK)
