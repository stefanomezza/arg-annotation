var MODE = "ANNOTATE_NEW"
var debates = []
var current_idx = -1

$(document).ready(function(){
    console.log("Loading debates...")
    load_debates().then((dbs) =>
    {
        if (MODE == "ANNOTATE_NEW")
            dbs = Object.keys(dbs)
                  .filter((d) => dbs[d]['argumentativeness'].length == 0)
                  .reduce((obj, key) => {
                    obj[key] = dbs[key];
                    return obj;
                  }, {});
        debates = dbs
        current_idx = 0
        show_current_debate()
    })
})

load_debates = () => {
    return new Promise((resolve, reject) => {
        fetch("http://127.0.0.1:1234/get_data")
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
        console.log("FINISHED")
        var k = Object.keys(debates)[current_idx]
        debates[k]['relevance'].push($(".chosen[q=1]").attr("answer"))
        debates[k]['argumentativeness'].push($(".chosen[q=2]").attr("answer"))
        debates[k]['factuality'].push($(".chosen[q=3]").attr("answer"))
        debates[k]['best_overall'].push($(".chosen[q=4]").attr("answer"))
        var obj = {}
        obj[k] = debates[k]
        fetch("http://127.0.0.1:1234/send_response", {
                method: "POST",
                contentType: "application/json",
                body: JSON.stringify(obj)
            }
        ).then((r) => r.json())
        .then((j) => {
            console.log(j);
            current_idx = current_idx + 1
            show_current_debate()
        })
    }
}
show_current_debate = () => {
    var debate = debates[Object.keys(debates)[current_idx]];

    $(".chosen").removeClass("chosen")
    $("#chat-box").html("")
    $("#response-chat-box").html("")

    debate['history'] = debate['history'].slice(-3)
    var speaker_idx = 1
    for (var h of debate['history']){
        $("#chat-box").append(`
        <div class='chat-turn'>
            <div class="chat-message bot-message">
                Speaker ${speaker_idx}:
            </div>
            <div class="chat-message user-message">
                    ${h[0]}
        </div>`)
        speaker_idx += 1;
    }

    $("#response-chat-box").append(`
    <div class='chat-turn'>
        <div class="chat-message bot-message" id="response1">
            Response A:
        </div>
        <div class="chat-message resp-message resp-1">
                ${debate['pred_1']}
    </div>`)

    $("#response-chat-box").append(`
    <div class='chat-turn'>
        <div class="chat-message bot-message"  id="response2">
            Response B:
        </div>
        <div class="chat-message resp-message resp-2">
                ${debate['pred_2']}
    </div>`)
}