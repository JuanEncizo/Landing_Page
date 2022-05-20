window.onload = () => {
  $("#sendbutton").click(() => {
    input = $("#imageinput")[0];
    console.log("aqui");
    i = 0;
    if (input.files && input.files[0]) {
      let formData = new FormData();
      formData.append("imagen_a_detectar", input.files[0]);
      console.log("aqui error ajax");
      $.ajax({
        url: "/encuestaproc", // fix this to your liking
        type: "POST",
        data: formData,
        cache: false,
        processData: false,
        contentType: false,
        error: function (data) {
          console.log("upload error", data);
          console.log(data.getAllResponseHeaders());
        },
        success: function (data) {
          console.log(data);
          console.log(data);
          i = 1;
          document.getElementById("botonSiguienteApi").style.visibility = "visible";
          
        },
      });
    }
  });
};



function readUrl(input) {
  /*console.log(imagebox);*/
  console.log(input.files[0]);
  console.log("evoked readUrl");

  if (input.files && input.files[0]) {
    let reader = new FileReader();
    reader.onload = function (e) {
      //$("#imagep").append("<img src='"+reader.result +"'>");
      console.log(e.target);


      //   imagebox.height(500);
      //   imagebox.width(800);
    };
    reader.readAsDataURL(input.files[0]);
  }
}

