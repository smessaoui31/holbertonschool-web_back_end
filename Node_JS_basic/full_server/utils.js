import fs from 'fs';

export default function readDatabase(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(err);
        return;
      }

      const lines = data
        .split('\n')
        .map((l) => l.trim())
        .filter((l) => l.length > 0);

      const rows = lines.slice(1);
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

      resolve(fields);
    });
  });
}
