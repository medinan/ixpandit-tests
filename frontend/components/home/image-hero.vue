<template>
  <div class="hero-image-wrapper">
    <div id="carousel-example-1z" class=" hero-image-src carousel slide carousel-fade" data-ride="carousel">
      <!--Indicators-->
      <ol class="carousel-indicators">
        <li data-target="#carousel-example-1z" data-slide-to="0" class="active"></li>
        <li data-target="#carousel-example-1z" data-slide-to="1"></li>
        <li data-target="#carousel-example-1z" data-slide-to="2"></li>
      </ol>
      <!--/.Indicators-->
      <!--Slides-->
      <div class="carousel-inner" role="listbox">
        <!--First slide-->
        <div class="carousel-item active">
          <img class="d-block w-100" src="~assets/img/example/covers/image_1.png" alt="First slide">
        </div>
        <!--/First slide-->
        <!--Second slide-->
        <div class="carousel-item">
          <img class="d-block w-100" src="~assets/img/example/covers/image_2.png" alt="Second slide">
        </div>
        <!--/Second slide-->
        <!--Third slide-->
        <div class="carousel-item">
          <img class="d-block w-100" src="~assets/img/example/covers/image_3.png" alt="Third slide">
        </div>
        <!--/Third slide-->
      </div>
      <!--/.Slides-->
      <!--Controls-->
      <a class="carousel-control-prev" href="#carousel-example-1z" role="button" data-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="sr-only">Previous</span>
      </a>
      <a class="carousel-control-next" href="#carousel-example-1z" role="button" data-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="sr-only">Next</span>
      </a>
      <!--/.Controls-->
    </div>
    <!-- /.hero-image-src -->
    <div class="hero-image-filter-wrapper">
          <div class="container">
            <div class="hero-image-filter">
              <div class="form-group">
                <input type="text" class="form-control" placeholder="Search by keyword">
              </div>
              <!-- /.form-group -->
              <div class="form-group">
                <select class="form-control">
                  <option>Chicago</option>
                  <option>San Francisco</option>
                  <option>Seattle</option>
                  <option>New York</option>
                  <option>Washington</option>
                </select>
              </div>
              <!-- /.form-group -->
              <div class="form-group">
                <input type="text" class="form-control" placeholder="Starting price">
              </div>
              <!-- /.form-group -->
              <div class="form-group">
                <input type="text" class="form-control" placeholder="Starting price">
              </div>
              <!-- /.form-group -->
              <div class="form-group-btn">
                <button type="submit" class="btn">Filter Listings</button>
              </div>
              <!-- /.form-group -->
            </div>
            <!-- /.hero-image-filter -->
          </div>
          <!-- /.container -->
        </div>
  </div>
  <!-- /.hero-image-wrapper -->
</template>

<script>
    export default {
        name: "image-hero"
    }
</script>

<style scoped>

</style>
