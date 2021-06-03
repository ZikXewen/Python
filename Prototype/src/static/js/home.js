var _stream;
var audio_context;
var recorder;
var recordList = document.getElementById("recordList");
function startRecord(button) {
  navigator.getUserMedia(
    { audio: true },
    function (stream) {
      _stream = stream;
      audio_context = new AudioContext();
      var input = audio_context.createMediaStreamSource(stream);
      recorder = new Recorder(input);
      console.log("start");
      recorder.record();
      button.disabled = true;
      button.nextElementSibling.disabled = false;
    },
    function () {
      console.log("No Audio Input");
    }
  );
}
function stopRecord(button) {
  recorder.stop();
  button.disabled = true;
  button.previousElementSibling.disabled = false;
  recorder.exportWAV(createDownloadLink);
  recorder.clear();
  _stream.getAudioTracks()[0].stop();
}
function createDownloadLink(blob) {
  var url = URL.createObjectURL(blob);
  var li = document.createElement("li");
  var au = document.createElement("audio");
  var hf = document.createElement("a");
  au.controls = true;
  au.src = url;
  hf.href = url;
  hf.download = new Date().toISOString() + ".wav";
  hf.innerHTML = "<i class='bi bi-download'></i>";
  hf.className = "mx-3";
  li.className = "mx-3";
  li.className = "list-group-item bg-dark mx-3 my-1 py-3";
  li.appendChild(au);
  li.appendChild(document.createElement("br"));
  li.appendChild(hf);
  recordList.appendChild(li);
}
