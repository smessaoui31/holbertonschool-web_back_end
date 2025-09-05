const express = require('express');
const fs = require('fs');

const database = process.argv[2];
const app = express();

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data
        .split('\n')
        .map((l) => l.trim())
        .filter((l) => l.length > 0);

      const rows = lines.slice(1);
      const total = rows.length;

      const fields = {};
      rows.forEach((row) => {
        const parts = row.split(',');
        if (parts.length >= 4) {
          const firstname = parts[0];
          const field = parts[3];
          if (field) {
            if (!fields[field]) fields[field] = [];
            fields[field].push(firstname);
          }
        }
      });

      let output = `Number of students: ${total}\n`;
      Object.keys(fields)
        .sort()
        .forEach((field) => {
          const list = fields[field];
          output += `Number of students in ${field}: ${list.length}. List: ${list.join(', ')}\n`;
        });

      resolve(output.trim());
    });
  });
}

app.get('/', (_req, res) => {
  res.set('Content-Type', 'text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', async (_req, res) => {
  res.set('Content-Type', 'text/plain');
  const header = 'This is the list of our students';
  try {
    const stats = await countStudents(database);
    res.send(`${header}\n${stats}`);
  } catch (_e) {
    res.send(`${header}\nCannot load the database`);
  }
});

app.listen(1245);

module.exports = app;
