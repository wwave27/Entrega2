$("#password").on("focusout", function (e) {
    if ($(this).val() != $("#passwordConfirm").val()) {
        $("#passwordConfirm").removeClass("valid").addClass("invalid");
    } else {
        $("#passwordConfirm").removeClass("invalid").addClass("valid");
    }
});

$("#passwordConfirm").on("keyup", function (e) {
    if ($("#password").val() != $(this).val()) {
        $(this).removeClass("valid").addClass("invalid");
    } else {
        $(this).removeClass("invalid").addClass("valid");
    }
});

var canRegister = false; 
var checkboxBool = false;

function checkboxCheck() {
    // Get the checkbox
    var checkBox1 = document.getElementById("cboxps");
    var checkBox2 = document.getElementById("cboxxbox");
    var checkBox3 = document.getElementById("cboxnin");
    var checkBox4 = document.getElementById("cboxpc");
    var checkBox5 = document.getElementById("cboxold");
    // Get the output text
    var text = document.getElementById("text");
  
    // If the checkbox is checked, display the output text
    if (checkBox1.checked == true || checkBox2.checked == true || checkBox3.checked == true || checkBox4.checked == true || checkBox5.checked == true ){
      checkboxLabel.style.display = "none";
      canRegister = true;
    } if (checkBox1.checked == false && checkBox2.checked == false && checkBox3.checked == false && checkBox4.checked == false && checkBox5.checked == false ){
      checkboxLabel.style.display = "block";
      canRegister = false;
    }
  } 

  function registrarse(){
      if (canRegister){
      }if(checkboxBool == false && canRegister == false){
        alert("Debes elegir al menos un interés");
      }
  }
