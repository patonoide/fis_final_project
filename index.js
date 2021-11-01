async function doupload() {
  let photo = document.getElementById("dataset").files[0];
  let formData = new FormData();

  formData.append("photo", photo);
  fetch('/file', {method: "POST", body: formData}).then( (response) => {
    
  });
}