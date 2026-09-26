from datetime import datetime
from rich.console import Console


console = Console()
def get_employees():
    today=datetime.now().strftime("%d.%m.%y")
    console.print(f"[bold blue][{today}][/] Список сотрудников получен")