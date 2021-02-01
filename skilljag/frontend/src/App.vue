<template>
  <v-app v-if="profile!=null" >
    <!-- <NavDrawer :currentUser=profile />
    <v-main class="grey lighten-3">
      <v-container fluid>
        <router-view :currentUser=profile />
      </v-container>
    </v-main> -->
      <home-screen v-if="profile.completed_at!=null"/>
      <additionalinfo v-else />
  </v-app> 

</template>

<script>

import { apiService } from '@/common/api.service.js'
import NavDrawer from '@/components/NavDrawer.vue'
import Additionalinfo from './views/Screens/Additionalinfo.vue'

export default {
  name: 'App',

  components: {
    NavDrawer,
    Additionalinfo
  },
  data: () => ({
    requestUser: '',
    avatar: '',
    profile: null
  }),
  methods: {
    async setUserInfo () {
      const data = await apiService('/api/profiles/me/')
      console.log(data)
      this.requestUser = data.username
      this.avatar = data.avatar
      this.profile = data
      window.localStorage.setItem('profile', this.profile)
    }
  },
  created () {
    this.setUserInfo()
  }
}
</script>
