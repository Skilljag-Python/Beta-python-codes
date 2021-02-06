<template>
  <div class="py-5">
    <v-sheet rounded="lg">
      <v-container class="px-16 py-10 p-relative">
        <edit-button
          :active="editEnabled"
          @on-click="editEnabled = !editEnabled"
        ></edit-button>
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
          <v-col class="flex-grow-0 p-relative"
            ><v-avatar color="grey darken-2" size="137" rounded="lg">
              <v-img v-if="avatar" :src="avatar"></v-img>
              <span v-else class="grey--text text-h2">{{ avatarText }}</span>
            </v-avatar>
            <!-- <edit-button
              v-if="editEnabled"
              @on-click="editEnabled = !editEnabled"
            ></edit-button> -->
          </v-col>
          <v-col class="align-self-center p-relative"
            ><span class="text-h6">{{ fullName }}</span>
            <div class="text-body-2 grey--text">{{ values }}</div>

            <div v-if="user.highested" class="text-body-2 grey--text">
              <v-icon size="20" class="mr-1">mdi-school-outline</v-icon
              >{{ user.highested }}
            </div>
            <div v-if="user.designation" class="text-body-2 grey--text">
              <v-icon size="20" class="mr-1">mdi-briefcase-outline</v-icon
              >{{ user.designation }}
            </div>
            <div v-if="user.institution" class="text-body-2 grey--text">
              <v-icon size="20" class="mr-1">mdi-office-building-outline</v-icon
              >{{ user.institution }}
            </div>
            <div v-if="userState" class="text-body-2 grey--text">
              <v-icon size="20" class="mr-1">mdi-map-marker-outline</v-icon
              >{{ userState }}
            </div>
            <!-- <edit-button
              v-if="editEnabled"
              @on-click="editEnabled = !editEnabled"
            ></edit-button> -->
          </v-col>
          <v-spacer></v-spacer>
          <v-col cols="auto" class="align-self-center">
            <div>
              <v-btn depressed text color="grey darken-1">
                Followers {{user.followers_count}}
              </v-btn>
            </div>
            <div>
              <v-btn depressed text color="grey darken-1"> Following {{user.following_count}} </v-btn>
            </div> </v-col
          ><v-col class="align-self-center flex-grow-0"
            ><badge :badge="[user.q1, user.q2, user.q3]"></badge>
          </v-col>
        </v-row>
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
      <v-container v-else class="px-4 p-relative"
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
        <!-- <edit-button
          v-if="editEnabled"
          @on-click="editEnabled = !editEnabled"
        ></edit-button> -->
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
      <v-container v-else class="px-4 p-relative"
        >About
        <p v-if="user.bio">
          {{ user.bio }}
        </p>
        <div>
          <v-dialog v-model="aboutDialog" max-width="600px">
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                v-show="!user.bio"
                v-bind="attrs"
                v-on="on"
                depressed
                text
                color="grey darken-1"
                >What should the world know about you?</v-btn
              >
            </template>
            <v-card>
              <v-card-title>
                <v-row align="center" class="spacer" no-gutters>
                  <v-col cols="4" sm="2" md="1">
                    <avatar></avatar>
                  </v-col>

                  <v-col>
                    <strong>{{ fullName }}</strong>
                  </v-col>
                </v-row>
              </v-card-title>
              <v-card-text>
                <v-divider></v-divider>
                <v-container>
                  <v-textarea
                    hide-details
                    rows="6"
                    solo
                    v-model="editor.about"
                    counter="300"
                    label="What should the world know about you?"
                  ></v-textarea>
                </v-container>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>

                <v-btn
                  color="purple lighten-1"
                  text
                  @click="aboutDialog = false"
                >
                  Close
                </v-btn>
                <v-btn
                  color="purple"
                  :loading="aboutSubmitLoading"
                  text
                  @click="submitAbout"
                >
                  Go!
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </div>
        <!-- <edit-button
          v-if="editEnabled"
          @on-click="aboutDialog = true"
        ></edit-button> -->
      </v-container>
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
      <v-row v-else class="pa-15">
        <v-col v-for="n in 9" :key="n" class="d-flex child-flex" cols="4">
          <v-img
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
      </v-row>
    </v-sheet> -->
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
  </div>
</template>

<script>
import Avatar from "../Partials/Avatar.vue";
import Badge from "../Partials/Badge.vue";
import EditButton from "../Partials/EditButton.vue";
export default {
  components: { Badge, Avatar },
  data: () => ({
    user: {},
    editor: { about: "" },
    editEnabled: false,
    aboutDialog: false,
    aboutSubmitLoading: false,
    userLoading: false,
    workimages: []
  }),
  mounted: function () {
    // window.home.selected=false;
    this.loadUser();
  },
  methods: {
    loadWorkGallery()
    {
      axios.get("/api/workimages/?uid="+this.$store.state.user.id)
      .then(response => {
        this.workimages = response.data.results
      })
    },
    submitAbout() {
      this.aboutSubmitLoading = true;
      this.$http
        .post("/profile/update/about", this.editor, {
          "Content-Type": "multipart/form-data",
        })
        .then((response) => {
          if (response.data == 200) {
            this.aboutDialog = false;
            return this.loadUser();
          }
          if (response.data.error) {
          }
        })
        .catch((error) => {
          if (error.response.status === 422) {
            this.errors = error.response.data;
          } else {
            console.log(error);
          }
        })
        .then(() => {
          this.aboutSubmitLoading = false;
        });
    },
    loadUser() {
      this.userLoading = true;
      axios.get("/api/profiles/me/").then((r) => {
        this.user = r.data;
        this.userLoading = false;
      });
    },
  },
  computed: {
    userState() {
      var user = this.user,
        states = this.$store.state.states,
        stateName;
      if (!user.state_id || !states.length) {
        return "";
      }
      states.forEach((e) => {
        if (e.id == user.state_id) {
          stateName = e.name;
        }
      });
      return stateName;
    },
    fullName() {
      return this.user.firstname + " " + this.user.lastname;
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
    avatarText() {
      if (!this.user.firstname || !this.user.lastname) {
        return "You";
      }
      return ("" + this.user.firstname[0]).toUpperCase();
    },
    avatar() {
      return this.user.avatar;
    },
  },
};
</script>