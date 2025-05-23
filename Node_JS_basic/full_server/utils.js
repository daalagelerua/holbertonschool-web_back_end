import fs from 'fs';

const readDatabase = (filePath) => {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf8', (error, data) => {
      if (error) {
        reject(error);
        return;
      }

      try {
        // Split content by lines and filter out empty lines
        const lines = data.split('\n').filter((line) => line.trim() !== '');

        // Extract headers (first line)
        const headers = lines[0].split(',');

        // Get index of field column
        const fieldIndex = headers.indexOf('field');
        const firstnameIndex = headers.indexOf('firstname');

        // Remove header line to get only student data
        const studentLines = lines.slice(1);

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

        resolve(studentsByField);
      } catch (parseError) {
        reject(parseError);
      }
    });
  });
};

export default readDatabase;
