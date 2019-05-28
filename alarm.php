<?php
$wakeuptime = $_POST['wakeup-time'];
// Remove digits for seconds and miliseconds
$wakeuptime = substr($wakeuptime, 0, 16);

echo 'The wake-up time ' . $wakeuptime . ' .';

file_put_contents('data/alarm_time.txt', $wakeuptime);
?>