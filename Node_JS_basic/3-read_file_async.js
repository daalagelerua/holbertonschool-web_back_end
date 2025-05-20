const fs = require('fs').promises;

/**
 * Counts the number of students in each field from a CSV database file asynchronously
 * @param {string} path - Path to the CSV file
 * @return {Promise} - A promise that resolves when counting is done
 */
function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8')
      .then((fileContent) => {
        // Split content by lines and filter out empty lines
        const lines = fileContent.split('\n').filter((line) => line.trim() !== '');

        // Extract headers (first line)
        const headers = lines[0].split(',');

        // Get index of field column
        const fieldIndex = headers.indexOf('field');
        const firstnameIndex = headers.indexOf('firstname');

        // Remove header line to get only student data
        const studentLines = lines.slice(1);

        // Log total number of students
        console.log(`Number of students: ${studentLines.length}`);

        // Group students by field
        const studentsByField = {};

        studentLines.forEach((line) => {
          const fields = line.split(',');
          const field = fields[fieldIndex];
          const firstname = fields[firstnameIndex];

          if (!studentsByField[field]) {
            studentsByField[field] = [];
          }

          studentsByField[field].push(firstname);
        });

        // Log number of students in each field
        for (const field in studentsByField) {
          if (Object.prototype.hasOwnProperty.call(studentsByField, field)) {
            const students = studentsByField[field];
            console.log(`Number of students in ${field}: ${students.length}. List: ${students.join(', ')}`);
          }
        }

        resolve();
      })
      .catch(() => {
        reject(new Error('Cannot load the database'));
      });
  });
}

module.exports = countStudents;
