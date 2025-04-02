export default function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    const success = true; // simule une reponse reussie

    if (success) {
      resolve('Success!');
    } else {
      reject(new Error('Error: request failed.'));
    }
  });
}
