<template>
  <div class="page-wrapper">
    <Menu></Menu>
    <Wellcome></Wellcome>
    <Footer></Footer>
  </div>

</template>

<script>
import Logo from '~/components/Logo.vue';
import Wellcome from '~/components/home/wellcome.vue';
import Menu from '~/layouts/menu.vue';
import Footer from '~/layouts/footer.vue';

export default {
  components: {
    Logo, Menu, Footer, Wellcome
  }
}
</script>

<style>
</style>
