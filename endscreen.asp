<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Lato:wght@300&display=swap" rel="stylesheet">

  <style>
      body {
          margin: 0;
          font-family: 'Lato', sans-serif;
          color: white;
          background: #202731;
      }

      section{
          position: relative;
          display: flex;
          flex-direction: column;
          align-items: center;
          min-height: 50px;
          padding: 100px 20vw;
      }

      .blue {background: #4682b4;}
      .red {background: indianred;}
      .green {background: seagreen;}
      .dark {background: slategray;}

      .center {
          display: block;
          margin-left: auto;
          margin-right: auto;
          width: 50%;
          text-align:center;
          padding: 5px;
      }

      .button {
          background-color: #4caf50; /* Green */
          border: none;
          border-radius:10px;
          color: white;
          padding: 15px 32px;
          text-align: center;
          text-decoration: none;
          display: inline-block;
          font-size: 16px;
      }

      .button:hover {
          background-color:#235324;
          transition: 0.2s;
      }

      .button:active {
          background-color: #143115;
      }

      .column {
          float: left;
          width: 33.33%;
          padding: 5px;
      }

      /* Clearfix (clear floats) */
      .row::after {
          content: "";
          clear: both;
          display: table;
      }

  </style>

  <script>
    var container = window.open('', '', 'height=400,width=800');
    container.document.write('<html><head><title>DIV Contents</title>');
    container.document.write('</head><body >');
    container.document.write(<data value=""></data>)

    $(document).ready(function(){
      $.get("GetTally", null, function(data, status){
        console.log(data);
        container.print();
      });
    });
  </script>

</head>

<body>

  <div id="Results">
    <div class="center">

      <p>This is a test</p>


    </div>
  </div>

</body>
</html>
