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

            event.preventDefault();
            
        })
    })
})