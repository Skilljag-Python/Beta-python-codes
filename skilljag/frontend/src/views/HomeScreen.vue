<template>
  <v-app>
    <template v-if="$vuetify.breakpoint.lgAndUp">
      <v-app-bar app :color="$vuetify.theme.dark ? '' : 'white'" flat>
        <v-avatar
          :color="
            $vuetify.breakpoint.smAndDown ? 'grey darken-1' : 'transparent'
          "
          size="32"
        ></v-avatar>
        <v-toolbar-title class="mx-3">
          <router-link
            style="position: absolute; top: 1px; left: 155px; z-index: 5"
            to="/online"
          >
            <v-img src="/media/images/text.png" max-width="116"></v-img>
          </router-link>
        </v-toolbar-title>
        <v-tabs
          v-if="!hideTabs"
          style="color: #f4a701"
          v-model="selected"
          centered
          class="ml-n9"
          color="grey darken-1"
        >
          <v-tab
            class="text-button"
            :to="link.to"
            v-for="link in links"
            :key="link.to"
          >
            {{ link.name }}
          </v-tab>
        </v-tabs>
        <v-spacer v-else></v-spacer>

        <search-dialog></search-dialog>
        <conversations-icon></conversations-icon>
        <avatar-menu></avatar-menu>
      </v-app-bar>
    </template>
    <template v-else>
      <v-app-bar :color="$vuetify.theme.dark ? '' : 'white'" app absolute1 hide-on-scroll dense1 flat>
        <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>

        <v-toolbar-title
          ><router-link to="/online"
            ><v-img src="/media/images/text.png" max-width="106"></v-img></router-link
        ></v-toolbar-title>

        <v-spacer></v-spacer>

        <search-dialog icon-only></search-dialog>

        <conversations-icon></conversations-icon>

        <avatar-menu></avatar-menu>

        <template v-slot:extension>
          <v-tabs
            v-if="!hideTabs"
            style="color: #f4a701"
            v-model="selected"
            align-with-title
            centered
            center-active
            color="grey darken-1"
          >
            <v-tab
              class="text-button"
              :to="link.to"
              v-for="link in links"
              :key="link.to"
            >
              {{ link.name }}
            </v-tab>
          </v-tabs>
        </template>
      </v-app-bar>
      <v-navigation-drawer v-model="drawer" app temporary>
        <v-list nav dense>
          <v-list-item
            v-for="([icon, text], i) in [
              [
                'mdi-info',
                `<span style='color: #a759ef;'>About <span style='color: #f4a700;'>Us</span>`,
              ],
              ['mdi-chat', 'Feedback'],
            ]"
            :key="i"
            link
          >
            <v-list-item-icon class="mr-2">
              <v-icon size="24" v-if="i != 0">{{ icon }}</v-icon>
              <v-img
                v-else
                src="/media/images/logo/color/icon/icon-192.png"
                width="4"
              ></v-img>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title v-html="text"></v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
        <v-spacer></v-spacer>
      </v-navigation-drawer>
    </template>

    <v-main :class="{'grey lighten-3':!$vuetify.theme.dark}">
      <v-container class="px-0 py-md-0">
        <transition name="fade" mode="out-in">
          <router-view :key="$route.fullPath"></router-view>
        </transition>
      </v-container>
      <v-overlay
        dark="false"
        color="white"
        opacity="1"
        :value="overlay"
        v-if="overlay"
        style=""
      >
        <v-container>
          <v-row
            class="fill-height"
            justify="center"
            no-gutters
            @click="overlay = !overlay"
          >
            <v-img max-width="400" src="/media/images/Poster1.jpg"> </v-img>
          </v-row>
        </v-container>
      </v-overlay>
      <v-snackbar timeout="10000" v-model="hasSnack">
      {{ snackError }}

      <template v-slot:action="{ attrs }">
        <v-btn color="purple" text v-bind="attrs" @click="hasSnack = false">
          Close
        </v-btn>
      </template>
    </v-snackbar>
    </v-main>
  </v-app>
</template>

<script>
import AvatarMenu from "./Partials/AvatarMenu.vue";
import ConversationsIcon from "./Partials/ConversationsIcon.vue";
import SearchDialog from "./Partials/SearchDialog.vue";
import Conversations from "./Screens/Conversations.vue";
export default {
  components: { SearchDialog, Conversations, ConversationsIcon, AvatarMenu },
  created(){
    this.$store.dispatch('getInitData');
  },
  mounted() {
    this.avatar = window.avatar;
    setTimeout(() => {
      this.overlay = false;
      window.home = this;
    }, 3000);
    if (this.$route.path == "/") {
      this.$router.push({ path: "/online" });
    }
  },
  computed: {
    isSearch() {
      return this.$route.path == "/search";
    },
    hideTabs() {
      return this.isSearch || this.$route.path == "/profile" || this.$route.path == "/updateprofile" || this.$route.path == "/conversations";
    },
  },
  data: () => ({
    overlay: !true,
    hasSnack:false,
    snackError:'',

    drawer: false,
    links: [
      { name: "Online", to: "/online" },
      { name: "Recommended", to: "/recommended" },
      { name: "You", to: "/you" },
      { name: "New TECHS", to: "/newtechs" },
    ],

    selected: "",
  }),
  methods: {},
};
</script>

<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
</style>