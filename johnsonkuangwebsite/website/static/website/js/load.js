$(document).ready(function () {
    //TODO: remove localStorage.setItem
    if (localStorage.getItem('popState') != 'shown') {
        $('body').css({backgroundColor: '#FFF'})
        $("#popup").delay(0).fadeIn(700);
        localStorage.setItem('popState', 'shown');
        $('#popup').delay(4000).fadeOut(600);

        //find good animation method to convert background back to white
        setTimeout(location.reload.bind(location), 5000);
    }

    $('#popup-close').click(function (e) // You are clicking the close button
    {
        $('#popup').fadeOut(); // Now the pop up is hidden.
    });
    $('#popup').click(function (e) {
        $('#popup').fadeOut();
    });

});