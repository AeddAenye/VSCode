<?php

class Player{
    private $name;
    private $money;
    private $side;

    function __construct($name, $side, $money=100){
        $this->name = $name;
        $this->money = $money;
        $this->side = $side;
}

function getName(){
    return $this->name;
}

function getMoney(){
    return $this->money;
}

function giveCoin(){
    $this->money -=1;
}

function takeCoin(){
    $this->money +=1;
}

function getSide(){
    return $this->side;
}
}

class Game{
    protected $firstPlayer;
    protected $secondPlayer;

    

    function __construct($firstPlayer, $secondPlayer){
        $this->firstPlayer = $firstPlayer;
        $this->secondPlayer = $secondPlayer;
}

    function flipCoin(){
        return rand(0,1) ? 'Heads' : 'Tails';
}

    function startGame(){
        $player1 = $this->firstPlayer;
        $player2 = $this->secondPlayer;
        $counter = 0;
        $BR = PHP_EOL;

        function step( Player $winner, Player $looser ){
            $winner->takeCoin();
            $looser->giveCoin();
        }

        while ($player1->getMoney() != 0 && $player2->getMoney() != 0){
            $coinSide = $this->flipCoin();
            if($player1->getSide() == $coinSide){
                step( $player1, $player2);
                echo "{$player1->getName()} took the coin";
            } else {
                step( $player2, $player1);
                echo "{$player2->getName()} took the coin";
            }
            $counter +=1;
            echo $BR;
    }

    if($player1->getMoney() == 0){
        echo "{$player2->getName()} win".$BR;
    } else {
        echo "{$player1->getName()} win".$BR;
    }

    echo $BR."Coin tosses: " . $counter;

}
}

$player1 = new Player($name = 'Alex', $side = 'Heads');
$player2 = new Player($name = 'Mike', $side = 'Tails');

$game = new Game($player1, $player2);

$game->startGame();