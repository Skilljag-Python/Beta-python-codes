<template>
  <v-row :no-gutters="$vuetify.breakpoint.smAndDown">
    <v-col cols="12" sm="2">
      <v-sheet
        rounded="lg"
        min-height="268"
        style="
          min-height: 268px;
          position: sticky;
          top: 75px;
          overflow-y: auto;
          max-height: 84vh;
        "
        v-if="false"
      >
        <div class="text-subtitle-1 pa-3">Trending Posts</div>
        <v-list three-line>
          <template v-for="(item, index) in items10">
            <v-subheader
              v-if="item.header"
              :key="item.header"
              v-text="item.header"
            ></v-subheader>

            <v-divider
              v-else-if="item.divider"
              :key="index"
              :inset="item.inset"
            ></v-divider>

            <post v-else :item="item" :key="index"></post>
          </template>
        </v-list>
      </v-sheet>
    </v-col>

    <v-col cols="12" sm="7">
      <v-sheet min-height="70vh" style="overflow: hidden">
        <v-container class="px-5 text-center">
          <v-btn
            large1
            class="mx-3"
            rounded
            text
            :color="filters.category == 'O' ? 'purple' : ''"
            @click="changeIsType('O')"
          >
            Opportunity
          </v-btn>

          <v-btn
            large1
            class="mx-3"
            rounded
            text
            :color="filters.category == 'P' ? 'purple' : ''"
            @click="changeIsType('P')"
          >
            Project Idea
          </v-btn>

          <v-btn
            large1
            class="mx-3"
            rounded
            text
            :color="filters.category == 'T' ? 'purple' : ''"
            @click="changeIsType('T')"
          >
            Thought
          </v-btn>
        </v-container>
        <v-divider></v-divider>
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
          <v-divider/>
          <br/>
          <br/>
         <div>
          <v-btn
          v-show="next"
          @click="loadMorePosts"
          outlined
          absolute
          z-index:9999
          :style="{left:'30px', bottom:'18px'}"
          >Load More
          </v-btn>
        </div>
        </v-list>
      </v-sheet>
    </v-col>

    <v-col cols="12" sm="3">
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
        <h5 class="pa-10" v-if="false">Ad</h5>
      </v-sheet>
    </v-col>
  </v-row>
</template>


<script>
export default {
  data: () => ({
    filters: {
      category: "P",
    },
    posts: [],
    next: null,
    postsLoading: false,
  }),
  methods: {
    interleave(arr, thing) {
      return [].concat(...arr.map((n) => [n, thing])).slice(0, -1);
    },
    changeIsType: function (v) {
      this.filters.category = v;
      this.next= null;
      this.posts = [];
      this.loadPosts();
    },
    loadMorePosts:function(){
      if(this.next) {
        let endpoint = this.next
        axios
        .get(endpoint, { })
        .then((r) => {
          this.posts.push({divider:true, inset:true})
          this.posts.push(...this.interleave(r.data.results, { divider: true, inset: true }))
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
      }

    },

    loadPosts: function () {
      this.postsLoading = true;
      this.post = [];
      let endpoint = "/api/posts/?recommended=1&category="+this.filters.category
      console.log(endpoint)
      axios
        //.get("/posts/recommended", { params: this.filters })
        .get(endpoint)
        .then((r) => {
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
  },

  mounted: function () {
    this.loadPosts();
  },
};
</script>