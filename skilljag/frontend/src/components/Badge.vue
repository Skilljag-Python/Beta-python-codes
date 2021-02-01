<template>

  <v-tooltip close-delay="100" bottom>
    <template v-slot:activator="{ on, attrs }">
      <span v-bind="attrs" v-on="on" class="badge-icons mx-2">
        <v-icon
          v-if="badgeSplit[0] == '1'"
          :color="['yellow darken-3', 'blue', 'green'][0]"
          >mdi-check-bold</v-icon
        >
        <v-icon
          v-if="badgeSplit[1] == '1'"
          :color="['yellow darken-3', 'blue', 'green'][1]"
          >mdi-check-bold</v-icon
        >
        <v-icon
          v-if="badgeSplit[2] == '1'"
          :color="['yellow darken-3', 'blue', 'green'][2]"
          >mdi-check-bold</v-icon
        >
      </span>
    </template>
    
    <div>
      <v-icon :color="['yellow darken-3', 'blue', 'green'][0]">
        mdi-check-bold
      </v-icon>
      Willing to work in a startup in a startup, projects, MSMEs or other small ventures.
    </div>
    <div>
      <v-icon :color="['yellow darken-3', 'blue', 'green'][1]">
        mdi-check-bold
      </v-icon>
      Willing to mentor startups and projects with your intellectual skills and knowledge.
    </div>
    <div>
      <v-icon :color="['yellow darken-3', 'blue', 'green'][2]">
        mdi-check-bold
      </v-icon>
      Willing to mentor for free.
    </div>
  </v-tooltip>
</template>

<script>
export default {
  props: ["badge"],
  computed: {
    badgeSplit() {
      if (!this.badge) return [];
      return this.badge.split("");
    },
  },
};
</script>
