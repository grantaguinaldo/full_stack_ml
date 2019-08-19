// Code works if placed directly into the HTML oage.
// Problem linking .js file from within the Jinja template.

// Select DOM elements and assign to variables.
var $petalWidth = document.getElementById('_petalWidth');
var $petalLength = document.getElementById('_petalLength');
var $sepalWidth = document.getElementById('_sepalWidth');
var $sepalLength = document.getElementById('_sepalLength');
var $searchBtn = document.getElementById('searchBtn');
var $eraseBtn = document.getElementById('eraseBtn');

// Add event listeners and assign to functions.
$searchBtn.addEventListener("click", predictClick);
$eraseBtn.addEventListener("click", eraseData);


// Build out functions to erase data from forms.
function eraseData(){

    $petalWidth.value = '';
    $petalLength.value = '';
    $sepalWidth.value = '';
    $sepalLength.value = '';
    // TODO: Need to clear out the inner HTML from the prediction.
};

// Build out functions to take data in form and make prediction.
function predictClick(){

    var petalWidthValue = $petalWidth.value;
    var petalLengthValue = $petalLength.value;
    var sepalWidthValue = $sepalWidth.value;
    var sepalLengthValue = $sepalLength.value;
    var connectionString = 'prediction?sepallen='
                            + sepalWidthValue + '&'
                            + 'sepalwid=' + sepalWidthValue + '&'
                            + 'petallen=' + petalLengthValue + '&'
                            + 'petalwid=' + petalWidthValue;

    // console.log(connectionString);

    Plotly.d3.json(connectionString, function(error, response) {
      if (error) return console.warn(error);

    // Contains JSON response.
    console.log(response);
    });
};
