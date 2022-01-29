
var mysql = require('mysql');
var express = require('express')
var cors = require('cors');
var bodyParser = require('body-parser');  

var app = express()
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.use(cors());


var con = mysql.createConnection({
    host: "localhost",
    user: "root",
    port: "3306",
    password: "your_current_password",
    database: "booksystem"
});

con.connect(function (err) {
    if (err) throw err;
    console.log("Connected!");

});

app.get('/', function (req, res) {
    res.send('Hello World!');
});
app.post('/details',
    (req, res) => {app.use(bodyParser.json());
        app.use(bodyParser.json());

        console.log(req.body);
        var stock_name = req.body.stock_name;
        var price = req.body.price;
        var quantity =req.body.quantity;
        var type = req.body.type;
        

        var sql = "INSERT INTO stocks (stock_name, quantitiy, type, price ) VALUES ?";
        var values = [[stock_name,quantity,type, price ]];

        console.log(values);
        con.query(sql, [values],  (err, result) => {
            if (err) throw err;
            console.log("row created");
        });
        res.send('row inserted')
    });
app.listen(3000, () => "connected succesfully")