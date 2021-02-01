<template>
<div>
    <v-sheet color="#d8d5db" class= "sheet" rounded="lg">
      <div>
        <v-icon left v-if="post.category=='P'" color="#a759ef" large>mdi-head-lightbulb-outline</v-icon> 
        <v-icon left v-else-if="post.category=='T'" color="#a759ef" large>mdi-brain</v-icon>
        <v-icon left v-else-if="post.category=='O'" color="#a759ef" large>mdi-thought-bubble</v-icon>
      </div>
      <br/>
      <div class="postop">
        <v-avatar size="30">
          <img :src=post.created_by.avatar />
        </v-avatar>
        {{ post.created_by.username }}
      </div>
      <span>{{ post.timestamp  | moment("from", "now") }}</span>
      <br/><br/>
      <div class="title">
        <h3>{{ post.title }}</h3>
        </div>
       <PostCarousel v-bind:images=post.images />
       <div class="desc"><p>{{ post.description }}</p></div>
        <div class="likes">   
       <v-btn text  
                  color="#2c003e" @click.prevent="submitInterest">
                      <v-icon left v-on:click="post.interested='X', post.interest_count = post.interest_count - 1" v-if="post.interested=='I'" color="#a759ef" large>mdi-arrow-up-bold-box</v-icon>
                      <v-icon left v-on:click="post.interested='I', post.interest_count = post.interest_count + 1" v-else color="#a759ef" large>mdi-arrow-up-bold-box-outline</v-icon>
                      {{ post.interest_count }}
                  </v-btn>
                  <v-btn text @click.prevent="submitInterest"
                  color="#2c003e">
                      <v-icon left v-on:click="post.interested='X'" v-if="post.interested=='N'" color="#a759ef" large>mdi-arrow-down-bold-box</v-icon>
                      <v-icon left v-on:click="post.interested='N'" v-else color="#a759ef" large>mdi-arrow-down-bold-box-outline</v-icon>
                  </v-btn>
                  <v-btn text 
                  color="#2c003e">
                      <v-icon left v-if="post.bookmarked" color="#a759ef" large>mdi-bookmark-plus-outline</v-icon>
                      <v-icon left v-else color="#a759ef" large>mdi-bookmark-plus-outline</v-icon>
                  </v-btn>
       </div>
       <div v-on:click="isHidden = !isHidden">
         {{ post.comment_count }} comments.
       </div>
       <MultiComments
          :isHidden = isHidden
          :post_id = post.id
          :comments= post.comments
          :currentUser= currentUser
          />
    </v-sheet>
</div>
</template>
<style scroped lang="scss">
  h1{
    padding:5px;
  }
  p{
    padding:10px;
  }
  @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600&display=swap');

.montserrat {
  font-family: 'Montserrat', sans-serif;;
}
.postop{
  font-family: 'Montserrat', sans-serif;;
  font-size: 15px;
}
.desc{
  font-family: 'Montserrat', sans-serif;;
  font-size: 15px;
}
.comments{
font-size: 12px;
color: #86838a;
}
.sheet{
  padding: 10px;
}
.title{
  font-family: 'Montserrat', sans-serif;;
}
</style>

<script>

import PostCarousel from '../components/PostCarousel.vue'
import MultiComments from '../components/MultiComments.vue'
import { apiService } from "@/common/api.service.js";

export default {
  name: 'PostSheet',
  props: {
    post: Object,
    currentUser: Object()
  },
  components: {
    PostCarousel,
    MultiComments
  },
  data: function () {
    return {
      isHidden: true,
      intersted: null
    }
  },
  created () {
  },
  methods: {
        submitInterest () {
          if(this.post.interest_id != '') {
            let endpoint = `/api/interests/`+this.post.interest_id+'/';
          apiService(endpoint, "DELETE")
          .then(data => {
                      console.log(data);

          })
          }
        let endpoint = `/api/interests/`;
        var interest = { interest: this.post.interested, post: this.post.id }
        apiService(endpoint, "POST", interest)
          .then(data => {
                      this.post.interest_id = data.id

          })
        if (this.error) {
          this.error = null;
        }
    },

  }
}
</script>
