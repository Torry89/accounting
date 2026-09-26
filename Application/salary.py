from datetime import datetime
from rich.console import Console

console = Console()
def calculate_salary():
    today=datetime.now().strftime("%d.%m.%y")
    console.print(f"[bold green][{today}][/] зарплата посчитана")
