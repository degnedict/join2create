# Verwende die neueste LTS-Version von Node.js
FROM node:18

# Erstelle und setze das Arbeitsverzeichnis
WORKDIR /usr/src/app

# Kopiere package.json und package-lock.json (falls vorhanden)
COPY package*.json ./

# Installiere die Abhängigkeiten
RUN npm install

# Kopiere den Rest des Anwendungsverzeichnisses
COPY . .

# Definiere die Startkommandozeile für den Container
CMD [ "npm", "start" ]
