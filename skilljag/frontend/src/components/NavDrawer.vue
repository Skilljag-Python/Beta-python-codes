<template>
   <v-app-bar app>
    <div>
      <v-menu v-model="menu" :nudge-width="200" offset-x>
        <template v-slot:activator="{ on, attrs }">
          
          <v-badge content="" color="green " overlap>
            <v-avatar
              v-bind="attrs"
              v-on="on"
              size="34"
            >
              <v-img v-if="currentUser.avatar!=''" :src="currentUser.avatar"></v-img>
              <span v-else class="black--text">{{ avatarText }}</span>
            </v-avatar>
          </v-badge>
        </template>
    
    <div class="">
        <v-card>
          <v-list>
            <v-list-item>
              <v-list-item-avatar :color="true ? '' : 'grey darken-1 shrink'">
                <v-img v-if="true" :src="currentUser.avatar"></v-img>
                <span v-else class="white--text"> {{ avatarText }}</span>
              </v-list-item-avatar>
            </v-list-item>

            <v-list-item-content>
              <v-list-item-title>
                {{currentUser.username}}
              </v-list-item-title>
              <v-list-item-subtitle class="caption">
                {{currentUser.company}}
              </v-list-item-subtitle>
            </v-list-item-content>

            <v-list-item-action>
              <a href="/accounts/logout/">
                <v-icon>mdi-logout-variant</v-icon>
              </a>
            </v-list-item-action>

          </v-list>

          <v-divider></v-divider>
          <v-list-item to="/profile">
            <v-list-item-title>Profile</v-list-item-title>
          </v-list-item>
          <v-list-item @click="notifmenu = true">
            <v-list-item-title>Notifications</v-list-item-title>
          </v-list-item>
          <v-list>
            <dark-switch-item></dark-switch-item>
          </v-list>
        </v-card>
    </div>
      </v-menu>
    </div>
  </v-app-bar>
</template>

<script>
import DarkSwitchItem from '../components/DarkSwitchItem'

export default {
  components:{DarkSwitchItem},

  props: {
    currentUser: Object(),
    menu:false,
    notifmenu: false,
  },

  computed: {
    avatarText() {
      if (!this.currentUser.firstname || !this.currentUser.lastname) {
        return "You";
      }
      return ("" + this.currentUser.firstname[0] ).toUpperCase();
    },

    },

    methods: {
      
    }
  }
</script>