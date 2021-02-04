<template>
  <v-container>
      <div class="comment">
          <img :src="comment.created_by.avatar" alt="" class="avatar" padding=10px>
          <a :href="'/#/user/' + comment.created_by.id+ '/'">{{ comment.created_by.firstname }}</a>

          <div class="commentb">    
              <div >
                <span>{{ comment.text }}</span><br/>
              </div>
          </div>
      <div class="time">
          <div>
            <span>{{ comment.timestamp  | moment("from", "now") }}</span>
          </div>
      </div>
      </div>
  </v-container>
</template>

<script>
export default {
  name: 'SingleComment',
  props: {
    comment: Object
  }
}
</script>

<style>
  @import url("https://fonts.googleapis.com/css?family=Questrial");
.questrial {
  font-family: "Questrial";}
/* Single-comment component */
.comment {
    font-family: "Questrial";
    padding: 20px;
    margin: 5px;
    color: #333;
    background-color: #F2F2F2;
    box-shadow: 1px 1px 3px rgba(0, 0, 0, 0.2);
}
.avatar {
    font-family: "Questrial";
    border-radius: 500px;
    width: 30px;
    height: 30px;
    border-radius: 100%;
    float:left;
}
.time {

    font-variant: small-caps;
    font-size: 10px;
    color: gray;
    font-family: "Questrial";
}
</style>
