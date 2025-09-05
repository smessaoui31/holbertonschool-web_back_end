import readDatabase from '../utils.js';

class StudentsController {
  static async getAllStudents(_req, res) {
    const dbPath = process.argv[2];
    const header = 'This is the list of our students';

    try {
      const data = await readDatabase(dbPath);
      const fields = Object.keys(data).sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));

      const lines = [header];
      const total = fields.reduce((acc, f) => acc + (data[f]?.length || 0), 0);
      lines.push(`Number of students: ${total}`);

      fields.forEach((field) => {
        const list = data[field] || [];
        lines.push(`Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`);
      });

      res.status(200).type('text/plain').send(lines.join('\n'));
    } catch (_e) {
      res.status(500).type('text/plain').send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const dbPath = process.argv[2];
    const { major } = req.params;

    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).type('text/plain').send('Major parameter must be CS or SWE');
      return;
    }

    try {
      const data = await readDatabase(dbPath);
      const list = data[major] || [];
      res.status(200).type('text/plain').send(`List: ${list.join(', ')}`);
    } catch (_e) {
      res.status(500).type('text/plain').send('Cannot load the database');
    }
  }
}

export default StudentsController;
