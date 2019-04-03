var current_hole;

$(window).load(function(){
    //process players and assign teams
    if(players.length == 4){
        var values = find_high_low(players);

        var lowest = values[0];
        var highest = values[1];
        for(i = 0; i<players.length;i++){
            earnings[players[i].name] = 0;

            if(player[i].hcp == lowest || player[i].hcp == highest){
                players[i].team = 1;
            }
            else{
                players[i].team = 2;
            }
            player_order.push(players[i].team);
        }

        //table generation
        var table = document.getElementById("scorecard");

        for(i=0; i<players.length; i++){
            var row = table.insertRow(2);
            row.id = "player" + (i+1);

            var name = row.insertCell();
            name.innerHTML(players[i].name);

            var hcp = row.insertCell();
            hcp.innerHTML(players[i].hcp);

            var team = row.insertCell();
            team.innerHTML(players[i].team);

            for (j=1; j<19; j++){
                var hole = row.insertCell();
                hole.innerHTML("<input disabled class='input' id='" + "player" + (i+1)+"_"+ j + "'>");
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
        // noinspection JSAnnotator
        $(document).getElementById("player"+(i+1)).getElementById(index).disabled() = false;
    }
}
function disable_column(index){
    for (i=0; i<players.length; i++) {
        // noinspection JSAnnotator
        $(document).getElementById("player"+(i+1)).getElementById(index).disabled() = true;
    }
}

function advance_row(current_hole){
    for (i=0; i<players.length; i++) {
        if ($(document).getElementById("player"+(i+1)+"_"+current_hole).textContent == "") {
            continue;
        }
        else{
            alert("Please Fill Out the Entire Column");
            return false;
        }
    }
    //current_hole
    disable_column(current_hole);

    //advance 1 hole
    current_hole++;
    enable_column(current_hole);
    return current_hole;
}

//iterate through list and add same value, 0-> main game, anymore = presses
var games = [];
var earnings = {};

//update with infomation as it passes
var kps = [null, null, null];
var kp_hole = 0;
var player_order = [];

//positive = team1, negative = team2
function update_scores(){
  //retrieve all the values and sort into teams
  var team1_low, team1_hi, team2_low, team2_hi;
  var scores = [];

  //subtract 1 for hdcp
  for (i=0; i<players.length; i++) {
        // noinspection JSAnnotator
        scores.push(parseInt($(document).getElementById("player"+(i+1)).getElementById(current_hole).textContent));
    }

    var ordered_scores = player_order.map(function(e,i){
        return [e,scores[i]];
    });

  //check for kp's
    if(holes[current_hole-1].kp){
        var kp_player = kp();
        kps[kp_hole] = kp_player;
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
            if (players[i].name.equalTo(person)){
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