<template>
  <div class="header-wrapper primary-nav-wrapper affix-top">
      <div class="header">
        <div class="container">
          <div class="header-inner">
            <div class="navigation-toggle toggle">
              <span></span>
              <span></span>
              <span></span>
            </div>
            <div class="header-logo">
              <a href="/">
                <img v-bind:src="require('../assets/img/logo.png')" alt="Home">
              </a>
            </div>
            <div class="header-nav">
              <div class="primary-nav-wrapper">
                <ul class="nav">
                  <li class="nav-item">
                    <a href="/pokedex/" class="nav-link active">Pokedex</a>
                  </li>

                </ul>
              </div>
            </div>

          </div>
        </div>
      </div>
    </div>
</template>

<script>
    export default {
        name: "menu",
        data () {
          return {

          }
        },
        mounted() {
            $('.navigation-toggle').on('click', function(e) {
                e.preventDefault();
                $('body').toggleClass('navigation-open');
            });
        }
    }
</script>

<style scoped>
  .header-wrapper {
    background: rgb(255, 255, 255);
  }
  .header-light .primary-nav-wrapper .nav-link {
    color: rgba(17, 17, 17, 0.07);
  }
</style>
