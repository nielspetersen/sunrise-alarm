<?php
$days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'];

$alarms = ["alarms" => []];

if($_POST) { 
    foreach($days as $day) {
        $alarm = [
            "time_utc" => filter_var($_POST[$day . '_alarmtime'], FILTER_SANITIZE_STRING),
            "melody" => "Default",
            "advance_start" => filter_var($_POST[$day . '_advance_time'], FILTER_SANITIZE_STRING),
            "active" => ($_POST[$day . '_active'] == 'active' ? true : false)
        ];
        
        $alarms['alarms'][$day] = $alarm;
    }

    $json_content = json_encode($alarms, JSON_PRETTY_PRINT);
    $json_content = str_replace(['[', ']'], '', $json_content); # Remove square brackets

    file_put_contents('data/alarms.json', $json_content);
}
?>