<?php
$first = $_POST['first'] ?? '';
$second = $_POST['second'] ?? '';
$mathsym = $_POST['mathsym'] ?? '';
$result = '';

if (isset($_POST['submit']) && $first && $second && $mathsym) {
    $result = eval("return $first $mathsym $second;");
}
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Калькулятор</title>
    <style>
        h1 {
            text-align: center;
        }

        input,
        select {
            border-radius: 10px;
            border: 1px solid rgba(0, 0, 0, 0.297);
            padding: 10px;
            background-color: white;
            font-size: 2rem;
            text-align: center;
        }

        section.action {
            display: flex;
            justify-content: center;
            gap: 20px;
        }

        section.action * {
            flex-grow: 1;
        }

        form {
            display: flex;
            justify-content: center;
            flex-direction: column;
            gap: 20px;
        }
    </style>
</head>

<body>
    <h1>Калькулятор</h1>
    <form action="" method="post">
        <section class="action">
            <input type="number" name="first" value="<?php echo $first; ?>">
            <select name="mathsym" id="">
                <option value="+" <?php if ($mathsym === '+') echo 'selected'; ?>>+</option>
                <option value="-" <?php if ($mathsym === '-') echo 'selected'; ?>>-</option>
                <option value="*" <?php if ($mathsym === '*') echo 'selected'; ?>>*</option>
                <option value="/" <?php if ($mathsym === '/') echo 'selected'; ?>>/</option>
            </select>
            <input type="number" name="second" value="<?php echo $second; ?>">
        </section>
        <input type="submit" name="submit" value="=">
    </form>

    <?php if ($result !== ''): ?>
        <h1>Результат: <?php echo $result; ?></h1>
    <?php endif; ?>
</body>`

</html>
