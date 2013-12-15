<?php
if (isset($_GET['api'])) {
	if (isset($_GET['l1']) && isset($_GET['l2'])) {
		if (strlen($_GET['l1']) <= 16 && strlen($_GET['l2']) <= 16) {
			sendCommand($_GET['l1'], $_GET['l2']);
			exit('SUCCESS');
		} else {
			exit('ERROR: 2 | GET "l1" and/or "l2" are longer than 16 chars.');
		}
	} else {
		exit('ERROR: 1 | GET "l1" and/or "l2" not defined.');
	}
} else if (isset($_GET['gui'])) {
	if (isset($_GET['l1']) && isset($_GET['l2'])) {
		if (strlen($_GET['l1']) <= 16 && strlen($_GET['l2']) <= 16) {
			sendCommand($_GET['l1'], $_GET['l2']);
		} else {
			$msg = 'String in Line 1 and/or Line 2 are longer than 16 chars.';
		}
	}
}

function sendCommand($l1, $l2) {
	$l1 = str_replace('"', '', $l1);
	$l2 = str_replace('"', '', $l2);
        shell_exec(' sudo python /home/pi/projects/lib/writetodisplay.py "'.$l1.'" "'.$l2.'" ');
}

?>


<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Displaywriter</title>
	<link rel="stylesheet" href="http://bootswatch.com/flatly/bootstrap.min.css">
	<style>
	input[type="text"] {max-width: 360px; margin-bottom: 10px;}
	</style>
</head>
<body>
	<div class="container">
		<h1>Displaywriter <small>writes strings to the pi-display</small></h1>
		<?php if (isset($msg)): ?>
		<div class="alert alert-danger fade-in">
			<?=$msg?>
		</div>
		<?php endif;  ?>
		<form action="displaywriter.php" method="get">
			<input type="hidden" name="gui" value="1">
			<input type="text" name="l1" class="form-control" maxlength="16" placeholder="line 1 string">
			<input type="text" name="l2" class="form-control" maxlength="16" placeholder="line 2 string">
			<input type="submit" value="send to display" class="btn btn-primary">
		</form>		
	</div>


<script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
<script src="//netdna.bootstrapcdn.com/bootstrap/3.0.3/js/bootstrap.min.js"></script>
</body>
</html>


