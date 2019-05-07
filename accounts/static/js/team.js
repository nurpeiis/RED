function showImage(imgName,membername,title,description,linkedin) {
    var container = document.getElementById('largeImg-text');
    document.getElementById('largeImg').src = imgName;
    document.getElementById('largeImg-name').innerHTML = membername;
    document.getElementById('largeImg-title').innerHTML = title;
    document.getElementById('largeImg-description').innerHTML = description;
    document.getElementById('largeImg-linkedin').innerHTML = linkedin;
    // var dscrpt = document.createTextNode(description);
    // container.appendChild(dscrpt);

    showLargeImagePanel();
  }
  
  function showLargeImagePanel() {
    document.getElementById('largeImagePanel').style.visibility = 'visible';
  }
  
  function hideMe() {
    document.getElementById('largeImagePanel').style.visibility = 'hidden';
  }
  