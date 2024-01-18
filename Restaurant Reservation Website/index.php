<!DOCTYPE HTML>
<html lang="ru">
  <head>
    <meta charset="utf-8">
    <title>Tabl.Link App</title>
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <?php
      include "components/header.php";
    ?>

    <div class="main_content">
      <?php
      
      require_once 'components/db_connect.php';
      $query = "SELECT * FROM restaurants";
      $rnum = 0;
      $rest = array();
      if ($result = mysqli_query($link, $query)) {
          $rnum = mysqli_num_rows($result);
          for ($i=0; $i<$rnum; $i++) {
              $row = mysqli_fetch_array($result, MYSQLI_ASSOC);
              $rest[$i]=$row;
          }
          mysqli_free_result($result);
      }
      mysqli_close($link);
      
      
        include "components/restaurant_list.php";
      ?>
    </div>

    <?php
      include "components/footer.php";
    ?>
  </body>
</html>
