<template>
  <v-tooltip close-delay="100" bottom>
    <template v-slot:activator="{ on, attrs }">
      <span v-bind="attrs" v-on="on" class="badge-icons mx-2">
        <v-icon
          v-if="badge[0] == true"
          :color="['yellow darken-3', 'blue', 'green'][0]"
          >mdi-check-bold</v-icon
        ><v-icon
          v-if="badge[1] == true"
          :color="['yellow darken-3', 'blue', 'green'][1]"
          >mdi-check-bold</v-icon
        ><v-icon
          v-if="badge[2] == true"
          :color="['yellow darken-3', 'blue', 'green'][2]"
          >mdi-check-bold</v-icon>
      </span>
    </template>
    <div>
      <v-icon :color="['yellow darken-3', 'blue', 'green'][0]"
        >mdi-check-bold</v-icon
      >
      Willing to work in startups, projects, MSMEs or other small
      ventures.
    </div>
    <div>
      <v-icon :color="['yellow darken-3', 'blue', 'green'][1]"
        >mdi-check-bold</v-icon
      >
      Willing to mentor startups and projects with my intellectual skills and
      knowledge.
    </div>
    <div>
      <v-icon :color="['yellow darken-3', 'blue', 'green'][2]"
        >mdi-check-bold</v-icon
      >
      Willing to mentor for free.
    </div>
  </v-tooltip>
</template>

<script>
export default {
  props: ["badge"],

};
</script>

<style lang="scss" scoped>
.badge-icons i {
  width: 8px;
  font-size: 28px !important;
}

.badge-icons {
  white-space: nowrap;
}
</style>
