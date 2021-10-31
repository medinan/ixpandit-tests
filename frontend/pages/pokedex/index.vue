<template>
  <div class="page-wrapper">
    <Menu></Menu>
    <Pokedex></Pokedex>
    <Footer></Footer>
  </div>

</template>

<script>
import Logo from '~/components/Logo.vue';
import Menu from '~/layouts/menu.vue';
import Footer from '~/layouts/footer.vue';
import Pokedex from '~/components/pokedex/pokedex';

export default {
  components: {
    Logo, Menu, Footer, Pokedex
  }
}
</script>

<style>
</style>
