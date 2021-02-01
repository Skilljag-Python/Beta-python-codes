<template>
  <v-row :no-gutters="$vuetify.breakpoint.smAndDown">
    <v-col cols="12" sm="4">
      <v-sheet rounded="lg" min-height="76vh" class="mb-2">
        <div class="text-subtitle-1 pa-3">
          Following
          <v-btn
            class="float-right"
            dense
            small
            depressed
            text
            color="grey darken-1"
          >
            Show all (12)
          </v-btn>
        </div>

        <v-row class="pa-6 py-3">
          <v-col
            v-for="(item, index) in this.$store.state.user.following"

            :key="index"
            :class="(item.avatar ? 'd-flex' : '') + 'child-flex'"
            cols="4"
          >
            <v-img
            v-if="item.avatar"
              style="border-radius: 6px"
              :src="item.avatar"
              aspect-ratio="1"
              class1="grey lighten-2">
            </v-img>
            <div style="border-radius: 6px" v-else class="grey--text text-h2">{{ avatarText(item) }}</div>
         
            <h3 class="subtitle-2">{{ item.firstname }}</h3>
            <div class="caption">{{ item.lastname }}</div>
            <div class="caption">{{ item.company }}</div>
          </v-col>
        </v-row>
      </v-sheet>
      <v-sheet rounded="lg" min-height="76vh" class="mb-2">
        <div class="text-subtitle-1 pa-3">Team</div>
        <v-row class="pa-6 py-3">
          <v-col
            v-for="(item, index) in team"
            v-show="item.avatar"
            :key="index"
            :class="(item.avatar ? 'd-flex' : '') + 'child-flex'"
            cols="4"
          >
            <v-img
              style="border-radius: 6px"
              :src="item.avatar"
              :lazy-src1="item.avatar"
              aspect-ratio="1"
              class1="grey lighten-2"
            >
              <template v-slot:placeholder v-if="false">
                <v-row class="fill-height ma-0" align="center" justify="center">
                  <v-progress-circular
                    indeterminate
                    color="grey lighten-5"
                  ></v-progress-circular>
                </v-row>
              </template>
            </v-img>
            <h3 class="subtitle-2">{{ item.title }}</h3>
            <div class="caption">{{ item.subtitle }}</div>
          </v-col>
        </v-row>
      </v-sheet>
    </v-col>

    <v-col cols="12" sm="7">
      <v-sheet rounded="lg" class="mb-3 pa-1 px-3">
        <v-row justify="center">
          <v-dialog
            v-model="dialog"
            max-width="800px"
            :fullscreen="$vuetify.breakpoint.smAndDown"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-container class="px-10">
                <v-row align="center" ripple dark v-bind="attrs" v-on="on">
                  <v-col class="flex-grow-0">
                    <avatar size="40"></avatar>
                  </v-col>
                  <v-col
                    ><h1
                      class="heading"
                      style="text-align: center; width: 100%"
                    >
                      <v-textarea
                        hide-details
                        rows="1"
                        no-resize
                        readonly
                        
                        name="input-7-4"
                        label="Write new post..."
                      ></v-textarea>
                    </h1>
                  </v-col>
                </v-row>
              </v-container>
            </template>
            <v-card>
              <v-card-title>
                <span class="headline">Is it a</span>

                <v-btn
                  large
                  class="mx-3 my-1 ml-6"
                  rounded
                  depressed
                  :outlined="newPost.category == 'O'"
                  @click="newPost.category = 'O'"
                >
                  Opportunity
                </v-btn>

                <v-btn
                  large
                  class="mx-3 my-1"
                  rounded
                  depressed
                  :outlined="newPost.category == 'P'"
                  @click="newPost.category = 'P'"
                >
                  Project Idea
                </v-btn>

                <v-btn
                  large
                  class="mx-3 my-1"
                  rounded
                  depressed
                  :outlined="newPost.category == 'T'"
                  @click="newPost.category = 'T'"
                >
                  Thought
                </v-btn>
              </v-card-title>
              <v-card-text>
                <v-divider></v-divider>
                <v-container>
                  <v-textarea
                    counter="335"
                    hide-details1
                    rows="4sd"
                    solo
                    name="input-7-4"
                    label="Write newer post..."
                    v-model="newPost.description"
                  ></v-textarea>

                </v-container>
                <small
                  >The following info will not be shown with the post.</small
                >
                <v-row>
                  <v-col cols="12" md="3"
                    ><span
                      class="sub-title"
                      style="position: relative; top: 8px"
                      >Select skills involved</span
                    ></v-col
                  >
                  <v-col
                    ><v-autocomplete
                      rounded
                      v-model="newPost.skills"
                      :items="skillStore"
                      item-value="id"
                      item-text="title"
                      dense
                      chips
                      small-chips
                      hide-details1
                      label="Skills involved"
                      multiple
                      solo
                      outlined1
                      :search-input.sync="searchskills"
                      @change="searchskills = ''"
                      :rules="[
                        (v) => v.length <= 4 || 'Maximum limit of four.',
                      ]"
                    ></v-autocomplete
                  ></v-col>
                </v-row>
                <v-row>
                  <v-col cols="12" md="3"
                    ><span
                      class="sub-title"
                      style="position: relative; top: 8px"
                      >Select values involved</span
                    ></v-col
                  >
                  <v-col
                    ><v-autocomplete
                      rounded
                      v-model="newPost.values"
                      :items="valueStore"
                      item-value="id"
                      item-text="title"
                      dense
                      chips
                      small-chips
                      hide-details1
                      label="Values involved"
                      multiple
                      solo
                      :search-input.sync="searchvalues"
                      @change="searchvalues = ''"
                      :rules="[
                        (v) => v.length <= 4 || 'Maximum limit of four.',
                      ]"
                    ></v-autocomplete
                  ></v-col>
                </v-row>
                <v-row>
                  <v-col cols="12" md="3"
                    ><span
                      class="sub-title"
                      style="position: relative; top: 8px"
                      >Select category</span
                    ></v-col
                  >
                  <v-col
                    ><v-autocomplete
                      :items="categoryStore"
                      item-value="id"
                      item-text="name"
                      label="Category"
                      v-model="newPost.category_id"
                      dense
                      flat
                      hide-details
                      solo-inverted
                      rounded
                    ></v-autocomplete
                  ></v-col>
                </v-row>
                <v-row>
                  <v-col cols="6" v-for="(image, i) in newImages" :key="i">
                    <v-img
                      style="border-radius: 4px"
                      :src="image"
                      width="100%"
                      aspect-ratio="1"
                    >
                      <v-btn
                        class="ma-1"
                        light
                        style="background: #fff"
                        outlined
                        icon
                        ><v-icon>mdi-close</v-icon></v-btn
                      >
                    </v-img>
                  </v-col>
                </v-row>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-file-input
                  v-model="newPost.files"
                  hide-input
                  multiple
                  class="pa-0 flex-grow-0"
                  show-size
                  truncate-length="15"
                  accept="image/*,.pdf"
                  change="handleFileSelect"
                ></v-file-input>
                <v-btn color="blue darken-1" text @click="dialog = false">
                  Close
                </v-btn>
                <v-btn
                  color="blue darken-1"
                  :loading="submitLoading"
                  text
                  @click="submitNewPost"
                >
                  Post
                </v-btn>
              </v-card-actions>
            </v-card>
            <v-snackbar v-model="hasNewPostError">
              {{ newPostError }}

              <template v-slot:action="{ attrs }">
                <v-btn
                  color="pink"
                  text
                  v-bind="attrs"
                  @click="hasNewPostError = false"
                >
                  Close
                </v-btn>
              </template>
            </v-snackbar>
          </v-dialog>
        </v-row>
      </v-sheet>
      <v-sheet min-height="70vh" style="overflow: hidden">
        <div v-if="postsLoading">
          <v-skeleton-loader
            class="mx-auto"
            max-width1="300"
            type="list-item-avatar, divider, card-heading, image, actions"
            v-for="n in 5"
            :key="n"
          ></v-skeleton-loader>
        </div>
        <v-list three-line v-else>
          <template v-for="(item, index) in posts">
            <v-subheader
              v-if="item.header"
              :key="item.header + index"
              v-text="item.header"
            ></v-subheader>

            <v-divider
              v-else-if="item.divider"
              :key="index"
              :inset="item.inset"
            ></v-divider>

            <post v-else :item="item" :key="index"></post>
          </template>
          <button
          v-show="next"
          @click="loadPosts"
          class="btn btn-sm"
          >Load More
        </button>
        </v-list>
      </v-sheet>
    </v-col>

    <v-col cols="12" sm="3" v-if="false">
      <v-sheet
        rounded="lg"
        min-height="268"
        style="
          min-height: 468px;
          position: sticky;
          top: 75px;
          overflow-y: auto;
          max-height: 84vh;
          opacity: 0.6;
        "
      >
        <h5 class="pa-10" v-show="false">Ad</h5>
      </v-sheet>
    </v-col>
  </v-row>
</template>


<script>
import Avatar from "../Partials/Avatar.vue";
export default {
  components: { Avatar },
  data: () => ({
    newPostError: "",
    hasNewPostError: false,
    dialog: false,
    newFiles: [],
    newImages: [],
    searchskills: "",
    searchvalues: "",
    new:null,
    showModal:null,
    next:null,

    newPost: {
      category: "O",
      description: "",
      files: [],
      skills: [],
      values: [],
      category_id: "",
      title:"notitle"
    },
    following: [],
    /*     team: [
      {
        avatar: "https://cdn.vuetifyjs.com/images/lists/5.jpg",
        title: "Ernesto Epling",
        company: "Google",
        subtitle: `Designer`,
      },

      {
        avatar: "https://cdn.vuetifyjs.com/images/lists/4.jpg",
        title: "Myrna Barb",
        company: "Google",
        subtitle: `Designation`,
      },

      {
        avatar: "https://cdn.vuetifyjs.com/images/lists/3.jpg",
        title: "Adina Ealey",
        company: "Google",
        subtitle: `Designation`,
      },

      {
        avatar: "https://cdn.vuetifyjs.com/images/lists/2.jpg",
        title: "Ariane Roff",
        company: "Google",
        subtitle: `Designation`,
      },

      {
        avatar: "https://cdn.vuetifyjs.com/images/lists/1.jpg",
        title: "Ariane Roff",
        company: "Google",
        subtitle: `Designation`,
      },
    ], */

    posts: [],

    //loaders
    submitLoading: false,
    postsLoading: false,
  }),
  mounted: function () {
    this.loadPosts();
     window.addEventListener('keydown', (e) => {
      if (e.key == '=') {
        this.new = !this.showModal;
      }
    });
  },
  methods: {
    avatarText(item) {
      if (!item.firstname) {
        return "You";
      }
      return ("" + item.firstname[0]).toUpperCase();
    },
    handleFileSelect(v) {
      this.newImages = [];
      console.log(v);
      let fileList = v;
      fileList.forEach((f) => {
        if (!f.type.match("image.*")) {
          return;
        }

        // this.newImages.push(URL.createObjectURL(f));
        // URL.revokeObjectURL(this.src);

        let reader = new FileReader();
        let that = this;

        reader.onload = function (e) {
          that.newImages.push(e.target.result);
        };
        reader.readAsDataURL(f);
      });
    },

    interleave(arr, thing) {
      return [].concat(...arr.map((n) => [n, thing])).slice(0, -1);
    },
    loadPosts: function () {
/*       this.postsLoading = true;
 */      let endpoint = "/api/posts/"
      if(this.next) {
        endpoint = this.next
      }
      axios
        .get(endpoint)
        .then((r) => {
          /* this.posts.push({divider:true, inset:true}) */
          this.posts.push(...this.interleave(r.data.results, { divider: true, inset: true }));
          if (r.data.next) {
            this.next = r.data.next
          } else {
            this.next = null
          }
        })
        .catch((error) => {
          console.log(error);
        })
        .then(() => {
          this.postsLoading = false;
        });
    },
    newPostValidate() {
      var p = this.newPost;
      this.newPostError = "";
      this.hasNewPostError = false;
      if (p.description.length < 4) {
        this.newPostError = "Please write at least 4 characters.";
      } else if (p.description.length > 355) {
        this.newPostError = "Please write less than 355 characters.";
      } else if (p.skills.length > 4 || p.values.length > 4) {
        this.newPostError =
          "Number of skills or values should be less than four";
      }
      if (this.newPostError.length) {
        this.hasNewPostError = true;
        return false;
      }
      return true;
    },
    initNewPost() {
      (this.newPost.category = "O"),
        (this.newPost.description = ""),
        (this.newPost.files = []),
        (this.newPost.skills = []),
        (this.newPost.values = []),
        (this.newPost.category_id = "");
    },
    async submitNewPost() {
      if (!this.newPostValidate()) {
        return;
      }

      this.submitLoading = true;

      let formData = new FormData();

      // files

     /*  for (var i = 0; i < this.newPost.files.length; i++) {
        let file = this.newPost.files[i];

        formData.append("images[" + i + "]", file);
      } */
      // additional data
      var data = this.newPost;
      for (let key in data) {
        if(key == 'files')
        {
          console.log(key)
        }
        else 
        {if (typeof data[key] === "object") {
          for (let subKey in data[key]) {
            formData.append(`${key}.${subKey}`, data[key][subKey]);
          }
        } else {
          formData.append(key, data[key]);
        }
        }
      }
      axios
        .post("/api/posts/", data)
        .then((response) => {
          console.log(response);
          if (response.status == 201) {
            for (var i = 0; i < this.newPost.files.length; i++) {
              let file = this.newPost.files[i];
              const imagedata = new FormData();
              imagedata.append('image',file)
              imagedata.append('post',response.data.id)
              axios
              .post("/api/images/", imagedata);

            }

            this.dialog = false;
            this.initNewPost();
            this.loadPosts();
          }
          if (response.error) {
            this.newPostError = response.data.error;
            this.hasNewPostError = true;
          }
        })
        .catch((error) => {
          /* if (error.response.status === 422) {
            this.errors = error.response.data;
          } else {
            console.log(error);
          } */
          console.log(error)
        })
        .then(() => {
          this.submitLoading = false;
        });
    },
  },
  computed: {
    skillStore() {
      return this.$store.state.skills;
    },
    valueStore() {
      return this.$store.state.values;
    },
    categoryStore() {
      return this.$store.state.categories;
    },
  },
};
</script>