<template>
  <v-row :no-gutters="$vuetify.breakpoint.smAndDown">
    <v-col v-if="$vuetify.breakpoint.mdAndUp" cols="12" md="2">
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
        </v-list>
      </v-sheet>
    </v-col>

    <v-col cols="12" md="7">
      <v-sheet rounded="lg" class="mb-3 pa-3">
        <v-row align="center" no-gutters class="justify-center">
          <!-- <v-col cols="12" class="py-2" :key="index"> -->
          <v-col cols="auto" class="py-1">
            <v-btn
              class="px-1"
              text
              :color="filters.sort == 'trending' ? 'purple' : ''"
              @click="changeSort('trending')"
            >
              <v-icon class="px-1">mdi-trending-up</v-icon>
              Trending
            </v-btn>
          </v-col>
          <v-col cols="auto" class="py-1">
            <v-btn
              class="px-1"
              text
              :color="filters.sort == 'recent' ? 'purple' : ''"
              @click="changeSort('recent')"
            >
              <v-icon class="px-1">mdi-newspaper</v-icon>
              Recent
            </v-btn>
          </v-col>
          <v-col
            class="py-1"
            cols="12"
            md="auto"
            :style="$vuetify.breakpoint.mdAndUp ? 'flex-basis: 420px' : ''"
            :class="{ 'pl-2': $vuetify.breakpoint.mdAndUp }"
          >
            <v-text-field
              placeholder="Search posts..."
              prepend-inner-icon="mdi-magnify"
              dense
              flat
              hide-details
              solo-inverted
              rounded
              :clearable="!!filters.search"
              v-model="filters.search"
              @blur="loadPosts"
              @keydown.enter="$event.target.blur()"
            ></v-text-field>
          </v-col>
          <!-- <v-col
            class="py-1"
            cols="12"
            md="auto"
            :style="$vuetify.breakpoint.mdAndUp ? 'flex-basis: 210px' : ''"
            :class="{ 'pl-2': $vuetify.breakpoint.mdAndUp }"
          >
            <v-autocomplete
              :items="categoryStore"
              item-value="id"
              item-text="name"
              label="Filter"
              dense
              flat
              hide-details
              solo-inverted
              rounded
              clearable
              @change="loadPosts"
            ></v-autocomplete>
          </v-col> -->
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

            <post
              :trending="
                filters.sort == 'trending' ? 1 + index - (index) / 2 : false
              "
              v-else
              :item="item"
              :key="index"
            ></post>
          </template>
          <button
          v-show="next"
          @click="loadMorePosts"
          class="btn btn-sm"
          >Load More
        </button>
        </v-list>
      </v-sheet>
    </v-col>

    <v-col cols="12" md="3">
      <ad></ad>
      <v-sheet
        rounded="lg"
        min-height="200"
        class="mb-3"
        style="
          margin-top:20px
          position: sticky;
          top: 75px;overflow:auto;
        "
      >
        <v-list>
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
                src="/images/logo/color/icon/icon-192.png"
                width="4"
              ></v-img>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title v-html="text"></v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
        <v-spacer></v-spacer>
        
        <div class="grey--text caption px-4 mt-9">
          Copyright 2020 - Skilljag
        </div>
      </v-sheet>
    </v-col>
  </v-row>
</template>


<script>
export default {
  data: () => ({
    next: null,
    prevSearch:false,
    filters: {
      sort: "recent",
      search: "",
      category: "",
    },
    posts: [],
    postsLoading: false,
  }),
  methods: {
    interleave(arr, thing) {
      return [].concat(...arr.map((n) => [n, thing])).slice(0, -1);
    },
    changeSort(v) {
      this.filters.sort = v;
      this.posts = [];
      this.next = null;
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
      this.posts=[]
      var endpoint
      if(this.filters.search){
        endpoint = "/api/posts/?ordering="+this.filters.sort+"&text="+this.filters.search
      }
      else{
        endpoint = "/api/posts/?ordering="+this.filters.sort
      }     
       axios
        .get(endpoint, { })
        .then((r) => {
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
    },
  },
  mounted: function () {
    this.loadPosts();
  },
  computed: {
    categoryStore() {
      return this.$store.state.categories;
    },
  },
};
</script>