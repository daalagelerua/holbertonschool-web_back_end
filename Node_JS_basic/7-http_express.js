const express = require('express');
const fs = require('fs').promises;

const app = express();
const port = 1245;

/**
 * Counts the number of students in each field from a CSV database file asynchronously
 * @param {string} path - Path to the CSV file
 * @return {Promise} - A promise that resolves with a string containing the formatted results
 */
async function countStudents(path) {
  try {
    const fileContent = await fs.readFile(path, 'utf8');

    // Split content by lines and filter out empty lines
    const lines = fileContent.split('\n').filter((line) => line.trim() !== '');

    // Extract headers (first line)
    const headers = lines[0].split(',');

    // Get index of field column
    const fieldIndex = headers.indexOf('field');
    const firstnameIndex = headers.indexOf('firstname');

    // Remove header line to get only student data
    const studentLines = lines.slice(1);

    // Prepare output string
    let output = `Number of students: ${studentLines.length}\n`;

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

    // Add field information to output
    for (const field in studentsByField) {
      if (Object.prototype.hasOwnProperty.call(studentsByField, field)) {
        const students = studentsByField[field];
        output += `Number of students in ${field}: ${students.length}. List: ${students.join(', ')}\n`;
      }
    }

    return output.trim();
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

// Route for the root path
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// Route for /students path
app.get('/students', async (req, res) => {
  let responseText = 'This is the list of our students\n';

  try {
    // Get the database file path from command line arguments
    const dbFilePath = process.argv[2];

    if (!dbFilePath) {
      throw new Error('Cannot load the database');
    }

    // Get student data
    const studentData = await countStudents(dbFilePath);
    responseText += studentData;

    res.send(responseText);
  } catch (error) {
    responseText += error.message;
    res.send(responseText);
  }
});

app.listen(port, () => {
  // Server is now listening
});

module.exports = app;
