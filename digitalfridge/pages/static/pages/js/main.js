// // Create a "close" button and append it to each list item
// var myNodelist = document.getElementsByTagName("LI");
// var i;
// for (i = 0; i < myNodelist.length; i++) {
//   var span = document.createElement("SPAN");
//   var txt = document.createTextNode("\u00D7");
//   span.className = "close";
//   span.appendChild(txt);
//   myNodelist[i].appendChild(span);
// }
//
// // Click on a close button to hide the current list item
// var close = document.getElementsByClassName("close");
// var i;
// for (i = 0; i < close.length; i++) {
//   close[i].onclick = function() {
//     var div = this.parentElement;
//     div.style.display = "none";
//   }
// }
//
// // Add a "checked" symbol when clicking on a list item
// var list = document.querySelector('ul');
// list.addEventListener('click', function(ev) {
//   if (ev.target.tagName === 'LI') {
//     ev.target.classList.toggle('checked');
//   }
// }, false);
//
// // Create a new list item when clicking on the "Add" button
// function newElement() {
//   var li = document.createElement("li");
//   var inputValue = document.getElementById("myInput").value;
//   var t = document.createTextNode(inputValue);
//   li.appendChild(t);
//   if (inputValue === '') {
//     alert("Did you forget to type your item?");
//   } else {
//     document.getElementById("myUL").appendChild(li);
//   }
//   document.getElementById("myInput").value = "";
//
//   var span = document.createElement("SPAN");
//   var txt = document.createTextNode("\u00D7");
//   span.className = "close";
//   span.appendChild(txt);
//   li.appendChild(span);
//
//   for (i = 0; i < close.length; i++) {
//     close[i].onclick = function() {
//       var div = this.parentElement;
//       div.style.display = "none";
//     }
//   }
// }


// Get the modal
var frozen_modal = document.getElementById('frozenModal');
var heatneat_modal = document.getElementById('heatneatModal');
var desserts_modal = document.getElementById('dessertsModal');
var meat_modal = document.getElementById('meatModal');
var seafood_modal = document.getElementById('seafoodModal');
var dairy_modal = document.getElementById('dairyModal');
var veg_modal = document.getElementById('vegModal');
var fruit_modal = document.getElementById('fruitModal');
var leftovers_modal = document.getElementById('leftoversModal');
var alcohol_modal = document.getElementById('alcoholModal');
var nonedible_modal = document.getElementById('nonedibleModal');
var other_modal = document.getElementById('otherModal');
var condiments_modal = document.getElementById('condimentsModal');
var sauces_modal = document.getElementById('saucesModal');
var beverages_modal = document.getElementById('beveragesModal');


// Get the button that opens the modal
var frozen_btn = document.getElementById("frozenBtn");
var heatneat_btn = document.getElementById("heatneatBtn");
var desserts_btn = document.getElementById("dessertsBtn");
var meat_btn = document.getElementById("meatBtn");
var seafood_btn = document.getElementById("seafoodBtn");
var dairy_btn = document.getElementById("dairyBtn");
var veg_btn = document.getElementById("vegBtn");
var fruit_btn = document.getElementById("fruitBtn");
var leftovers_btn = document.getElementById("leftoversBtn");
var alcohol_btn = document.getElementById("alcoholBtn");
var nonedible_btn = document.getElementById("nonedibleBtn");
var other_btn = document.getElementById("otherBtn");
var condiments_btn = document.getElementById("condimentsBtn");
var sauces_btn = document.getElementById("saucesBtn");
var beverages_btn = document.getElementById("beveragesBtn");

// Get the <span> element that closes the modal
var frozen_span = document.getElementsByClassName("close")[0];
var heatneat_span = document.getElementsByClassName("close")[1];
var desserts_span = document.getElementsByClassName("close")[2];
var meat_span = document.getElementsByClassName("close")[3];
var seafood_span = document.getElementsByClassName("close")[4];
var dairy_span = document.getElementsByClassName("close")[5];
var veg_span = document.getElementsByClassName("close")[6];
var fruit_span = document.getElementsByClassName("close")[7];
var leftovers_span = document.getElementsByClassName("close")[8];
var alcohol_span = document.getElementsByClassName("close")[9];
var nonedible_span = document.getElementsByClassName("close")[10];
var other_span = document.getElementsByClassName("close")[11];
var condiments_span = document.getElementsByClassName("close")[12];
var sauces_span = document.getElementsByClassName("close")[13];
var beverages_span = document.getElementsByClassName("close")[14];

// When the user clicks on the button, open the modal
frozen_btn.onclick = function() {
      frozen_modal.style.display = "block";
};
heatneat_btn.onclick = function() {
    heatneat_modal.style.display = "block";
};
desserts_btn.onclick = function() {
    desserts_modal.style.display = "block";
};
meat_btn.onclick = function() {
    meat_modal.style.display = "block";
};
seafood_btn.onclick = function() {
    seafood_modal.style.display = "block";
};
dairy_btn.onclick = function() {
    dairy_modal.style.display = "block";
};
veg_btn.onclick = function() {
    veg_modal.style.display = "block";
};
fruit_btn.onclick = function() {
    fruit_modal.style.display = "block";
};
leftovers_btn.onclick = function() {
    leftovers_modal.style.display = "block";
};
alcohol_btn.onclick = function() {
    alcohol_modal.style.display = "block";
};
nonedible_btn.onclick = function() {
    nonedible_modal.style.display = "block";
};
other_btn.onclick = function() {
    other_modal.style.display = "block";
};
condiments_btn.onclick = function() {
    condiments_modal.style.display = "block";
};
sauces_btn.onclick = function() {
    sauces_modal.style.display = "block";
};
beverages_btn.onclick = function() {
    beverages_modal.style.display = "block";
};

// When the user clicks on <span> (x), close the modal
frozen_span.onclick = function() {
    frozen_modal.style.display = "none";
};
heatneat_span.onclick = function() {
    heatneat_modal.style.display = "none";
};
desserts_span.onclick = function() {
    desserts_modal.style.display = "none";
};
meat_span.onclick = function() {
    meat_modal.style.display = "none";
};
seafood_span.onclick = function() {
    seafood_modal.style.display = "none";
};
dairy_span.onclick = function() {
    dairy_modal.style.display = "none";
};
veg_span.onclick = function() {
    veg_modal.style.display = "none";
};
fruit_span.onclick = function() {
    fruit_modal.style.display = "none";
};
leftovers_span.onclick = function() {
    leftovers_modal.style.display = "none";
};
alcohol_span.onclick = function() {
    alcohol_modal.style.display = "none";
};
nonedible_span.onclick = function() {
    nonedible_modal.style.display = "none";
};
other_span.onclick = function() {
    other_modal.style.display = "none";
};
condiments_span.onclick = function() {
    condiments_modal.style.display = "none";
};
sauces_span.onclick = function() {
    sauces_modal.style.display = "none";
};
beverages_span.onclick = function() {
    beverages_modal.style.display = "none";
};
