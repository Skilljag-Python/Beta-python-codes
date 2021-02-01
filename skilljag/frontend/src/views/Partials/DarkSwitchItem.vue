
<template>
  <v-list-item>
    <v-list-item-action>
      <v-switch
        v-model="$vuetify.theme.dark"
        @change="setDark"
        color="purple"
      ></v-switch>
    </v-list-item-action>
    <v-list-item-title>Dark mode</v-list-item-title>
  </v-list-item>
</template>

<script>
export default {
  methods: {
    setDark(v) {
        console.log(v);
      localStorage.setItem("dark", v);
    },
  },
};
</script>
