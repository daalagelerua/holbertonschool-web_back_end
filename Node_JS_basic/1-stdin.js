#!/usr/bin/node

// Display welcome message
process.stdout.write('Welcome to Holberton School, what is your name?\n');

// Set up stdin to receive input
process.stdin.setEncoding('utf8');

// Listen for data on stdin
process.stdin.on('data', (data) => {
  // Display the user's name
  process.stdout.write(`Your name is: ${data.trim()}\n`);
  
  // If this is not being piped (interactive mode), exit after displaying the name
  if (process.stdin.isTTY) {
    process.exit();
  }
});

// Handle end of input (occurs with piped input)
process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing\n');
});
