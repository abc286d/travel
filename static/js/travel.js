function openWindow() {
    document.getElementById('light').style.display = 'block';
    document.getElementById('fade').style.display = 'block';
}

function closeWindow() {
    document.getElementById('light').style.display = 'none';
    document.getElementById('fade').style.display = 'none';
}

//这些图片的地址都可能有问题
function changelike() {
    document.getElementById("liking").src = "img/likered.png";
}

function biglike() {
    if (document.getElementById("liking").src != "static/img/likered.png") {
        document.getElementById("liking").src = "img/likebig.png";
    }
}

function smalllike() {
    if (document.getElementById("liking").src != "img/likered.png") {
        document.getElementById("liking").src = "img/like.png";
    }
}