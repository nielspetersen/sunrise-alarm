$(document).ready(function() {

    var form = $('#addAlarm'),
        message = $('#message'),
        submit = $("#submit");    
    
    submit.on('click', function(e) {
        e.preventDefault();
        $.ajax({
            type: "POST",
            url: "alarm.php",
            data: form.serialize(),
            dataType: "json",
            success: function(data) {
                message.text('Alarms have be updated!').css('color', 'green').slideDown("slow");
            },
            error: function(jqXHR, textStatus, errorThrown) {
                alert(errorThrown);
                message.text('Error occured. Alarms have not been updated').css('color', 'red').slideDown("slow");
            }
        });
    });
});