<html>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tugas 5 PBW - Muhammad Reynaldo Aulia Rachman</title>
</head>

<body>
    <h1>Aplikasi Penghitung BMI</h1>
    <form method="POST" action="index.php">
        Berat Badan (kg) :
        <input type="number" name="berat">
        <br>
        <br>
        Tinggi Badan (cm) :
        <input type="number" name="tinggi">
        <BR></BR>
        <button type="submit" >Hitung BMI</button>
    </form>


    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $beratBadan = $_POST['berat'];
        $tinggiBadan = $_POST['tinggi'];

        $tinggiMeter = $tinggiBadan / 100;
        $bmi = $beratBadan / ($tinggiMeter * $tinggiMeter);

        echo '<h1> Hasil Perhitungan :</h1> ';
        echo 'Berat Badan : ', $beratBadan, ' kg <br>';
        echo 'Tinggi Badan : ', $tinggiBadan, ' cm <br>';
        echo 'BMI : ', number_format($bmi, 2), '<br>';
        if ($bmi < 18.5) {
            echo "Kategori BMI : Underweight";
        } else if ($bmi > 18.5 && $bmi < 24.9 ) {
            echo "Kategori BMI : Normal";
        } else if ($bmi > 24.9 && $bmi < 29.9 ) {
            echo "Kategori BMI : Overweight";
        } else if ($bmi > 29.9 && $bmi < 34.9 ) {
            echo "Kategori BMI : Obese";
        } else {
            echo "Kategori BMI : Extremely Obese";
        }
    }

    ?>

</body>

</html>