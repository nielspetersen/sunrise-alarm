<?php
$days = ['monday', 'tuesday', 'wednesdays', 'thursday', 'friday', 'saturday', 'sunday'];

$alarms = ["alarms" => []];

foreach($days as $day) {
    $alarm = [
            "time_utc" => $_POST[$day . '_alarmtime'],
            "melody" => "Default",
            "advance_start" => $_POST[$day . '_advance_time'],
            "active" => ($_POST[$day . '_active'] == 'active' ? true : false)
    ];
    
    $alarms['alarms'][$day] = $alarm;
}

$json_content = json_encode($alarms, JSON_PRETTY_PRINT);
$json_content = str_replace(['[', ']'], '', $json_content); # Remove square brackets

file_put_contents('data/alarms.json', $json_content);

header("Location: index.php");
?>