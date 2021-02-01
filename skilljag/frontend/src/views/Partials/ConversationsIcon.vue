<template>
  <v-tooltip v1-model="show" bottom>
    <template v-slot:activator="{ on, attrs }">
      <v-btn
        to="/conversations"
        icon
        text
        v-bind="attrs"
        v-on="on"
        class="ma-1"
      >
        <v-icon color="grey lighten-1"> mdi-message-minus-outline </v-icon>
      </v-btn>
    </template>
    <span>Messages</span>
  </v-tooltip>
</template>

<script>
export default {
 
};
</script>
