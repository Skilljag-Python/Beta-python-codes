<template>
  <div class="py-5">
    <v-sheet rounded="lg">
      <v-container class="px-16 py-10 p-relative">
        <div v-if="userLoading">
          <v-skeleton-loader
            class="mx-auto"
            max-width1="700"
            type="list-item-avatar, list-item-two-line"
            v-for="n in 1"
            :key="n"
          ></v-skeleton-loader>
        </div>
        <v-row v-else>
          <v-col class="flex-grow-0">
            <v-avatar color="grey darken-2" size="137" rounded="lg">
              <v-img v-if="avatar" :src="avatar"></v-img>
              <span v-else class="white--text text-h2">{{ avatarText }}</span>
            </v-avatar>
          </v-col>
          <v-col class="align-self-center"
            ><span class="text-h6">{{ fullName }}</span
            ><span class="text-h6 grey--text" v-if="userIsCurrentUser">
              (You)</span
            >
            <div class="text-body-2 grey--text">{{ values }}</div>

            <div v-if="user.highested" class="text-body-2 grey--text"><v-icon size="20" class="mr-1">mdi-school-outline</v-icon>{{ user.highested }}</div>
            <div v-if="user.designation" class="text-body-2 grey--text"><v-icon size="20" class="mr-1">mdi-briefcase-outline</v-icon>{{ user.designation }}</div>
            <div v-if="user.company" class="text-body-2 grey--text"><v-icon size="20" class="mr-1">mdi-office-building-outline</v-icon>{{ user.company }}</div>
            <div v-if="userState" class="text-body-2 grey--text"><v-icon size="20" class="mr-1">mdi-map-marker-outline</v-icon>{{ userState }}</div>
            
            
            
             </v-col
          ><v-spacer></v-spacer>
          <v-col
            v-if="!userIsCurrentUser"
            cols="auto"
            class="align-self-center"
          >
            <v-menu offset-y v-if="user.me_following">
              <template v-slot:activator="{ on, attrs }">
                <v-btn color="grey" dark v-bind="attrs" v-on="on">
                  Following <v-icon>mdi-chevron-down</v-icon>
                </v-btn>
              </template>
              <v-list>
                <v-list-item @click="followDestroy">
                  <v-list-item-title>Unfollow</v-list-item-title>
                </v-list-item>
              </v-list>
            </v-menu>
            <!-- <v-btn
              depressed
              color="grey"
              dark
              v-else-if="user.follow_status.outgoing_request"
              @click="followDestroy"
              >Requested</v-btn
            > -->
            <v-btn
              depressed
              color="primary"
              :disabled="userIsCurrentUser"
              v-else-if="!user.me_following"
              @click="follow"
              >Follow</v-btn
            >
          </v-col>
          <v-col cols="auto" class="align-self-center" v-if="!userIsCurrentUser">
            <v-btn
              @click="sendMessage()"
              depressed
              color="primary"
              :disabled="userIsCurrentUser"
            >
              <v-icon class="pr-1">mdi-message-minus-outline</v-icon>Message
            </v-btn>
          </v-col>
          <v-col class="align-self-center flex-grow-0"
            ><badge :badge="[user.q1,user.q2,user.q3]"></badge>
          </v-col>
        </v-row>
        <v-menu offset-y>
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              style="position: absolute; top: 0px; right: 0; margin: 5px"
              v-bind="attrs"
              v-on="on"
              icon
              text
              v-ripple="false"
            >
              <v-icon>mdi-dots-vertical</v-icon>
            </v-btn>
          </template>
          <v-list>
            <v-list-item>
              <v-list-item-title>Report</v-list-item-title>
            </v-list-item>
            <v-list-item>
              <v-list-item-title>Block</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
      </v-container>
    </v-sheet>
    <v-sheet rounded="lg" class="mt-5">
      <div v-if="userLoading">
        <v-skeleton-loader
          class="mx-auto"
          type="list-item-two-line"
          v-for="n in 1"
          :key="n"
        ></v-skeleton-loader>
      </div>
      <v-container v-else class="px-4"
        >Skills
        <div>
          <v-chip
            v-for="(item, index) in skills"
            class="ma-2"
            :color="index < 4 ? 'purple' : ''"
            outlined
            large
            :key="index"
          >
            {{ item }}
          </v-chip>
        </div>
      </v-container>
      

      
    </v-sheet>
    <v-sheet rounded="lg" class="mt-5">
            
            <div v-if="userLoading">
                <v-skeleton-loader
                    class="mx-auto"
                    type="list-item-two-line"
                    v-for="n in 1"
                    :key="n"
                ></v-skeleton-loader>
            </div>
            <v-container v-else class="px-4 p-relative">
                Additional Skills
                <div>
                    <v-chip
                        v-for="(item, index) in askills"
                        class="ma-2"
                        :color="index < 4 ? 'orange' : ''"
                        outlined
                        large
                        :key="index"
                    >
                        {{ item }}
                    </v-chip>
                </div>
            </v-container>          
        </v-sheet>
    <v-sheet rounded="lg" class="mt-5">
      <div v-if="userLoading">
        <v-skeleton-loader
          class="mx-auto"
          type="list-item-two-line"
          v-for="n in 1"
          :key="n"
        ></v-skeleton-loader>
      </div>
      <v-container v-else class="px-4"
        >About
        <p v1-if="user.bio">
          {{ user.bio }}
        </p>
      </v-container>
</v-sheet>
      <v-sheet rounded="lg" class="mt-5">
      <v-container class="px-4">Work Gallery</v-container>
      <div v-if="userLoading">
        <v-skeleton-loader
          class="mx-auto"
          max-width1="300"
          type="list-item-avatar, divider, card-heading, image, actions"
          v-for="n in 2"
          :key="n"
        ></v-skeleton-loader>
      </div>
      <v-row v-else class="pa-15">
        <v-col v-for="image in workimages" :key="image.id" class="d-flex child-flex" cols="4">
          <v-img
            :src="image.image"
            aspect-ratio="1"
            class="grey lighten-2"
          >
            <template v-slot:placeholder>
              <v-row class="fill-height ma-0" align="center" justify="center">
                <v-progress-circular
                  indeterminate
                  color="grey lighten-5"
                ></v-progress-circular>
              </v-row>
            </template>
          </v-img>
        </v-col>
      </v-row>
    </v-sheet>
    
    <!-- <v-sheet rounded="lg" class="mt-5">
      <v-container class="px-4">Work Gallery</v-container>
      <div v-if="userLoading">
        <v-skeleton-loader
          class="mx-auto"
          max-width1="300"
          type="list-item-avatar, divider, card-heading, image, actions"
          v-for="n in 2"
          :key="n"
        ></v-skeleton-loader>
      </div>
      <v-row v-else-if="user.work_gallery" class="pa-15">
        <v-col
          v-for="item in user.work_gallery"
          :key="item.url"
          class="d-flex child-flex"
          cols="4"
        >
          <v-img
            :src="item.url"
            lazy-src1=""
            aspect-ratio="1"
            class="grey lighten-2"
          >
            <template v-slot:placeholder>
              <v-row class="fill-height ma-0" align="center" justify="center">
                <v-progress-circular
                  indeterminate
                  color="grey lighten-5"
                ></v-progress-circular>
              </v-row>
            </template>
          </v-img>
          <v-img
            v-if="false"
            :src="`https://picsum.photos/500/300?image=${n * 5 + 10}`"
            :lazy-src="`https://picsum.photos/10/6?image=${n * 5 + 10}`"
            aspect-ratio="1"
            class="grey lighten-2"
          >
            <template v-slot:placeholder>
              <v-row class="fill-height ma-0" align="center" justify="center">
                <v-progress-circular
                  indeterminate
                  color="grey lighten-5"
                ></v-progress-circular>
              </v-row>
            </template>
          </v-img>
        </v-col>
      </v-row> -->
     
  </div>
</template>

<script>
export default {
  data: () => ({
    user: {
      values: [],
      skills: [],
      askills:[],
    },
    userLoading: false,
    workimages:[]
  }),
  mounted: function () {
    this.loadUser();
    this.loadWorkGallery()
  },
  methods: {

    sendMessage(){
      axios.get('/api/rooms/?uid='+this.user.id)
      .then((response) => {
        console.log(response)
        if(response.status == 200)
        {
          this.$router.push({path:'/conversations'})
        }
      })
    },
    loadUser() {
      this.userLoading = true;
      axios.get("/api/profiles/" + this.$route.params.id + '/').then((r) => {
        this.user = r.data;

        this.userLoading = false;
      });
    },
    loadWorkGallery()
    {
      axios.get("/api/workimages/?uid="+this.$route.params.id)
      .then(response => {
        this.workimages = response.data
      })
    },
    followDestroy() {
      var fol;
      var following=[];
      this.$store.state.user.following.forEach(fol =>{
         console.log(fol)
        if(fol!=this.user.id)
        {
          following.push(fol)
        }
      })

      axios.patch(`/api/profiles/me/`,{following: following}).then((r) => {
        console.log(r.data)
        this.user.me_following = false;
        this.$store.dispatch('getInitData');
      });
    },
    follow() {
      var fol;
      var following=[];
      this.$store.state.user.following.forEach(fol =>{
         console.log(fol)
        if(fol!=this.user.id)
        {
          following.push(fol)
        }
      })
      following.push(this.user.id)
      console.log({following: following})
      axios.patch(`/api/profiles/me/`,{following: following}).then((r) => {
        console.log(r.data)
        this.user.me_following = true;
        this.$store.dispatch('getInitData');
      });
    },
  },
  computed: {
    userState(){
      var user = this.user,
      states= this.$store.state.states,
      stateName;
      if(!user.state || !states.length){
        return '';
      }
      states.forEach((e)=>{
        if(e.id==user.state){
          stateName = e.title;
        }
      });
      return stateName;
    },
    fullName() {
      return this.user.firstname + " " + this.user.lastname;
    },
    skills() {
      if (!this.user.skills) return;
      var skills = [];
      var sks = this.$store.state.skills;
      this.user.skills.forEach((e) => {
        sks.forEach((el)=>{
          if(el.id == e)
          {
            skills.push(el.title);
          }
        }) 
      });
      return skills;
    },
    askills() {
      if (!this.user.askills) return;
      var askills = [];
      var asks = this.$store.state.skills;
      this.user.askills.forEach((e) => {
        asks.forEach((el)=>{
          if(el.id == e)
          {
            askills.push(el.title);
          }
        }) 
      });
      return askills;
    },
    values() {
      if (!this.user.values) return;
      var values = [];
      var vals = this.$store.state.values;
      this.user.values.forEach((e) => {
        vals.forEach((el)=>{
          if(el.id == e)
          {
            values.push(el.title);
          }
        }) 
      });
      return values.join(" . ");
    },
    avatarText() {
      if (!this.user.firstname || !this.user.lastname) {
        return "You";
      }
      return ("" + this.user.firstname[0]).toUpperCase();
    },
    avatar() {
      return this.user.avatar;
    },
    userIsCurrentUser() {
      if (this.userLoading) return true;
      return this.user.id == this.$store.state.user.id;
    },
  },
};
</script>