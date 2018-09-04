$(document).ready(function () {

    localStorage.setItem('popState', 'askjldf');
    if (localStorage.getItem('popState') != 'shown') {
        $('body').css({backgroundColor: '#222A35'})
        $("#popup").delay(200).fadeIn(1000);
        localStorage.setItem('popState', 'shown');
        $('#popup').delay(3400).fadeOut(600);
        //find good animation method to convert background back to white

    }
    $('body').animate({backgroundColor: '#FFFFFF'}, 'slow');
    $('#popup-close').click(function (e) // You are clicking the close button
    {
        $('#popup').fadeOut(); // Now the pop up is hidden.
    });
    $('#popup').click(function (e) {
        $('#popup').fadeOut();
    });
});