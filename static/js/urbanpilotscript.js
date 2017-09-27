$(document).ready(function () {
    $(function () {
        $('form').submit(function (event) {

            if (!event.isDefaultPrevented()) {
                emailval = $('#email').val()
                fnameval = $('#fname').val()
                mnameval = $('#mname').val()
                lnameval = $('#lname').val()
                zipval = Number($('#zip').val())

                info = {
                    fname: fnameval,
                    mname: mnameval,
                    lname: lnameval,
                    zip: zipval,
                    email: emailval
                }


                console.log(fnameval, mnameval, lnameval, emailval, zipval)

                $.ajax({
                    type: 'POST',
                    url: '/signup',
                    data: info,

                    success: function (data) {
                        console.log(data)
                        console.log(data.fname)
                        console.log(data.id)
                        console.log(data.email)
                        $('#signupform').hide()
                        $('#success').show()

                    },
                    error: function (xhr, status, error) {
                        alert("That email address is already taken, sorry :(")
                    }

                })

                /*
                $.post("/signup", {
                    fname: $('#fname').val(),
                    mname: $('#mname').val(),
                    lname: $('#lname').val(),
                    zip: $('#zip').val(),
                    email: $('#email').val()
                }, function (data) {
                    console.log(data)
                    if (status == 500) {
                        alert("That email is already taken, sorry :(")
                    }
                    console.log(data)
                    console.log(status)
                })
                */

            }

            /*

            if (fnameval == "" || lnameval == "" || zipval == "" || emailval == "") {
                alert("Please fill in all required fields")
            }
            else if (!Number.isInteger(Number(zipval))) {
                alert("Please enter a valid zipcode")
            
            }
            else {
                $.getJSON("/infosubmission", {
                    fname: $('#fname').val(),
                    mname: $('#mname').val(),
                    lname: $('#lname').val(),
                    zip: $('#zip').val(),
                    email: $('#email').val()
                })
            }
            */

            event.preventDefault();
            
        })
    })
})