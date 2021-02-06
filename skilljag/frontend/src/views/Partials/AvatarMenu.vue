<template>
  <div>
    <v-menu v-model="menu" :nudge-width="200" offset-x>
      <template v-slot:activator="{ on, attrs }">
        <v-badge :content="notifications.length" color="red darken-4" overlap>
          <v-avatar
            v-bind="attrs"
            v-on="on"
            :color="avatar?'':'grey darken-1 shrink'"
            size="34"
          >
            <v-img v-if="avatar" :src="avatar"></v-img>
            <span v-else class="white--text">{{ avatarText }}</span>
          </v-avatar>
        </v-badge>
      </template>

      <v-card>
        <v-list>
          <v-list-item>
            <v-list-item-avatar :color="avatar ? '' : 'grey darken-1 shrink'">
              <v-img v-if="avatar" :src="avatar"></v-img>
              <span v-else class="white--text">{{ avatarText }}</span>
            </v-list-item-avatar>

            <v-list-item-content>
              <v-list-item-title>{{
                user.firstname + " " + user.lastname
              }}</v-list-item-title>
              <v-list-item-subtitle class="caption">{{
                user.company
              }}</v-list-item-subtitle>
            </v-list-item-content>

            <v-list-item-action>
              <v-btn icon href='/accounts/logout/'>
                <v-icon>mdi-logout-variant</v-icon>
              </v-btn>
            </v-list-item-action>
          </v-list-item>
        </v-list>

        <v-divider></v-divider>
        <v-list-item to="/profile">
          <v-list-item-title>Profile</v-list-item-title>
        </v-list-item>
        <v-list-item @click="notifmenu = true">
          <v-list-item-title>Notifications</v-list-item-title>
        </v-list-item>
        <v-list-item>
          <v-list-item-title>Organisation</v-list-item-title>
          <v-list-item-subtitle>Coming Soon</v-list-item-subtitle>
        </v-list-item>
        <v-list>
          <dark-switch-item></dark-switch-item>
        </v-list>
      </v-card>
    </v-menu>
    <!-- <v-menu
      :close-on-content-click="true"
      :nudge-width="400"
      offset-y
      v-model="notifmenu"
      transition="slide-x-transition"
      bottom
      right
      :position-x="100"
    >
      <v-list>
        <v-list-item link v-for="n in 5" :key="n">
          <v-list-item-avatar>
            <img
              src="https://cdn.vuetifyjs.com/images/lists/3.jpg"
              alt="John"
            />
          </v-list-item-avatar>

          <v-list-item-content>
            <v-list-item-title
              >Notification really long text {{ n }}</v-list-item-title
            >
            <v-list-item-subtitle class="caption"
              >some text</v-list-item-subtitle
            >
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-menu> -->
    <v-menu
      :close-on-content-click="false"
      :nudge-width="400"
      offset-y
      v-model="notifmenu"
      transition="slide-x-transition"
      bottom
      right
      :position-x="100"
      max-height="400"
      max-width="400"
    >
      <v-list>

        <v-list-item link v-for="n in notifications" :key="n.id">
          <v-list-item-avatar>
            <span class="grey--text text-h6">{{n.type}}</span>
          </v-list-item-avatar>
 
          <v-list-item-content @click="deleteN(n.id)">
            <v-list-item-title v-if="n.type!='F'">{{n.post.content}}</v-list-item-title>
            <v-list-item-subtitle v-if="n.type == 'C' " class="caption">Your post got {{n.value}} new comments</v-list-item-subtitle>
            <v-list-item-subtitle v-if="n.type == 'I' " class="caption">Your post got {{n.value}} new interests</v-list-item-subtitle>
            <v-list-item-subtitle v-if="n.type == 'F' " class="caption">Your have {{n.value}} new followers</v-list-item-subtitle>
          </v-list-item-content>
          
 
        </v-list-item>
       
      </v-list>
    </v-menu>

  </div>
</template>

<script>
export default {
  data: () => ({
    menu:false,
    notifmenu: false,
    notifications: []
  }),
  mounted(){
    this.getNotifications()
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
      return this.user.avatar // this.user.avatar;
    },
  },
  methods: {
    getNotifications() {
      axios.get('/api/notifications/')

      .then((response) => {
        console.log(response)
        this.notifications = response.data
      })
    },
    deleteN(nId){
      axios.delete('/api/notifications/'+nId+'/')
      .then(response => {
        this.getNotifications()
      })

    },
    logout() {
      document.body.innerHTML += `<form id="logout-form" action="/logout" method="POST" class="d-none"><input type="hidden" name="_token" value="${
        document.querySelector('meta[name="csrf-token"]').content
      }"></form>`;
      document.getElementById("logout-form").submit();
    },
  },
};
</script>
