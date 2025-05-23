import readDatabase from '../utils.js';

class StudentsController {
  static async getAllStudents(request, response) {
    try {
      const databasePath = process.argv[2];

      if (!databasePath) {
        response.status(500).send('Cannot load the database');
        return;
      }

      const studentsByField = await readDatabase(databasePath);

      let responseText = 'This is the list of our students\n';

      // Sort fields alphabetically (case insensitive)
      const sortedFields = Object.keys(studentsByField).sort((a, b) => 
        a.toLowerCase().localeCompare(b.toLowerCase())
      );

      sortedFields.forEach((field) => {
        const students = studentsByField[field];
        responseText += `Number of students in ${field}: ${students.length}. List: ${students.join(', ')}\n`;
      });
  
      response.status(200).send(responseText.trim());
    } catch (error) {
      response.status(500).send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(request, response) {
    try {
      const { major } = request.params;

      // Validate major parameter
      if (major !== 'CS' && major !== 'SWE') {
        response.status(500).send('Major parameter must be CS or SWE');
        return;
      }

      const databasePath = process.argv[2];

      if (!databasePath) {
        response.status(500).send('Cannot load the database');
        return;
      }

      const studentsByField = await readDatabase(databasePath);

      const students = studentsByField[major] || [];
      const responseText = `List: ${students.join(', ')}`;

      response.status(200).send(responseText);
    } catch (error) {
      response.status(500).send('Cannot load the database');
    }
  }
}

export default StudentsController;
