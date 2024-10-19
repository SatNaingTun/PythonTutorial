<?php
 $led1=3;
 $led2=4;
 $led3=17;
 $led4=27;
 $ledRun;
 $status = array();

 $ledName= $_GET["id"];

switch ($ledName) {
case "led1":
// echo "led1";
    $ledRun=$led1;break;
case "led2":
    $ledRun=$led2;break;
case "led3":
    $ledRun=$led3;break;
break;
case "led4":
    $ledRun=$led4;break;
break;
// default:
// echo "i is not equal to 0, 1, or 2";
}

system("gpio -g mode $ledRun out");
exec ("gpio -g read $ledRun", $status);
echo $status[0];

 $changeStatus= $_GET["status"];
 system("gpio -g mode $ledRun out");

 if ($changeStatus=="on")
 {
   echo "LED1 is now on";
   system("gpio -g write $ledRun 1" );
 }

 if ($changeStatus=="off")
 {
   echo "LED1 is now off";
   system("gpio -g write $ledRun 0" );
 }