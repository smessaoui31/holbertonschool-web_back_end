const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf-8');
    const lines = data.split('\n').filter((line) => line.trim() !== '');

    // remove header
    const students = lines.slice(1);

    console.log(`Number of students: ${students.length}`);

    const fields = {};
    students.forEach((student) => {
      const parts = student.split(',');
      const firstname = parts[0];
      const field = parts[3];

      if (field) {
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstname);
      }
    });

    for (const [field, list] of Object.entries(fields)) {
      console.log(
        `Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`
      );
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
