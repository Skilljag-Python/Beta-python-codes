

<template>
  <v-avatar :color="(avatar?'':'grey darken-1 shrink')" :size="size">
    <v-img v-if="avatar" :src="avatar"></v-img>
    <span v-else class="white--text">{{ avatarText }}</span>
  </v-avatar>
</template>
          
<script>
export default {
  props: {
    size: {
      default: 34,
      // type: Number,
    },
  },
  computed: {
    user() {
      return this.$store.state.user;
    },
    avatarText() {
      if (!this.user.firstname || !this.user.lastname) {
        return "You";
      }
      return (
        "" +
        this.user.firstname[0]
      ).toUpperCase();
    },
    avatar() {
      return this.user.avatar;
    },
  },
};
</script>
