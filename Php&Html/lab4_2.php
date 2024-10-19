<?php
 $pinName = 3;
 $pinVal = 0;
 $status = array();
 // set pin3 to output mode, read it current value
 system("gpio -g mode $pinName out");
 exec ("gpio -g read $pinName", $status);
 // Now $status[0] keep the value of pin 3
 $pinVal = $status[0]; // and so does $pinVal
 if ($pinVal) {
    echo "LED1 is OFF Now";
    system("gpio -g write 3 0" );
 }
 else {
 
 echo "LED1 is ON Now";
 system("gpio -g write 3 1" );
 }
?>