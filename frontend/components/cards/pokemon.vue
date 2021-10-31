<template>
  <div class="col-md-3 col-lg-3">
    <div class="listing-row">
      <div class="listing-box-inner">
        <a class="listing-box-image">
          <span class="listing-box-image-content" v-bind:style="'background-image: url('+ image +')'"></span>
        </a>
        <div class="listing-row-content">
          <div class="listing-row-content-header">
            <h3>{{ name | capitalize }}</h3>
            <h4>height: {{ height }} weight: {{ weight }} </h4>
            <h4>type: {{ types | types_to_string }}</h4>
            <h4>evolution: {{ evolutions | evolutions_to_string }}</h4>
            <h4>abilities: {{ abilities | types_to_string }}</h4>
            <!-- /.actions -->
          </div>

          <!-- /.listing-row-content-body -->
        </div>
        <!-- /.listing-row-content -->
      </div>
      <!-- /.listing-row-inner -->
    </div>
  </div>
</template>

<script>
    export default {
        name: "pokemon-card",
        props: ['name', 'height', 'weight', 'image', "types", "abilities", "evolutions"],
        filters: {
          capitalize: function (value) {
            if (!value) return ''
            value = value.toString()
            return value.toUpperCase()
          },
          types_to_string: function (value) {
            let result = [];
            value.forEach((value, index) => {
              result.push(value.name);
            })
            return result.join(", ")
          },
          evolutions_to_string: function (value) {
            let result = [];
            value.forEach((value, index) => {
              result.push(value.name);
            })
            return result.join(" => ")
          }
        }
    }

</script>

<style scoped>
  .listing-row-image {
    min-width: 300px;
  }
  .listing-row-content-read-more .btn {
    background-color: #F74949;
    color: #fff;
  }
</style>
