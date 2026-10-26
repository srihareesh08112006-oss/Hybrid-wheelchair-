# Hybrid Wheelchair

A hybrid manual/electric-assist wheelchair. Pushrim sensors detect the user's effort and a motor controller adds proportional assist, with battery and safety monitoring.

> Assumptions: microcontroller firmware (PlatformIO) + Python tools for logging and analysis. Edit to match your actual stack.

## Features
- Manual mode, assist mode, and full-electric mode
- Torque-proportional assist from pushrim sensors
- Battery, speed, and fault monitoring
- Emergency stop and over-current protection
- Data logging for testing and tuning

## Repository Structure
```
firmware/      Microcontroller code
software/      Python tools (logging, analysis, simulation)
sample_data/   Example sensor logs
tests/         Test cases
docs/          Technical design document
```

## Prerequisites
- Python 3.10+
- PlatformIO (`pip install platformio`)
- Git
- Hardware: MCU board, motor driver, pushrim torque/encoder sensors, battery pack

## Setup
```bash
git clone https://github.com/<your-username>/hybrid-wheelchair.git
cd hybrid-wheelchair
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env             # then edit values
```

Build and flash firmware:
```bash
cd firmware
pio run
pio run -t upload
```

Run tests:
```bash
pytest tests/
```

## Environment Variables
| Variable | Description | Example |
|---|---|---|
| `SERIAL_PORT` | Port the controller connects to | `/dev/ttyUSB0` |
| `BAUD_RATE` | Serial baud rate | `115200` |
| `MAX_SPEED_KMH` | Speed limit | `6.0` |
| `ASSIST_RATIO` | Motor assist as fraction of user torque | `0.5` |
| `BATTERY_LOW_PCT` | Low-battery warning threshold | `20` |
| `MAX_CURRENT_A` | Over-current cutoff | `15` |
| `LOG_DIR` | Where logs are stored | `./logs` |

Never commit `.env`. Only `.env.example` is tracked.

## Safety Notice
This is a prototype. Do not use with a real passenger until it has passed safety validation.

## License
MIT. See [LICENSE](LICENSE).
