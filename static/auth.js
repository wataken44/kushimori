
var kushimori = kushimori || {};

kushimori.initializeFirebase = function() {
  let firebaseConfig = {
    apiKey: "AIzaSyAcFlYHOdBR0FJyKvvH-qJiYiyDxA7_HVk",
    authDomain: "kushimori.firebaseapp.com",
    databaseURL: "https://kushimori.firebaseio.com",
    projectId: "kushimori",
    storageBucket: "kushimori.appspot.com",
    messagingSenderId: "424175899837",
    appId: "1:424175899837:web:c383d2e8185b7627"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);
}
kushimori.initializeFirebase();

kushimori.initializeFirebaseUI = function(selector) {
  // FirebaseUI config.
  let uiConfig = {
    signInSuccessUrl: '/login',
    signInOptions: [
      // Leave the lines as is for the providers you want to offer your users.
      firebase.auth.GoogleAuthProvider.PROVIDER_ID,
    ],
    // tosUrl and privacyPolicyUrl accept either url string or a callback
    // function.
    // Terms of service url/callback.
    tosUrl: '/tos',
    // Privacy policy url/callback.
    privacyPolicyUrl: '/pp'
  };

  // Initialize the FirebaseUI Widget using Firebase.
  let ui = new firebaseui.auth.AuthUI(firebase.auth());
  // The start method will wait until the DOM is loaded.
  ui.start(selector, uiConfig);
}

kushimori.createSessionAfterAuth = function() {
  firebase.auth().onAuthStateChanged(function(user) {
    if (user) {
      let name = user.displayName;
      user.getIdToken().then(function(idToken) {
        $.ajax({
          'url': '/session',
          'type': 'POST',
          'data': {
            'token': idToken
          },
          'dataType': 'json'
        }, {
          headers: {
            'Authorization': 'Bearer ' + idToken
          }
        }).then(function(data) {
          if(data["session"]) {
            // login succeeded
            Cookies.set('session_id', data["session"], { expires: 360 });
            // redirect
            location.href="/dashboard/";
          }
        });
      });
    }
  });
};
