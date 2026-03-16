Dette er et test program, designet til at fremvise QR scanning funktionalitet i App.
For at køre dette skal du bruge Docker/docker-compose.

Før du kan køre det skal du lave en ny fil der heder .env du kan også kopier .env.example og omdøb den.

Heri skal du definere 3 Enviorenment Variabler:
Env Variable | Indhold | Eksemple
--- | --- | ---
PORT | Dette er porten programmet smider sin test hjemmeside på | 5000
API_URL | Dette er url til hvor Web API ligger | "https://api.com"
DEVICE_CODE | Dette er en kode genereret når du opretter en device på WebApp | "1234567890"

Når disse er defineret kan du køre<br>
`docker-compose up -d`<br>
For at køre programmet i baggrunden og så kan du gå til localhost:PORT og se en rullende QR kode

Når du vil ligge det ned igen kan du køre<br>
`docker-compose down`<br>
Herefter kan du køre dette for at sikre containers/volumes bliver slettet korrekt<br>
`docker-compose rm`<br>
