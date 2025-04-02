import { uploadPhoto, createUser } from './utils';

function handleProfileSignup() {
  Promise.all([uploadPhoto(), createUser()])
    .then(([uploadPhoto, user]) => {
      console.log(`${uploadPhoto.body} ${user.firstName} ${user.lastName}`);
    })
    .catch(() => {
      console.log('Sugnup system offline');
    });
}

export default handleProfileSignup;
