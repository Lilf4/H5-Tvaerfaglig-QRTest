# Test Program – QR Scanning

Dette er et testprogram designet til at fremvise **QR-scanning funktionalitet** i App.

## Krav

For at køre projektet skal følgende være installeret:

- Docker
- docker-compose

---

# Opsætning

Før du kan køre projektet, skal du oprette en `.env` fil.

Du kan enten:

- oprette en ny fil kaldet `.env`
- eller kopiere `.env.example` og omdøbe den
---

# Environment Variables

I `.env` filen skal følgende variabler defineres:

| Env Variable | Beskrivelse | Eksempel |
|---|---|---|
| PORT | Port som testprogrammet viser sin hjemmeside på | 5000 |
| API_URL | URL til Web API | https://api.com |
| DEVICE_CODE | Kode genereret ved oprettelse af en device i WebApp | 1234567890 |

---

# Start Test Program

Når variablerne er defineret kan du starte programmet:

```bash
docker-compose up -d
```

Dette starter programmet i **baggrunden**.

Herefter kan du åbne programmet i browseren:

```
http://localhost:PORT
```

Her vil du kunne se en **rullende QR-kode**.

---

# Stop Test Program

For at stoppe programmet:

```bash
docker-compose down
```

For også at fjerne containers og volumes:

```bash
docker-compose rm
```
