<?php
 $pinName = 3;

 $status= $_GET["led1"];
 system("gpio -g mode $pinName out");

 if ($status=="on")
 {
   echo "LED1 is now on";
   system("gpio -g write $pinName 1" );
 }

 if ($status=="off")
 {
   echo "LED1 is now off";
   system("gpio -g write $pinName 0" );
 }
