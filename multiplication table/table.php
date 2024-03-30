<?php
$row = '';
$col = '';
$selectedColor = '';

$json = file_get_contents('colors.json');
$colors = json_decode($json, true);

if (isset ($_GET["row"]) && isset ($_GET["col"]) && $_GET["row"] !== "" && $_GET["col"] !== "") {
    $row = $_GET["row"];
    $col = $_GET["col"];
    if ((is_numeric($row) && ($row > 0 && $row < 100)) && (is_numeric($col) && ($col > 0 && $col < 100))) {
        $row = (int) $_GET["row"];
        $col = (int) $_GET["col"];
    }
} else {
    $row = 9;
    $col = 9;
}

if (isset ($_GET["color"])) {
    $selectedColor = $_GET["color"];
}
$table = '<table>';
$table .= '<tr style="background-color: ' . $selectedColor . ';">';
$table .= '<td> </td>';
for ($j = 1; $j <= $col; $j++) {
    $table .= '<td>' . $j . '</td>';
}
$table .= '</tr>';

for ($i = 1; $i <= $row; $i++) {
    $table .= '<tr>';
    $table .= '<td style="background-color: ' . $selectedColor . ';">' . $i . '</td>';
    for ($j = 1; $j <= $col; $j++) {
        $table .= '<td>' . $i * $j . '</td>';
    }
    $table .= '</tr>';
}
$table .= '</table>';
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Document</title>
</head>

<body>
    <h1>Таблица умножения</h1>
    <form action="" method="GET">
        <section class="inputs">
            <div class="container">
                <label for="row">Количество строк</label>
                <input type="number" name="row" id="" value=<?php echo $row ?>>
            </div>

            <div class="container">
                <label for="col">Количество столбцов</label>
                <input type="number" name="col" id="" value=<?php echo $col ?>>
            </div>

            <div class="container">
                <label for="color">Выберите цвет</label>
                <select name="color" id="color">
                    <?php
                    // Выводим опции для каждого цвета из JSON
                    foreach ($colors['soft_colors'] as $color) {
                        $colorName = $color['name'];
                        $colorBackground = $color['background'];
                        $colorTextColor = $color['text-color'];
                        $selected = ($colorName === $selectedColor) ? 'selected' : '';
                        echo '<option value="' . $colorBackground . '" style="background-color: ' . $colorBackground . '; color: ' . $colorTextColor . ';" ' . $selected . '>' . $colorName . '</option>';
                    }
                    ?>
                </select>
            </div>
        </section>

        <input type="submit" value="Сгенерировать таблицу">
    </form>

    <section class="table">
        <?php echo $table ?>
    </section>
</body>

</html>