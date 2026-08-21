from rich.console import Console
from rich.panel import Panel
from rich.text import Text

# Инициализируем консоль один раз внутри модуля
_console = Console()


def log_connection(client_address, method: str, path: str, user_agent: str):
    # Фигня это чисто для вайба блять!
    log_text = Text()

    log_text.append("IP/Port: ", style="bold white")
    log_text.append(f"{client_address}\n", style="cyan")

    log_text.append("Method:  ", style="bold white")
    method_color = "green" if method == "GET" else "yellow"
    log_text.append(f"{method}\n", style=f"bold {method_color}")

    log_text.append("Path:    ", style="bold white")
    log_text.append(f"{path}\n", style="magenta bold")

    log_text.append("Browser: ", style="bold white")
    log_text.append(f"{user_agent}", style="dim italic white")

    _console.print(
        Panel(
            log_text,
            title="[bold green] NEW CONNECTION [/bold green]",
            border_style="green",
            expand=False
        )
    )


def log_error(message: str, factor: str = ""):
    # И это что бы вайбово ловить ошибки йооо
    if factor:
        _console.print(f"\n[bold red]!!! {message} !!![/bold red] Factor: {factor}\n")
    else:
        _console.print(f"\n[bold red]!!! {message} !!![/bold red]\n")
