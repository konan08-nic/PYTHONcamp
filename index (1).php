<?php
/*for($i=1;$i<=10;$i++)
    for ($j=0; $j <=10 ; $j++)  
     echo($i.'x'.$j.'='.$i*$j.'<br>'); */
     $tableau=[10,15,17,10,9];
    // var_dump($tableau);
    //echo $tableau[4];  
    //print_r($tableau);
    /*for ($i=0; $i <count($tableau) ; $i++) { 
        echo $tableau[$i].'--';


    }*/
    //$note=array('et1'=>17, 'et2'=>15, 'et3'=>15,18,'et1'=>13);
    //var_dump($note);
    //echo $note[0];
    //foreach ($note as $key => $value) {
        //echo $value .'--';
    //$tableau=[[1,2,3],[4,5,6],[7,8,9]];
    //var_dump($tableau);
    /*foreach($tableau as $value)
      foreach($value as $v)
      echo $v.'-- '; */
      $tableau= ['yao' => ['note1' => 10, 'note2' => 11, 'note3' => 13, 'moyenne' =>(10+11+13)/3 ],
      'koffi' => ['note1' => 15, 'note2' => 13, 'note3' => 11, 'moyenne' =>(15+13+11)/3],
      'yeo' => ['note1' => 14, 'note2' => 12, 'note3' => 11, 'moyenne' =>(14+12+11)/3],
      'Franck' => ['note1' => 12, 'note2' => 12, 'note3' => 14, 'moyenne' =>(12+12+14)/3]];
      foreach($tableau as $value)
        foreach($value as $v)
         echo $v.'-- ';
    
?>