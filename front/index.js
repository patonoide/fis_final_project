async function doupload() {
  let photo = document.getElementById("dataset").files[0];
  let formData = new FormData();

  formData.append("file", photo);

  document.getElementById("list-results").innerHTML = "";
  document.getElementById("spinner1").innerHTML = `
    <div class="spinner-border" role="status">
      <span class="visually-hidden">Loading...</span>
    </div>
  `;

  var e = document.getElementById("preprocessing-opt");
  var opt = e.value;
  formData.append("type", opt);


  fetch('http://localhost:5000/furry', {method: "POST", body: formData}).then( async (response) => {
      let data = await response.json();
      data.forEach((result)=> {
        document.getElementById("list-results").innerHTML += ` 
        <li class="nav-item">
          <a class="nav-link" data-bs-toggle="tab">
            <h4>Image: ` + result.name + `</h4>
            <p>We found that this image is ` +parseFloat(result.value*100).toFixed(2) + `% furry.</p>
          </a>
        </li>`;
      })
      document.getElementById("spinner1").innerHTML = "";
      window.scrollTo(0,document.body.scrollHeight);
  });


}