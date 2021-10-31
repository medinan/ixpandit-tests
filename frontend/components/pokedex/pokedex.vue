<template>
  <div class="main-wrapper">
    <div class="main">
      <div class="main-inner">
        <div class="page-title">
          <div class="container">
            <h1>POKEDEX</h1>
            <!-- /.page-title-actions -->
          </div>
          <!-- /.container-->
        </div>
        <!-- /.page-title -->
        <div class="container">
          <nav class="breadcrumb">
            <a class="breadcrumb-item" href="/">Home</a>
            <span class="breadcrumb-item active">Pokedex</span>
          </nav>

          <div class="row">
            <PokemonCard v-for="adv in pokemons"
                            :name="adv.name"
                            :height="adv.height"
                            :weight="adv.weight"
                            :types="adv.types"
                            :evolutions="adv.evolutions"
                            :abilities="adv.abilities"
                            :image="adv.image"></PokemonCard>
          </div>
          <div class="row">
            <button type="submit" class="btn btn-primary pull-right">VER MAS</button>
          </div>
          <!-- /.row -->
        </div>
        <!-- /.container-fluid -->
      </div>
      <!-- /.main-inner -->
    </div>
    <!-- /.main -->
  </div>
</template>

<script>
  import PokemonCard from '~/components/cards/pokemon'
  export default {
    name: "Pokedex",
    components: {PokemonCard},
    mounted: function () {
      this.getpokemons();
    },
    data: function () {
      return {
        pokemons: []
      }
    },
    methods: {
      getpokemons: function () {
        const url = "/api/v1/pokemons/"
        let self = this;
        this.$axios.get(url, {
          dataType: "json",
          headers: {"Content-type": "application/json"}
        }).then(function (response) {
          console.log(response.data);
          self.pokemons = response.data.results;
        })
      }
    }
  }
</script>

<style scoped>

</style>
