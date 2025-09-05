const fs = require('fs');

async function countStudents(path) {
  const myPromise = new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
      }
      resolve(data);
    });
  });

  return myPromise.then((data) => {
    const content = data.split('\n');
    const fields = {};
    let total = 0;

    for (let i = 1; i < content.length; i += 1) {
      const [firstname, , , field] = content[i].split(',');

      if (!(field in fields) && field) {
        fields[field] = [];
      }

      if (field) {
        fields[field].push(firstname);
        total += 1;
      }
    }

    let result = `Number of students: ${total}`;

    for (const [key] of Object.entries(fields)) {
      result = result + `\nNumber of students in ${key}: ${fields[key].length}. List: ${fields[key].join(', ')}`;
    }

    console.log(result);
    return result;
  });
}

module.exports = countStudents;
