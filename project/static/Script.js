function searchFunction() {

    var input, filter, ul, li, a, i, txtValue;
    input = document.getElementById('myInput');
    filter = input.value.toUpperCase();
    ul = document.getElementById("myUL");
    li = ul.getElementsByTagName('li');

    // Loop through all list items, and hide those who don't match the search query
    for (i = 0; i < li.length; i++) {
        a = li[i].getElementsByTagName("a")[0];
        txtValue = a.textContent || a.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            li[i].style.display = "";
        } else {
            li[i].style.display = "none";
        }
    }
}



for (book in class Book {}) {
    $(".cat{{book.category.id}}").click(function() {
        $(".bookhide").hide();
        $(".book{{book.category.id}}").show();


    });

}




function toggleClock(a) {

    if (a == 1) {
        document.getElementById("mm").style.display = "none";
        document.getElementById("mm2").style.display = "block";
    } else {
        document.getElementById("mm").style.display = "block";
        document.getElementById("mm2").style.display = "none";

        document.getElementById("username").value = "";
        document.getElementById("pwd").value = "";
    }
}


function saveData() {
    if (document.getElementById("username").value == "" && document.getElementById("pwd").value == "") {
        alert("You have changed nothing");

    } else {
        if (document.getElementById("username").value == "") {
            var passTarget = document.getElementById("pwd").value;
            document.getElementById("pass").innerText = passTarget;
            alert("You have changed the password");
        } else if (document.getElementById("pwd").value == "") {
            var userTarget = document.getElementById("username").value;
            document.getElementById("user").innerText = userTarget;
            alert("You have changed the username");
        } else {
            var userTarget = document.getElementById("username").value;
            document.getElementById("user").innerText = userTarget;

            var passTarget = document.getElementById("pwd").value;
            document.getElementById("pass").innerText = passTarget;
            alert("You have changed the username and the password");
        }

    }

}