<template>
    <div class="comments">
        <hr>
        <div v-if="!isHidden">
            <div
        class="comments-wrapper">
            <SingleComment
                v-for="comment in comments"
                :comment=comment
                :key="comment.id"
            />
            </div>
            <hr>
        </div>
        <div class="reply">
            <div class="avatar" style="position:absolute; top:7px;">
                <img :src="currentUser.avatar" alt="">
            </div>
            <input
                type="text"
                v-model.trim="reply"
                class="reply--text"
                placeholder="Leave a comment..."
                maxlength="250"
                required
                @keyup.enter="submitComment"
            />
            <button class="reply--button" @click.prevent="submitComment"><i class="fa fa-paper-plane"></i> Send</button>
        </div>
    </div>
</template>

<script>
import SingleComment from './SingleComment'
import { apiService } from "@/common/api.service.js";


export default {
  name: 'MultiComments',
  components: {
    SingleComment
  },
  data () {
    return {
      reply: '',
      next: null,
      loadingComments: false,
    }
  },
  methods: {
    submitComment () {
      if (this.reply != '' ) {
        let endpoint = `/api/comments/`;
        var comment = { text: this.reply, post: this.post_id }
        apiService(endpoint, "POST", comment)
          .then(data => {
            console.log(data)
            this.comments.unshift(data)
          })
        this.reply = '';
        if (this.error) {
          this.error = null;
        }
      }
    },

  },
  props: {
    isHidden: Boolean,
    post_id: '',
    comments: Array
  },
  computed: {
    currentUser(){
      return this.$store.state.user
    }
  }
}
</script>

<style scoped>
.comments-wrapper {
    max-height: 250px;
    overflow-y: auto;
    padding-right: 10px;
}
.comments{
    padding:5px;
}
/* Reply component */
.reply {
    border-radius: 25px;
    display: flex;
    position: relative;
    align-items: center;
    background-color: #EBEBEB;
    padding: 5px;
    margin: 10px;
    overflow: hidden;
}
.reply .avatar {
    position: absolute;
}
.reply .avatar > img {
    width: 40px;
    height: 40px;
    border-radius: 100%;
}
.reply .reply--text {
    min-height: 40px;
    padding: 10px 10px 10px 55px;
    margin-right: 10px;
    border: 0;
    color: #333;
    width: 100%;
    outline: 0;
    background-color: transparent;
    box-shadow: none;
}
.reply input.reply--text:valid {
    margin-right: 71px;
}
.reply input.reply--text:valid + .reply--button {
    right: 10px;
}
.reply .reply--button {
    position: absolute;
    right: -100px;
    border: 1px solid #2a629c;
    background-color: transparent;
    color: #2a629c;
    display: inline-block;
    font-weight: 400;
    text-align: center;
    white-space: nowrap;
    vertical-align: middle;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    padding: 0.375rem 0.75rem;
    font-size: 15px;
    line-height: 1.5;
    border-radius: 30px;
    transition: color 0.25s ease-in-out, background-color 0.25s ease-in-out, border-color 0.25s ease-in-out, box-shadow 0.25s ease-in-out, right 0.25s ease-in-out;
    outline: 0;
}
.reply .reply--button:hover {
    color: #fff;
    background-color: #2a629c;
}
.reply .reply--button:focus,
.reply .reply--button:active {
    box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
}
hr {
    margin-top: 10px;
    margin-bottom: 10px;
}
</style>
