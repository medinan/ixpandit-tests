<template>
  <div class="footer-wrapper">
    <div class="footer">
      <div class="footer-inner">
        <div class="container">
          <div class="row">
            <div class="col-lg-4">
              <div class="widget">
                <h3>
                  <img v-bind:src="require('../assets/img/logo.png')" alt="Home">
                </h3>
                <p>
                  Prueba tecnica de NESTOR MEDINA para ixpandit.
                </p>
                <ul class="social">
                  <li><a href="https://www.linkedin.com/in/nestor-orlando-medina-743933100/"><i class="fa fa-linkedin"></i></a></li>
                  <li><a href="https://github.com/medinan"><i class="fa fa-github"></i></a></li>
                </ul>
              </div>
            </div>
          </div>
          <!-- /.row -->
        </div>
        <!-- /.container -->
      </div>
      <!-- /.footer-inner -->
    </div>
    <!-- /.footer -->
  </div>
</template>

<script>
    export default {
        name: "footer"
    }
</script>

<style scoped>
  .footer-wrapper {
    background: rgb(255, 255, 255)
  }
</style>
