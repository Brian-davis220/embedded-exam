
# VPS Setup Guide

This guide will walk you through setting up an Ubuntu Server VPS with Mosquitto MQTT broker and Node-RED dashboard.

## Prerequisites

- Ubuntu Server 20.04 or later
- SSH access to VPS
- Root or sudo privileges

## Step 1: Update System Packages

```bash
sudo apt update
sudo apt upgrade -y
```

## Step 2: Install Mosquitto MQTT Broker

```bash
sudo apt install -y mosquitto mosquitto-clients
```

## Step 3: Configure Mosquitto

Create a configuration file:

```bash
sudo nano /etc/mosquitto/conf.d/default.conf
```

Add the following content:

```
listener 1883
allow_anonymous true
```

Save and exit (Ctrl+O, Enter, Ctrl+X).

## Step 4: Start and Enable Mosquitto Service

```bash
sudo systemctl start mosquitto
sudo systemctl enable mosquitto
```

Check status:

```bash
sudo systemctl status mosquitto
```

## Step 5: Configure Firewall (UFW)

```bash
sudo ufw allow 1883/tcp
sudo ufw allow 80/tcp
sudo ufw allow 1880/tcp
sudo ufw enable
```

## Step 6: Test Mosquitto

### Test Subscriber

Open one SSH terminal and run:

```bash
mosquitto_sub -h localhost -t "temperature/sensor" -v
```

### Test Publisher

Open another SSH terminal and run:

```bash
mosquitto_pub -h localhost -t "temperature/sensor" -m "24.5"
```

You should see the message appear in the subscriber terminal.

## Step 7: Install Node-RED

```bash
bash &lt;(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)
```

## Step 8: Start and Enable Node-RED

```bash
sudo systemctl start nodered
sudo systemctl enable nodered
```

## Step 9: Install Node-RED Dashboard

Open Node-RED in your browser at `http://your-vps-ip:1880`

1. Click the hamburger menu (☰) → Manage Palette
2. Go to "Install" tab
3. Search for "node-red-dashboard"
4. Click "Install"

## Step 10: Import Dashboard Flow

1. In Node-RED, click hamburger menu → Import
2. Copy the content from `dashboard/flow.json` in this repository
3. Paste it into the import dialog
4. Click "Import"
5. Click "Deploy"

## Step 11: Access the Dashboard

Open your browser and go to: `http://your-vps-ip:1880/ui`

## Troubleshooting

### Mosquitto Not Starting

```bash
sudo journalctl -u mosquitto -f
```

### Node-RED Not Starting

```bash
sudo journalctl -u nodered -f
```

### Checking Open Ports

```bash
sudo netstat -tuln | grep -E '1883|1880|80'
```

### Firewall Issues

```bash
sudo ufw status
```

## Screenshot Placeholders

Please place the following screenshots in the `screenshots/` directory:

- `mqtt_messages.jpg`: Screenshot of MQTT messages being published/subscribed
- `dashboard.jpg`: Screenshot of Node-RED dashboard

