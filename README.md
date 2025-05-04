
🎾**Ping Pong Game (Python & Pygame)**

A simple Ping Pong game built using Python and Pygame. Currently, it's a local multiplayer game, but future updates will include network play!

🚀 **How to Play**

1️⃣ **Run the script:**
```bash
 python ping_pong.py
```
2️⃣ **Controls:**
	
Player 1: W (Up), S (Down)
Player 2: ↑ (Up Arrow), ↓ (Down Arrow)

3️⃣ **Objective:**

Hit the ball with your paddle.
Score points by making your opponent miss the ball.

🛠 **Features**

✅ Two-player local gameplay

✅ Simple physics-based ball movement

✅ Score tracking

🖥 **Installation**

Ensure you have Python and Pygame installed:

```bash
pip install p
```

# 🏓 Ping Pong Game (Network-Based, Python + Pygame + Sockets)

## 📝 Project Report: Network-Based Ping Pong Game (Python, Sockets)

This project demonstrates a simple **two-player networked Ping Pong game** developed using **Python** and the **socket** library. The architecture follows a **client-server model**, with the server acting as a central relay for exchanging game data.

### 💻 System Setup Overview

- **Machine 1 (Windows)** — Runs the **server** (`server(new).py`)
- **Machine 2 (Windows)** — Runs **Player 1 client** (`client.py`)
- **Machine 3 (Ubuntu)** — Runs **Player 2 client** (`client.py`)

All three machines are connected through the same local area network (LAN), either via VMware virtual adapters or physical LAN.

---

## 🧱 Architecture & Code Description

### `server(new).py` – The Server

- Initializes a TCP server on a specified port using Python’s `socket` module.
- Waits for **two clients** to connect (blocking mode).
- Assigns player numbers: the first connection is `Player 1`, the second is `Player 2`.
- Maintains a loop to **receive game state data** (position of paddles, ball) from each client and **broadcast it** to the other player.
- Uses `pickle` to serialize and deserialize Python dictionaries containing the game state, ensuring structured and consistent data exchange.

#### Key Server Responsibilities:
- Managing client connections
- Data synchronization between players
- Handling disconnections gracefully

---

### `client(new).py` – The Player Client

- Connects to the server using the server's IP and port.
- Initializes a `pygame` window to visually render the game.
- Each client handles **its own paddle control**, sending position updates to the server.
- Receives the **other player’s paddle position** and the **ball’s position** from the server.
- Implements basic collision detection and ball reflection logic on the client side (for responsiveness).
- Uses a main game loop with frame control via `pygame.time.Clock`.

#### Client Features:
- Controls:  
  - Player 1: `W` (up), `S` (down)  
  - Player 2: `↑` (up arrow), `↓` (down arrow)
- Handles keyboard input and game physics locally
- Sends updates to the server every frame

---

## 🌐 Networking & Testing

### Configuration

- Static IPs or local DHCP-assigned IPs used for all virtual/physical machines.
- Example server address in client:
  ```python
  s.connect(("192.168.1.101", 5555))
  ```

### Testing

- Verified connectivity using:
  ```bash
  ping 192.168.1.101       # From Linux to Windows Server
  ```

- Server console shows client connections:
  ```
  [INFO] Player 1 connected
  [INFO] Player 2 connected
  ```

- Game starts once both clients are active.

---

## 🛠️ Technologies Used

| Component      | Technology   |
|----------------|--------------|
| Programming    | Python 3.x   |
| Networking     | `socket`, `pickle` |
| Graphics       | `pygame`     |
| OS             | Windows 10, Ubuntu 22.04 |
| Virtualization | VMware Workstation |

---

## 🚀 How to Run

### 🖥️ Server (Machine 1):
```bash
python server(new).py
```

### 🎮 Client (Players 1 & 2 on separate machines):
```bash
python client.py [SERVER_IP]
```
> Replace `[SERVER_IP]` with the IP of the server machine (e.g., `192.168.1.101`)

---

## 🧪 Useful Bash / PowerShell Commands

### View your local IP:
- **Windows (PowerShell):**
  ```powershell
  ipconfig
  ```
- **Linux:**
  ```bash
  ip a
  ```

### Test Network Connectivity:
```bash
ping [target IP]
```

### Open Firewall for Python (Windows):
```powershell
New-NetFirewallRule -DisplayName "Python Socket Game" -Direction Inbound -Program "C:\Path\To\python.exe" -Action Allow
```
