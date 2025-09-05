const fs = require('fs');

async function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data
        .split('\n')
        .map((l) => l.trim())
        .filter((l) => l !== '');

      const rows = lines.slice(1);

      console.log(`Number of students: ${rows.length}`);

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

      Object.keys(fields)
        .sort()
        .forEach((field) => {
          const list = fields[field];
          console.log(
            `Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`
          );
        });

      resolve();
    });
  });
}

module.exports = countStudents;
