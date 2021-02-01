<template>
    <v-container>
        <v-row>
          <v-col
            cols="12"
            sm="2"
          >
          </v-col>

          <v-col
            cols="12"
            sm="8"
          >
            <div
              v-for="post in posts"
              :key="post.id"
            >
              <PostSheet v-bind:post=post :currentUser=currentUser />
              <br>
            </div>
            <div class="my-4">
        <p v-show="loadingPosts">...loading...</p>
        <button
          v-show="next"
          @click="getPosts"
          class="btn btn-sm"
          >Load More
        </button>
      </div>
          </v-col>

          <v-col
            cols="12"
            sm="2"
          >

          </v-col>
        </v-row>
    </v-container>
</template>

<script>

import { apiService } from '@/common/api.service.js'
import PostSheet from '../components/PostSheet.vue'

export default {
  name: 'TrendingView',
  props: {
    currentUser: Object()
  },
  data: () => ({
    posts: [],
    next: null,
    loadingPosts: false
  }),
  components: {
    PostSheet
  },
  methods: {
    getPosts () {
      // make a GET Request to the questions list endpoint and populate the questions array
      let endpoint = '/api/posts/?ordering=trending'
      if (this.next) {
        endpoint = this.next
      }
      this.loadingPosts = true
      apiService(endpoint)
        .then(data => {
          this.posts.push(...data.results)
          this.loadingPosts = false
          if (data.next) {
            this.next = data.next
          } else {
            this.next = null
          }
        })
    }
  },
  created () {
    this.getPosts()
  }
}
</script>