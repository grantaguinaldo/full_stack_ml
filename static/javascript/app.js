// Select DOM elements and assign to variables.
var $petalWidth = document.getElementById('_petalWidth');
var $petalLength = document.getElementById('_petalLength');
var $sepalWidth = document.getElementById('_sepalWidth');
var $sepalLength = document.getElementById('_sepalLength');
var $searchBtn = document.getElementById('searchBtn');

// Add event listeners and assign to functions.
$searchBtn.addEventListener("click", predictClick);
$eraseaBtn.addEventListener("click", eraseData);

// Build out functions to erase data from forms.
function eraseData(){

    $petalWidth.value = '';
    $petalLength.value = '';
    $sepalWidth.value = '';
    $sepalLength.value = '';
};

// Build out functions to take data in form and make prediction.
function predictClick(){

    var petalWidthValue = $petalWidth.value;
    var petalLengthValue = $petalLength.value;
    var sepalWidthValue = $sepalWidth.value;
    var sepalLengthValue = $sepalLength.value;

    console.log(petalWidthValue);
    console.log(petalLengthValue);
    console.log(sepalWidthValue);
    console.log(sepalLengthValue)
};

