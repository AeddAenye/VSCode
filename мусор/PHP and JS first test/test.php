<?php

if ($_SERVER['REQUEST_METHOD'] == "POST") {
    $data = json_decode(file_get_contents("php://input"), true);

    if ($data) {
        $txt = $data['txt'];
        $response = array(
            "message" => "Данные обработаны",
        );

        header("Content-Type: application/json");
        echo json_encode($response);
    } else {
        http_response_code(400);
        echo json_encode(array("error" => "Данные не были получены"));
    }
}
?>
