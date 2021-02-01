<template>
  <v-tooltip right>
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              v-bind="attrs"
              v-on="on"
              style="position: absolute; top: 0px; right: 0; margin: 5px"
              icon
              color="yellow darken-3"
              :class="{'v-btn--active':active}"
              @click="$emit('on-click');"
            >
              <v-icon>mdi-pencil</v-icon>
            </v-btn>
          </template>
          <span>Edit</span>
        </v-tooltip>
</template>

<script>
export default {
    props:['active']
}
</script>
