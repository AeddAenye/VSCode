<?php

$connect = mysql_connect("172.21.0.2", "root", "RB.inhl20!", "Module 2");

$method = $_SERVER['REQUEST_METHOD'];

if ($method == 'POST'){
    $data = $_POST;
    $user_email = $data['email'];
    $user_password = $data['password'];

    $check_user = mysqli_query($connect, "SELECT * FROM `users` WHERE `email` = '$user_email' AND `password` = '$user_password'");
    if($check_user && mysqli_num_rows($check_user) > 0){
        $token = hash('sha256', $user_email.$user_password);
        $response = [
            'success' => true,
            'message' => 'Success',
            'token' => $token
        ];

        http_response_code(200);
    } else {
        $response = [
            'success' => false,
            'message' => 'Error'
        ];
        http_response_code(401);
    }

    header('Content-Type: application/json');
    echo json_encode($response);
}