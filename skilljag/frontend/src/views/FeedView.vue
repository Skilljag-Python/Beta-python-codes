<template>
  <v-main>
    <v-app-bar
      flat
    >
      <v-tabs
        centered
        class="ml-n9"
      >
        <v-tab
          v-for="link in links"
          :key="link.title"
          :to = link.link
        >
          {{ link.title }}
        </v-tab>
      </v-tabs>
    </v-app-bar>
    <router-view :currentUser=currentUser />
  </v-main>
</template>

<script>

// import { apiService } from '@/common/api.service.js'

export default {
  name: 'FeedView',
  data: () => ({
    links: [
      { title: 'Recent', link:'/recent'},
      { title: 'Trending', link:'/trending'},
    ]
  }),
  components: {

  },
  props: {
    currentUser: Object()
  }
}
</script>
