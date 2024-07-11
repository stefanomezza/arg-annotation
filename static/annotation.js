var debates = []
var current_idx = -1
var password = window.location.href.split("=")[window.location.href.split("=").length - 1]
$(document).ready(function(){
    console.log("Loading debates...")
    load_debates().then((dbs) =>
    {
        if(dbs['res'] == 'ok'){
            dbs = dbs['data']
            frontend_dbs = {}
            for (var experiment_key of Object.keys(dbs)){
                for (var experiment_idx of Object.keys(dbs[experiment_key])){
                    if (dbs[experiment_key][experiment_idx]['argumentativeness'].length == 0){
                            frontend_dbs[`${experiment_key}__${experiment_idx}`] = dbs[experiment_key][experiment_idx]
                    }
                }
            }
            debates = frontend_dbs
            current_idx = Object.keys(debates)[0]
            show_current_debate()
        }
        else{
            alert("Wrong URL -- Please check again or contact s.mezza@unsw.edu.au")
        }
    })
})

load_debates = () => {
    return new Promise((resolve, reject) => {
        fetch("http://66.29.151.195:1234/get_data", {
            method: "POST",
            contentType: "application/json",
            body: JSON.stringify({"pass": password})
        })
        .then((d) => d.json())
        .then((r) => resolve(r))
    })
}
choose = () => {
    var button_id = event.target.id;
    var button_q = $("#"+button_id).attr("q")
    $("[q="+button_q+"]").removeClass("chosen")
    $("#"+button_id).addClass("chosen")
    $("#"+button_id).blur()
    if ($(".chosen").length == 4){
        var k = current_idx
        debates[k]['relevance'].push($(".chosen[q=1]").attr("answer"))
        debates[k]['argumentativeness'].push($(".chosen[q=2]").attr("answer"))
        debates[k]['factuality'].push($(".chosen[q=3]").attr("answer"))
        debates[k]['best_overall'].push($(".chosen[q=4]").attr("answer"))
        var obj = {}
        obj['response'] = {}
        obj['response'][k] = debates[k]
        obj['pass'] = password
        fetch("http://66.29.151.195:1234/send_response", {
                method: "POST",
                contentType: "application/json",
                body: JSON.stringify(obj)
            }
        ).then((r) => r.json())
        .then((j) => {
            console.log(j['res']);
            if (j['res'] == 'ok'){
                current_idx = Object.keys(debates)[
                    Object.keys(debates).findIndex(
                        (exp_idx) => debates[exp_idx]['argumentativeness'].length == 0
                    )
                ]
                if (current_idx == null)
                    alert("Annotation experiment is finished! Please contact s.mezza@unsw.edu.au to conclude the experiment.")
                else
                    show_current_debate()
            }
            else{
                alert("An error has occurred during the submission. Please interrupt the annotation and contact s.mezza@unsw.edu.au")
            }
        })
        .catch((error) => alert(`Error: ${error}. Please interrupt the annotation and contact s.mezza@unsw.edu.au.`))
    }
}
show_current_debate = () => {
    var debate = debates[current_idx];

    $(".chosen").removeClass("chosen")
    $("#chat-box").html("")
    $("#response-chat-box").html("")

//    debate['history'] = debate['history'].slice(-3)
    var speaker_idx = 0
    for (var h of debate['history']){
        if(speaker_idx == 0){
            $("#chat-box").append(`
            <div class='chat-turn topic-turn' id='chat-topic'>
                <div class="chat-message user-message  topic-turn-text">
                       <b>DEBATE TOPIC</b>: ${h[0]}
            </div>`)
            topic = false
        }
        else{
            $("#chat-box").append(`
            <div class='chat-turn' id='chat-turn-${speaker_idx}'>
                <div class="chat-message bot-message">
                    Speaker ${speaker_idx}:
                </div>
                <div class="chat-message user-message">
                        ${h[0]}
            </div>`)
        }
        if (speaker_idx < 3 && speaker_idx > 0){
            $("#chat-box").append(`<img src='static/arrowdown.png' class='downarrow'></img>`)
        }
        speaker_idx += 1;
    }

    $("#response-chat-box").append(`
    <div class="chat-message bot-message" style='margin-left:145px;display:inline-block;'>
        Speaker 4:
    </div>
    <div id='responses' style='display: inline-block; width:76%; vertical-align: top;'>
        <div class='chat-turn system-response'>
            <div class="chat-message bot-message" id="response1">
                Response A:
            </div>
            <div class="chat-message resp-message resp-1">
                    ${debate['pred_1']}
            </div>
        </div>
        <div class='chat-turn  system-response'>
            <div class="chat-message bot-message"  id="response2">
                Response B:
            </div>
            <div class="chat-message resp-message resp-2">
                    ${debate['pred_2']}
            </div>
        </div>
    </div>`)
    if (debate['move'] == "Attack")
        $("#movespan").html(" opposing ")
    else
        $("#movespan").html(" supporting ")
}
