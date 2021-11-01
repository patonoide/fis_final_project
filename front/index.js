async function doupload() {
  let photo = document.getElementById("dataset").files[0];
  let formData = new FormData();

  formData.append("file", photo);
  formData.append("type", 1);

  fetch('localhost:5000/furry', {method: "POST", body: formData}).then( async (response) => {
      let data = await response.json();
      document.getElementById("#list-results").innerHTML = "";
      data.forEach((result)=> {
        document.getElementById("#list-results").innerHTML += ` 
        <li class="nav-item">
          <a class="nav-link active show" data-bs-toggle="tab">
            <h4>Image: ` + result.name + `</h4>
            <p>We found that this image is ` + result.value*100 + `% furry.</p>
          </a>
        </li>`
      })
      window.scrollTo(0,document.body.scrollHeight);
  });


}