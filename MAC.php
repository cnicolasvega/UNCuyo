<!DOCTYPE html>
<html lang="es">
    <meta charset="utf-8"/>
	<meta name="viewport" content="width=device-width, initial-scale=1">
    <title>NOC | UNCuyo</title>
    <link rel="stylesheet" type="text/css" href="css/styles-noc.css">
    <link rel="shortcut icon" href="img/favicon.png"/>
    <body>
        <?php
            $mac_address = "FC:FB:FB:01:FA:21";
            $url = "https://api.macvendors.com/" . urlencode($mac_address);
            $ch = curl_init();
            curl_setopt($ch, CURLOPT_URL, $url);
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
            $response = curl_exec($ch);
            if($response) {
                echo "Vendor: $response";
            } else {
                echo "Not Found";
            }
        ?>
    </body>
</html>