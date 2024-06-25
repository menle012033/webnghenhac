let trackList = [];
let currentIndex = -1;




function loadTrackByIndex(index) {
    if (index >= 0 && index < trackList.length) {
        let track = trackList[index];
        loadTrack(track.id, track.ten, track.casi, track.imageURL, track.audioURL);
        currentIndex = index;
    }
}

function loadTrack(id, ten, casi, imageURL, audioURL) {
    console.log('Track ID:', id, 'Tên:', ten, 'Ca sĩ:', casi, 'Image URL:', imageURL, 'Audio URL:', audioURL);
    
    // Cập nhật thông tin bài hát trên giao diện
    document.getElementById('track-art').src = imageURL;
    document.getElementById('track-name').innerText = ten;
    document.getElementById('track-artist').innerText = casi;
    
    // Cập nhật nguồn audio
    let audioPlayer = document.getElementById('audio-player');
    audioPlayer.src = audioURL;
    audioPlayer.load();
    
    // Tự động phát khi chuyển bài hát
    if (!audioPlayer.paused) {
        audioPlayer.play();
    }
}

function playpauseTrack() {
    var audio = document.getElementById('audio-player');
    var playButton = document.getElementById('play-button');
    var pauseButton = document.getElementById('pause-button');

    if (audio.paused) {
        audio.play();
        playButton.style.display = 'none';
        pauseButton.style.display = 'inline';
    } else {
        audio.pause();
        playButton.style.display = 'inline';
        pauseButton.style.display = 'none';
    }
}

function handlePlay() {
    var playButton = document.getElementById('play-button');
    var pauseButton = document.getElementById('pause-button');
    playButton.style.display = 'none';
    pauseButton.style.display = 'inline';
}

function handlePause() {
    var playButton = document.getElementById('play-button');
    var pauseButton = document.getElementById('pause-button');
    playButton.style.display = 'inline';
    pauseButton.style.display = 'none';
}

function nextTrack() {
    let nextIndex = currentIndex + 1;
    if (nextIndex >= trackList.length) {
        nextIndex = 0; // Quay lại bài hát đầu tiên nếu đang ở bài hát cuối cùng
    }
    loadTrackByIndex(nextIndex);
}

function prevTrack() {
    let prevIndex = currentIndex - 1;
    if (prevIndex < 0) {
        prevIndex = trackList.length - 1; // Quay lại bài hát cuối cùng nếu đang ở bài hát đầu tiên
    }
    loadTrackByIndex(prevIndex);
}

function randomTrack() {
    let randomIndex;
    do {
        randomIndex = Math.floor(Math.random() * trackList.length);
    } while (randomIndex === currentIndex); // Chọn ngẫu nhiên một bài hát khác so với hiện tại
    loadTrackByIndex(randomIndex);
}

function repeatTrack() {
    var audio = document.getElementById('audio-player');
    audio.loop = !audio.loop;
}

