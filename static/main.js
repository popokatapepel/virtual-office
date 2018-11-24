/*
 *  Copyright (c) 2015 The WebRTC project authors. All Rights Reserved.
 *
 *  Use of this source code is governed by a BSD-style license
 *  that can be found in the LICENSE file in the root of the source
 *  tree.
 */

'use strict';

// Put variables in global scope to make them available to the browser console.
const video = document.querySelector('video');
const canvas = window.canvas = document.querySelector('canvas');
canvas.width = 0;
canvas.height = 0;

video.onclick = function() {
canvas.style.visibility="visible";
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;
  canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
  video.style.visibility="hidden";
    video.width = 0;
video.height = 0;
  setTimeout(function(){
    video.width = video.videoWidth;
  video.height = video.videoHeight;
  video.style.visibility="visible";
  canvas.style.visibility="hidden";
  canvas.width = 0;
canvas.height = 0;
   }, 3000);
};

const constraints = {
  audio: false,
  video: true
};

function handleSuccess(stream) {
  window.stream = stream; // make stream available to browser console
  video.srcObject = stream;

}

function handleError(error) {
  console.log('navigator.getUserMedia error: ', error);
}

navigator.mediaDevices.getUserMedia(constraints).then(handleSuccess).catch(handleError);
