# Importing required libraries
import requests  # For making HTTP requests to the weather API
from rich.console import Console  # To create rich terminal output
from rich.panel import Panel  # To display bordered panels
from rich.prompt import Prompt  # For styled user input prompt
from rich import box  # Provides different box styles for panels

# Create a Console object for styled printing
console = Console()

# Define the weather-fetching function
def get_weather(location=""):
    # Create the URL dynamically based on the location
    url = f"https://wttr.in/{location}?format=3"  # Format 3 gives a one-line summary

    try:
    # send HTTP GET request to the wrrt.in API
        response = requests.get(url)
        weather = response.text.strip() # Remove leading/trailing whitespace

    # Print weather in a styled panel using rich

        console.print(Panel.fit(
        f"[bold blue]📍 Weather Report[/bold blue]\n\n[green]{weather}[/green]",
            box=box.DOUBLE,  # Fancy double-line box
            border_style="bright_magenta",  # Border color
            padding=(1, 4),  # Space inside the panel (top/bottom, left/right)
        ))


    except Exception as e:
    # Print error message in red if request fails
        console.print(f"[bold red]⚠️ Error fetching weather:[/bold red] {e}")

# Main entry point of the program
if __name__ == "__main__":
    # Welcome panel displayed at startup
    console.print(Panel.fit(
        "[bold cyan]🌤️ Welcome to the Stylish Weather CLI App 🌤️[/bold cyan]",
        border_style="bold blue",  # Border color
        box=box.ROUNDED  # Use rounded corners for this panel
    ))

 # Prompt user for city input (or leave blank to use IP-based location)
    user_location = Prompt.ask("[yellow]Enter your city (or leave blank for current location)[/yellow]")
    
    # Call the weather function with the user input (trimmed of whitespace)
    get_weather(user_location.strip())






# command to run this project: uv run python src/weather_cli/main.py
