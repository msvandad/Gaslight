# Gaslight
A very basic nozzle dimension calculator for cold gas thrusters

Gaslight is a basic nozzle dimension calculator for cold gas thrusters. It allows you to calculate the throat and exit radii of a nozzle based on desired thrust, chamber pressure, chamber temperature, and environment pressure.

## Features

- Interactive selection of gas type from a predefined list.
- Calculation of nozzle dimensions using specific gas properties.
- User-friendly console interface powered by the `rich` library.

## Installation

To use this project, you need to have Python installed along with the required dependencies. You can install the dependencies using:

```bash
pip install -r requirements.txt
```

## Usage

Run the script using Python or `uv`:

```bash
uv run gaslight.py
```

Or, you can use the traditional Python command:

```bash
python gaslight.py
```

Follow the prompts to:

1. Select a gas by its identifier (e.g., `G-N2`).
2. Enter the desired thrust in newtons.
3. Enter the chamber pressure in pascals.
4. Enter the chamber temperature in Kelvin.
5. Enter the environment pressure in pascals.

The program will then calculate and display the throat and exit radii of the nozzle.

## Dependencies

- `rich==13.9.4`: For creating interactive console applications with styled text and tables.

## License

This project is licensed under the MIT License.
