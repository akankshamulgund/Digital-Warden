<?php
    if (isset($_POST["submit"])) {
        // Specify the target directory to save the uploaded video
        $targetFile =basename($_FILES["videoFile"]["name"]);

        ini_set('max_execution_time', 60); // Set maximum execution time to 60 seconds

        // Move the uploaded file to the target directory
        if (move_uploaded_file($_FILES["videoFile"]["tmp_name"], $targetFile)) {
            $fname=$_FILES["videoFile"]["name"];
            $ans = trim(shell_exec("python prediction.py $fname"));
        } else {
            echo "Sorry, there was an error uploading your file.";
        }
    }
?>


<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Deep Fake Video Detection</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
  <style>
    body {
      background-color: #f8f9fa;
    }
    
    .container2 {
      max-width: 500px;
      margin: 100px auto;
      padding: 30px;
      background-color: #fff;
      border-radius: 10px;
      box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    }
    
    .form-title {
      text-align: center;
      font-size: 24px;
      font-weight: bold;
      margin-bottom: 30px;
    }
    
    .navbar-brand {
      display: flex;
      font-size: 28px;
      font-weight: bold;
      justify-content: center;
      width: 100%;
    }

    .btn-primary {
      width: 100%;
    }

    .header {
      text-align: center;
      font-size: 28px;
      font-weight: bold;
      margin-bottom: 20px;
    }
    
    .content {
      text-align: justify;
      font-size: 18px;
      line-height: 1.6;
      margin-bottom: 40px;
    }

    .result {
      margin-top: 30px;
      text-align: center;
      font-size: 20px;
      font-weight: bold;
    }

    .video-preview {
      margin-top: 20px;
      text-align: center;
    }

    .video-preview video {
      max-width: 100%;
    }

    .container3{
      margin:0 120px;
    }

  </style>
</head>
<body>
<nav class="navbar navbar-dark bg-dark">
<div class="container">
<span class="navbar-brand text-center">Deep Fake Video Detection</span>
  </div>
</nav>
  <div class="container2">
    <h2 class="form-title">Deep Fake Video Detection</h2>
    <form action="" method="post" enctype="multipart/form-data">
      <div class="mb-3">
        <label for="videoFile" class="form-label">Upload Video</label>
        <input type="file" class="form-control" id="videoFile" name="videoFile" accept="video/*" oninput="previewVideo()" required>
      </div>
      <button type="submit" name="submit" class="btn btn-primary">Detect</button>
    </form>
    <div class="video-preview" id="videoPreview"></div>
  </div>

<?php if(isset($ans)): ?>
<div class="container3">
  

  <?php 
  if(strtolower($ans) === "fake"){ ?>
<h1 style="color:red;">The Input Video is : <?=$ans?></h1>
  <div class="content">

  </div>
    <?php }else{ ?>
      <h1 style="color:green;">The Input Video is : <?=$ans?></h1>
    <?php } ?>
</div>
    
<?php endif; ?>

<div class="container3">
</div>
  <!-- <script>
      function previewVideo() {
        var fileInput = document.getElementById("videoFile");
        var file = fileInput.files[0];
        
        if (file) {
          var video = document.createElement("video");
          video.src = URL.createObjectURL(file);
          video.controls = true;
          video.style.maxWidth = "100%";
          
          var videoPreview = document.getElementById("videoPreview");
          videoPreview.innerHTML = "";
          videoPreview.appendChild(video);
        }
      }
    </script> -->
</body>
</html>