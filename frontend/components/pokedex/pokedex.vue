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
          <div class="row mb80">
            <div class="col-sm-4 offset-sm-4">
              <div class="input-group mb-3">
                <input type="text" v-model="search_form.name" class="form-control" placeholder="Search pokemon" aria-label="Recipient's username" aria-describedby="basic-addon2">
                <div class="input-group-append">
                  <button class="btn btn-outline-secondary btn-primary" type="button" @click="getPokemon">Buscar</button>
                </div>
              </div>
            </div>
          </div>
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
          <div class="row align-content-center" v-show="is_more">
            <div class="col text-center">
              <button type="submit" class="btn btn-primary" @click="getMorePokemon">VER MAS</button>
            </div>

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
      this.getPokemon();
    },
    data: function () {
      return {
        pokemons: [],
        is_more: false,
        next_url: null,
        search_form: {
          name: null
        }
      }
    },
    methods: {
      getPokemon: function () {
        const url = "/api/v1/pokemons/"
        let self = this;
        let params = {name: this.search_form.name}
        this.$axios.get(url, {
          dataType: "json",
          headers: {"Content-type": "application/json"},
          params: params
        }).then(function (response) {
          console.log(response.data);
          self.pokemons = response.data.results;
          self.is_more = !(response.data.next  === null);
          self.next_url = response.data.next;
        })
      },
      getMorePokemon: function () {
        const url = this.next_url;
        let self = this;
        this.$axios.get(url, {
          dataType: "json",
          headers: {"Content-type": "application/json"}
        }).then(function (response) {
          console.log(response.data);
          self.pokemons = [].concat(self.pokemons, response.data.results);
          self.is_more = !(response.data.next  === null);
          self.next_url = response.data.next;
        })
      },
    }
  }
</script>

<style scoped>

</style>
