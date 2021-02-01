<template>
  <v-row>
    <v-col cols="12" sm="2"></v-col>
    <v-col cols="12" sm="7">
      <v-sheet min-height="660px" rounded="lg" style="overflow: hidden">
        <v-container class="px-5">
          <v-responsive max-width="" style="">
            <v-text-field
              v-model="filters.q"
              @blur="getData"
              @keydown.enter="$event.target.blur()"
              placeholder="Search for skill, person's name..."
              prepend-inner-icon="mdi-magnify"
              dense
              flat
              hide-details
              rounded
              solo-inverted
            ></v-text-field>
          </v-responsive>
          <v-row>
            <v-col>
              <v-autocomplete
                v-model="filters.values"
                :items="valueStore"
                @change="
                  valuesInput = '';
                  filters.values.length > 4 ? filters.values.pop() : getData();
                "
                :rules="[(v) => v.length <= 4 || 'Maximum limit of four.']"
                item-text="name"
                item-value="id"
                chips
                small-chips
                label="Values"
                multiple
                dense
                flat
                hide-details
                rounded
                solo-inverted
                clearable
              ></v-autocomplete></v-col
            ><v-col>
              <v-autocomplete
                v-model="filters.location"
                loading="false"
                :items="locationStore"
                item-text="name"
                item-value="id"
                search-input.sync="search"
                cache-items
                hide-no-data
                label="Location"
                dense
                flat
                hide-details
                rounded
                solo-inverted
                @change="getData"
                clearable
              ></v-autocomplete
            ></v-col>
          </v-row>
        </v-container>
        <v-divider></v-divider>
        <div v-if="itemsLoading">
          <v-skeleton-loader
            class="mx-auto"
            max-width1="300"
            type="list-item-avatar, divider, card-heading, image, actions"
            v-for="n in 3"
            :key="n"
          ></v-skeleton-loader>
        </div>
        <div
          class="caption text-title text-center pa-3"
          v-else-if="!filters.q.length && !items.length"
        >
          What are we looking for?
        </div>
        <div
          class="caption text-title text-center pa-3"
          v-else-if="!items.length"
        >
          No results here yet.
        </div>
        <v-list three-line v-else>
          <template v-for="(item, index) in items">
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

            <v-list-item :to="'/user/' + item.username" v-else :key="index">
              <v-list-item-avatar color="grey darken-2" size="90" rounded="lg">
                <v-img v-if="item.avatar" :src="item.avatar"></v-img>
                <span v-else class="white--text text-h4">{{
                  item.firstname[0]
                }}</span>
              </v-list-item-avatar>

              <v-list-item-content>
                <v-row no-gutter class="mb-n2"
                  ><v-col
                    ><v-list-item-title
                      v-html="item.firstname + ' ' + item.lastname"
                    ></v-list-item-title></v-col
                  ><v-spacer></v-spacer
                  ><v-col cols="2">
                    <badge :badge="item.badge_type"></badge> </v-col
                ></v-row>
                <v-list-item-subtitle>
                  <div>
                    <v-chip
                      class="ma-1"
                      small
                      :key="item.name"
                      v-for="item in item.values"
                    >
                      {{ item.name }}
                    </v-chip>
                  </div>
                  <div>
                    <v-chip
                      class="ma-1"
                      outlined
                      :color="index < 4 ? 'purple' : ''"
                      :key="item.name"
                      v-for="(item, index) in item.skills"
                    >
                      {{ item.name }}
                    </v-chip>
                  </div>
                </v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </template>
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
        <h5 class="pa-10" style="opacity: 0">Ad</h5>
      </v-sheet>
    </v-col>
  </v-row>
</template>


<script>
import Badge from "../Partials/Badge.vue";
export default {
  components: { Badge },
  mounted: function () {
    this.useRouteQuery();
    this.getData();
  },
  methods: {
    useRouteQuery() {
      this.filters.q = this.$route.query.q;
      this.filters.location = this.$route.query.l;
      if (this.$route.query.v) {
        this.filters.values = this.$route.query.v.split(",").map(Number);
      }
    },
    updateRouteQuery() {
      this.$router
        .replace({
          path: "/search",
          query: {
            q: this.filters.q,
            v: this.filters.values.join(","),
            l: this.filters.location,
          },
        })
        .catch((err) => {});
    },
    getData() {
      this.updateRouteQuery();
      this.itemsLoading = true;
      this.$http.post("/search", this.filters).then((response) => {
        this.items = response.data;
        this.itemsLoading = false;
      });
    },
  },
  computed: {
    valueStore() {
      return this.$store.state.values;
    },
    locationStore() {
      var states = this.$store.state.states,
        cities = this.$store.state.cities,
        locationStore = [];
      if (!states.length || !cities.length) {
        return;
      }

      states.forEach(function (o) {
        locationStore.push({
          id: "s-" + o.id,
          name: o.name,
        });
      });
      cities.forEach(function (o) {
        locationStore.push({
          id: "c-" + o.id,
          name: o.name,
        });
      });

      return locationStore;
    },
  },
  data: () => ({
    filters: {
      q: "",
      values: [],
      location: "",
    },
    items: [],
    itemsLoading: false,
  }),
};
</script>