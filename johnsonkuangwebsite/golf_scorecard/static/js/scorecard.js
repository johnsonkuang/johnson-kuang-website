var current_hole;

$(window).load(function(){
    //process players and assign teams
    if(players.length == 4){
        var values = find_high_low(players);

        var lowest = values[0];
        var highest = values[1];
        for(i = 0; i<players.length;i++){

            if(players[i].hcp == lowest || players[i].hcp == highest){
                players[i].team = 1;
            }
            else{
                players[i].team = 2;
            }
            player_order.push(players[i].team);

            //initialize earnings
            earnings[players[i].name] = 0;
        }

        //table generation
        var table = document.getElementById("scorecard");

        for(i=0; i<players.length; i++){
            var row = table.insertRow(2);
            row.id = "player" + (i+1);

            var name = row.insertCell();
            name.innerHTML = players[i].name;

            var hcp = row.insertCell();
            hcp.innerHTML = players[i].hcp;

            var team = row.insertCell();
            team.innerHTML = players[i].team;

            for (j=1; j<19; j++){
                var hole = row.insertCell();
                hole.innerHTML = "<input disabled class='input' style='width: 50px;' id='" + "player" + (i+1)+"_"+ j + "'>";
            }
        }

        //initialize counter
        current_hole = 1;
        //enable columns
        enable_column(current_hole);


    }
    /* else if(players.length == 5){
        var values = find_high_low(players);

        var lowest = values[0];
        var highest = values[1];
        for(i = 0; i<players.length;i++){
            if(player[i].hcp == lowest || player[i].hcp == highest){
                players[i].team = 1;
            }
        }
    }
    else{

    }*/

    //generate the forms

});

function enable_column(index){
    for (i=0; i<players.length; i++) {
        var id = "player"+(i+1)+"_"+index;
        var player = document.getElementById(id);
        player.disabled = false;
    }
}
function disable_column(index){
    for (i=0; i<players.length; i++) {
        // noinspection JSAnnotator
        document.getElementById("player"+(i+1)+"_"+index).disabled = true;
    }
}

function advance_row(current_hole){

    //current_hole
    disable_column(current_hole);

    //advance 1 hole
    current_hole++;
    enable_column(current_hole);
    return current_hole;
}

//iterate through list and add same value, 0-> main game, anymore = presses
//initiallized with 0 in index 0, represents 0 game count
var games = [0];
var earnings = {};

//update with infomation as it passes
var kps = [null, null, null];
var kp_hole = 0;
var kp_count = 1;
var player_order = [];
var winners = [0,0];

function driver(){

    for (i=0; i<players.length; i++) {
        if (document.getElementById("player"+(i+1)+"_"+current_hole).value == "") {
            alert("Please Fill Out the Entire Column");
            return false;
        }
        else{
            continue;
        }
    }
    //first update the scores
    update_scores();
   //update visual information
    update_visuals(current_hole);

    //check back/front switch
    check_change(current_hole);




    //advance the row
    current_hole = advance_row(current_hole);

    //end game
    if (current_hole>18){
        end_game();
    }
}

function update_visuals(current_hole){
    var fb = "b";
    if(current_hole<10){
        fb = "f";
    }
    var table = document.getElementById("games" + fb);
    var game_row = document.getElementById("gameRow" + fb);
    
    //check if prev game_num = current number of games
    if (game_num != games.length){
        game_num++;
        var new_game = game_row.insertCell();
        new_game.innerHTML = "Press " + (game_num-1);
    } 

    //new row for new hole
    var new_row = table.insertRow();
    new_row.id = "game_hole"+ fb + current_hole;
    var hole = new_row.insertCell();

    hole.innerHTML = current_hole;

    for (i = 0; i<games.length; i++){
        var game = new_row.insertCell();
        game.innerHTML = games[i];
    }
}

//checks the back side
function check_change(current_hole){
    if(current_hole == 9){
        var winning_team;
        if (games[0] > 0){
            winning_team = 1;
        }
        else if (games[0] < 0) {
            winning_team = 2;
        }
        else{
            winning_team = 0;
        }
        //reset games
        games = [0];
        game_num = 1;

        for (var i = 0; i < players.length; i++){
                if (players[i].team == winning_team){
                    earnings[players[i].name] +=2;
                }
                else if(winning_team==0){
                    earnings[players[i].name] += 0;
                }
                else{
                    earnings[players[i].name] -=2;
                }
        }
    }
    else if(current_hole==18){
        var winning_team;
        if (games[0] > 0){
            winning_team = 1;
        }
        else if (games[0] < 0) {
            winning_team = 2;
        }
        else{
            winning_team = 0;
        }
        games = [0];
        for (var i = 0; i < players.length; i++){
                if (players[i].team == winning_team){
                    earnings[players[i].name] +=4;
                }
                else if(winning_team==0){
                    earnings[players[i].name] += 0;
                }
                else{
                    earnings[players[i].name] -=4;
                }
        }
    }
}

//end the game
function end_game(){
    var button = document.getElementById("end");

    button.disabled = false;
    //display ending game stats
    for(i = 0; i<players.length; i++){
        var money = earnings[players[i].name];
        var txt = players[i].name + ": $" + money;
        var li = document.getElementById("p"+(i+1));
        li.innerHTML = txt;
    }
}


//check num for number of games
var game_num = 1;

//positive = team1, negative = team2
function update_scores(){
  //retrieve all the values and sort into teams
  var team1_low, team1_hi, team2_low, team2_hi;
  var scores = [];

  //subtract 1 for hdcp
  for (i=players.length - 1; i > -1; i--) {
        // noinspection JSAnnotator
        scores.push(parseInt(document.getElementById("player"+(i+1)+"_"+current_hole).value));
    }

    var ordered_scores = player_order.map(function(e,i){
        return [e,scores[i]];
    });


  //check for kp's
    if(holes[current_hole-1].kp){
        var kp_player = kp();
        kps[kp_hole] = kp_player;
        var kp_display = document.getElementById("kp"+(kp_hole+1));
        if (kp_player != null){
            var txt = "";
            for (i = 0; i<kp_count;i++){
                txt += "*";
            }
            kp_display.innerHTML = kp_player.name + " " + txt;
            earnings[kp_player.name] += kp_count;

            kp_count = 1;

        }
        else{
            kp_display.innerHTML = "N/A";
            kp_count++;
        }

        kp_hole++;
    }
  var team1 = [];
  var team2 = [];

  ordered_scores.forEach(function(item){
     if (item[0]==1){
         team1.push(item[1]);
     }
     else{
         team2.push(item[1]);
     }
  });

    team1_hi = Math.max(...team1);
    team1_low = Math.min(...team1);

    team2_hi = Math.max(...team2);
    team2_low = Math.min(...team2);

    //compare values
    var update = 0;
    if(team1_hi > team2_hi){
        update++;
    }
    //what happens with ties again
    else{
        update--;
    }

    if (team1_low > team2_low){
        update++;
    }
    else{
        update--;
    }

    //get values
    //for presses
    for (var i = 0; i < games.length; i++){
        games[i] += update;
    }
    if (Math.abs(games[games.length-1]) >= 2) {
        games.push(0);
        
    }

}

function kp(){
    var txt = "";
    var names = [];
    players.forEach(function (element){
        names.push(element.name);
    });


    var person = prompt("Please enter the name of who got the kp (enter N/A if none did): ", "");
    if (person == null || person == ""){
        alert("User cancelled the prompt.");
        kp();
    }
    else if(person == "N/A"){
        return null;
    }

    else if(names.indexOf(person) == -1){

        for (var i = 0; i < names.length; i++){
            txt += names[i] + "\n";
        }
        alert("Sorry, the person that you entered is not in this game. Are you sure the player is part of this list? \n" + txt);
        kp();
    }

    else{
        for (var i = 0; i < players.length; i++){
            if (players[i].name == person){
                return players[i];
            }
        }
    }
}


function find_high_low(players){
        var lowest = 999999999999;
        var highest = 0;

        for (i = 0; i<players.length;i++){
            if(lowest > players[i].hcp)lowest = players[i].hcp;
            else if(highest < players[i].hcp)highest = players[i].hcp;
        }
        return [lowest, highest];
    }