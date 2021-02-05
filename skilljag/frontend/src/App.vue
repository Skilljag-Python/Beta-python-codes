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

<!-- popup -->
    <v-row justify="center">
      <v-dialog
        v-model="dialog"
        persistent
        max-width="290"
      >
        <v-card>
          <v-card-title class="headline">
            SkillJag
          </v-card-title>
          <v-card-text>
            Share your feedback!
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
              color="green darken-1"
              text
              @click="dialog = false"
            >
              Cancel
            </v-btn>
            <v-btn
              color="green darken-1"
              text
              @click="dialog = false"
            >
              <a href="https://forms.zohopublic.in/skilljagindaiapvtltd/form/Promoterform/formperma/Mj2ksolHPexQ7VwYltX8clu5KpAozZx8XnpMEck2xcI?zf_rszfm=1" target="_blank">Ok!</a>
            </v-btn>
          </v-card-actions>
        </v-card>

      </v-dialog>
    </v-row>
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
    profile: null,
    dialog: false
  }),
  methods: {
    async setUserInfo () {
      const data = await apiService('/api/profiles/me/')
      console.log(data)
      this.requestUser = data.username
      this.avatar = data.avatar
      this.profile = data
      window.localStorage.setItem('profile', this.profile)
    },

    callFunction () {
      setTimeout( () =>
          this.dialog="true"
    , 600000);
    }
  },

  mounted () {
      this.callFunction()
    },

  created () {
    this.setUserInfo()
  },
}
</script>
