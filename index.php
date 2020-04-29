<!doctype html> <html lang="en"> 
<head> 
	<meta charset="utf-8"/> 
	<meta name="viewport" content="width=device-width, initial-scale=1.0"> 
	<title>Set sunrise alarm</title>
	<link rel="stylesheet" type="text/css" href="assets/main.css">
</head>
<body>
	<div class="content">
		<h1>Sunrise Alarm</h1>
		<h3>Upcomping alarms</h3>
		<span style="font-weight:bold;">Please set your wake-up time:</span>

		<?php 	
			$content = file_get_contents("data/alarms.json");
			$json_content = json_decode($content, true);
		?>
		<div id="alarms">
			<form id="addAlarm" action="" method="post">
				<span id="message"></span>
				<button type="submit" id="submit">Save alarms</button>	
				<table id="alarm-table">
					<th>Day</th>
					<th>Status</th>
					<th>Time</th>
					<th>Advance Start (in Min)</th>
					<?php foreach($json_content['alarms'] as $key => $alarm) {
						echo '<tr>';
						echo '<td><b>', ucfirst($key), '</b></td>';
						echo '<td><input type="checkbox" id="', $key, '_active" name="', $key, '_active" value="active" ', ($alarm['active'] == true) ? 'checked=checked' : '', '></td>'; 
						echo '<td><input type="time" id="', $key, '_alarmtime" name="', $key, '_alarmtime" value=', $alarm['time_utc'], '></td>';
						echo '<td><select id="', $key, '_advance_time" name="', $key, '_advance_time">';
							echo '<option value="5" ', ($alarm['advance_start'] == 5) ? 'selected=selected' : '', '>5 Minutes</option>';
							echo '<option value="10" ', ($alarm['advance_start'] == 10) ? 'selected=selected' : '', '>10 Minutes</option>';
							echo '<option value="15" ', ($alarm['advance_start'] == 15) ? 'selected=selected' : '', '>15 Minutes</option>';
							echo '<option value="20" ', ($alarm['advance_start'] == 20) ? 'selected=selected' : '', '>20 Minutes</option>';
							echo '<option value="30" ', ($alarm['advance_start'] == 30) ? 'selected=selected' : '', '>30 Minutes</option>';
						echo '</select></td>';
						echo '</tr>';
					}
					?>
				</table>
			</form>
		</div>
	</div>
	<script type="text/javascript" src="assets/jquery-3.4.1.min.js"></script>
	<script type="text/javascript" src="assets/main.js"></script>
</body>