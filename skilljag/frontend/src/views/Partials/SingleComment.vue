<template>
  <v-container>
      <div class="comment">
 
          <img v-if="comment.created_by.avatar" :src="comment.created_by.avatar" alt="" class="avatar" padding=10px>
          <span v-else class="grey--text">{{ comment.created_by.firstname[0] }}</span>
          <div class="firstname">
          <a :href="'/#/user/' + comment.created_by.id+ '/'">{{ comment.created_by.firstname }} </a>
          </div>
         

          <div class="text">   
            <br>
                <span>{{ comment.text }}</span><br>
              
          </div>

           
      <div class="time">
            <span>{{ comment.timestamp  | moment("from", "now") }}</span>
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
 /*    font-family: "Questrial";
    padding: 20px;
    margin: 5px;
    color: #333;
    background-color: #F2F2F2;
    -webkit-border-radius: 20px;
    -moz-border-radius: 20px;
     border-radius: 20px;
     color: #000000;
     padding-left: 10px; */
    display: flex;
    position: relative;
    background-color: #EBEBEB;
    overflow: hidden;
    -webkit-border-radius: 20px;
    -moz-border-radius: 20px;
    border-radius: 20px;
    height: fit-content;
    padding: 15px;
    padding-right: 100px;
    padding-bottom: 100px;
    text-align: left;
    align-items: stretch;
    overflow: overlay;
    }

.text{
  position: absolute;
  top: 30px;
  height: auto;
  font-size: 12px;
  


}
.time{
  position: absolute;
  right: 5px;
}
.firstname{
  position: absolute;
  left: 50px;
}
    
.comment:focus {
     outline: none;
     border: 1px solid #a0d18c;
     color: #2d9fd9;
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
